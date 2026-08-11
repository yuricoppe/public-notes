#!/usr/bin/env python3
"""Estima a largura de cada <text> num SVG e aponta o que vaza do viewBox.

O estimador anterior usava 0,52 em por caractere para tudo, o que subestima
maiúsculas (~0,70) e negrito. Este usa largura por classe de caractere.
"""
import re, sys, glob, os, xml.dom.minidom

NARROW = set("iljtfrI.,;:'|!()[]{}·")
WIDE = set("mwMWQ@%")
UPPER = set("ABCDEFGHJKLNOPRSTUVXYZÁÉÍÓÚÂÊÔÃÕÇ")

def char_w(c):
    if c == ' ': return 0.27
    if c in NARROW: return 0.30
    if c in WIDE: return 0.83
    if c in UPPER: return 0.68
    if c.isupper(): return 0.68
    if c.isdigit(): return 0.56
    if c in '—–': return 0.85
    return 0.52

def text_w(s, size, bold):
    w = sum(char_w(c) for c in s) * size
    return w * (1.06 if bold else 1.0)

def sizes_from_style(svg):
    """Lê font-size e font-weight declarados por classe no <style>."""
    out = {}
    for m in re.finditer(r'\.([\w-]+)\s*\{([^}]*)\}', svg):
        cls, body = m.group(1), m.group(2)
        fs = re.search(r'font-size:\s*([\d.]+)px', body)
        fw = re.search(r'font-weight:\s*(\d+|bold)', body)
        if fs or fw:
            out[cls] = (float(fs.group(1)) if fs else None,
                        bool(fw) and (fw.group(1) in ('bold',) or int(fw.group(1)) >= 600))
    return out

def check(path, verbose=False):
    s = open(path, encoding='utf-8').read()
    xml.dom.minidom.parseString(s)  # levanta se o XML for inválido
    vb = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', s)
    W, H = float(vb.group(1)), float(vb.group(2))
    styles = sizes_from_style(s)
    problems = []
    for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', s, re.S):
        attrs, inner = m.group(1), m.group(2)
        if 'transform' in attrs:      # rotacionado: não dá para medir assim
            continue
        xm = re.search(r'\bx="([-\d.]+)"', attrs)
        ym = re.search(r'\by="([-\d.]+)"', attrs)
        if not xm or not ym: continue
        x, y = float(xm.group(1)), float(ym.group(1))
        cls = (re.search(r'class="([^"]*)"', attrs) or [None, ''])[1]
        size, bold = None, False
        for c in cls.split():
            if c in styles:
                fs, fb = styles[c]
                if fs: size = fs
                bold = bold or fb
        fs_attr = re.search(r'font-size="([\d.]+)"', attrs)
        if fs_attr: size = float(fs_attr.group(1))
        if 'font-weight="700"' in attrs or 'font-weight="bold"' in attrs: bold = True
        if size is None: size = 12.5
        txt = re.sub(r'<[^>]+>', '', inner)
        anchor = re.search(r'text-anchor="(\w+)"', attrs)
        w = text_w(txt, size, bold)
        right = x + w
        if anchor and anchor.group(1) == 'middle': right = x + w / 2
        if anchor and anchor.group(1) == 'end': right = x
        if right > W + 2:
            problems.append(('LARGO', round(right), txt.strip()[:78]))
        if y > H - 3:
            problems.append(('ALTO', y, txt.strip()[:78]))
    return W, H, problems

if __name__ == '__main__':
    pats = sys.argv[1:] or ['content/attachments/*.svg']
    total = 0
    for pat in pats:
        for f in sorted(glob.glob(pat)):
            W, H, probs = check(f)
            if probs:
                print(f'\n{os.path.basename(f)}  (viewBox {W:.0f}×{H:.0f})')
                for kind, val, txt in probs:
                    print(f'   {kind:5} {val:>5}  {txt}')
                total += len(probs)
    print(f'\ntotal de problemas: {total}')
