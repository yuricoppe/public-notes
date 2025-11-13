#!/usr/bin/env python3
"""
Script para adicionar o prefixo 'Glossário/' aos wikilinks existentes
"""

import os
import re
from pathlib import Path

GLOSSARIO_DIR = Path("content/Glossário")

def fix_links_in_file(file_path: str) -> bool:
    """
    Adiciona o prefixo Glossário/ aos links wikilink que não o têm.
    Retorna True se o arquivo foi modificado.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Padrão para encontrar wikilinks sem o prefixo Glossário/
    # Categorias conhecidas: Componentes, Elementos, Padrões, Linguagem Visual, Sistemas de Layout, Entregáveis
    categories = [
        'Componentes',
        'Elementos',
        'Padrões',
        'Linguagem Visual',
        'Sistemas de Layout',
        'Entregáveis'
    ]
    
    for category in categories:
        # Padrão: [[Categoria/arquivo|texto]] mas não [[Glossário/Categoria/arquivo|texto]]
        pattern = r'\[\[(' + re.escape(category) + r'/[^\]|]+)(\|[^\]]+)?\]\]'
        
        def replace_link(match):
            path = match.group(1)
            alias = match.group(2) if match.group(2) else ''
            
            # Já tem o prefixo Glossário/?
            if path.startswith('Glossário/'):
                return match.group(0)
            
            return f'[[Glossário/{path}{alias}]]'
        
        content = re.sub(pattern, replace_link, content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def main():
    """Processa todos os arquivos markdown no glossário."""
    modified_count = 0
    
    print("Corrigindo links em arquivos do glossário...")
    print("=" * 60)
    
    for root, dirs, files in os.walk(GLOSSARIO_DIR):
        # Ignora diretórios que começam com .
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                relative_path = Path(file_path).relative_to(GLOSSARIO_DIR)
                
                if fix_links_in_file(file_path):
                    print(f"✓ Modificado: {relative_path}")
                    modified_count += 1
                else:
                    print(f"  Sem mudanças: {relative_path}")
    
    print()
    print("=" * 60)
    print(f"Total de arquivos modificados: {modified_count}")
    print("=" * 60)
    print()
    print("Processamento concluído!")

if __name__ == '__main__':
    main()
