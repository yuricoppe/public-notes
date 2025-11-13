#!/usr/bin/env python3
"""
Script para verificar quais arquivos do glossário estão mapeados para receber links
"""

import os
import sys
from pathlib import Path

# Importa a função do add_links.py
sys.path.insert(0, str(Path(__file__).parent))
from add_links import get_terms_to_link, GLOSSARIO_DIR

def main():
    # Pega todos os termos mapeados
    terms = get_terms_to_link()
    
    # Extrai os caminhos únicos dos arquivos que são destino de links
    mapped_paths = set()
    for term, (path, full_path) in terms.items():
        # Remove o .md e pega só o nome relativo
        mapped_paths.add(path)
    
    # Pega todos os arquivos markdown do glossário
    all_files = []
    for root, dirs, files in os.walk(GLOSSARIO_DIR):
        # Ignora diretórios que começam com .
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.endswith('.md') and file not in ['index.md', 'README.md']:
                file_path = Path(root) / file
                relative_path = file_path.relative_to(GLOSSARIO_DIR)
                # Remove o .md
                path_without_ext = str(relative_path)[:-3]
                all_files.append(path_without_ext)
    
    # Identifica arquivos não mapeados
    unmapped_files = sorted(set(all_files) - mapped_paths)
    
    # Agrupa por categoria
    categories = {}
    for file_path in unmapped_files:
        category = file_path.split('/')[0] if '/' in file_path else 'Root'
        if category not in categories:
            categories[category] = []
        file_name = file_path.split('/')[-1]
        categories[category].append(file_name)
    
    # Imprime resultado
    print(f"Total de arquivos no glossário: {len(all_files)}")
    print()
    print("=" * 70)
    print("ARQUIVOS NÃO MAPEADOS PARA LINKS:")
    print("=" * 70)
    
    for file_path in unmapped_files:
        category = file_path.split('/')[0] if '/' in file_path else 'Root'
        file_name = file_path.split('/')[-1] + '.md'
        print(f"  • {file_path}.md".ljust(60) + f"({category})")
    
    print()
    print("=" * 70)
    print("RESUMO:")
    print(f"  Total de arquivos: {len(all_files)}")
    print(f"  Mapeados: {len(mapped_paths)}")
    print(f"  Não mapeados: {len(unmapped_files)}")
    print(f"  Cobertura: {len(mapped_paths) / len(all_files) * 100:.1f}%")
    print("=" * 70)
    
    print()
    print("POR CATEGORIA:")
    print()
    for category in sorted(categories.keys()):
        files = categories[category]
        print(f"{category} ({len(files)}):")
        for file_name in sorted(files):
            print(f"    - {file_name}")
        print()

if __name__ == '__main__':
    main()
