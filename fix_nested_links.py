#!/usr/bin/env python3
"""
Script para corrigir links wikilink aninhados [[..[[..]]..]]
"""

import os
import re
from pathlib import Path

GLOSSARIO_DIR = Path("content/Glossário")

def fix_nested_links(content: str) -> str:
    """
    Corrige links wikilink aninhados.
    Exemplo: [[Elementos/form_controls|[[Componentes/menu|menus]] suspensos]]
    Deve se tornar: [[Componentes/menu|menus]] suspensos
    """
    # Pattern para encontrar links aninhados
    # [[outer|[[inner|text]]]]
    pattern = r'\[\[([^\[\]]+)\|\[\[([^\[\]]+)\|([^\[\]]+)\]\]([^\]]*)\]\]'
    
    def replace_nested(match):
        # outer_path = match.group(1)
        inner_path = match.group(2)
        inner_text = match.group(3)
        remaining = match.group(4)
        # Mantém apenas o link interno mais específico
        return f'[[{inner_path}|{inner_text}]]{remaining}'
    
    # Repete até não haver mais links aninhados
    max_iterations = 10
    iteration = 0
    while '[[' in content and iteration < max_iterations:
        new_content = re.sub(pattern, replace_nested, content)
        if new_content == content:
            break
        content = new_content
        iteration += 1
    
    return content

def process_file(file_path: str) -> bool:
    """
    Processa um arquivo para corrigir links aninhados.
    Retorna True se o arquivo foi modificado.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    fixed_content = fix_nested_links(content)
    
    if fixed_content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        return True
    
    return False

def main():
    """Processa todos os arquivos markdown no glossário."""
    modified_count = 0
    
    print(f"Processando arquivos no diretório: {GLOSSARIO_DIR}")
    print("Corrigindo links aninhados...\n")
    
    for root, dirs, files in os.walk(GLOSSARIO_DIR):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                relative_path = Path(file_path).relative_to(GLOSSARIO_DIR)
                
                if process_file(file_path):
                    print(f"✓ Corrigido: {relative_path}")
                    modified_count += 1
    
    print(f"\n{'='*60}")
    print(f"Total de arquivos corrigidos: {modified_count}")
    print(f"{'='*60}")

if __name__ == "__main__":
    if not GLOSSARIO_DIR.exists():
        print(f"Erro: Diretório {GLOSSARIO_DIR} não encontrado!")
        exit(1)
    
    print("Iniciando correção de links aninhados...\n")
    main()
    print("\nProcessamento concluído!")
