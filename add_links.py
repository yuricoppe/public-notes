#!/usr/bin/env python3
"""
Script para adicionar links wikilink [[]] entre páginas do glossário.
Funciona tanto no Obsidian quanto no Quartz 4.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

# Diretório base do glossário
GLOSSARIO_DIR = Path("content/Glossário")

# Mapeamento de termos para seus arquivos
FILE_MAP = {}

def build_file_map():
    """Constrói um mapa de todos os arquivos markdown no glossário."""
    for root, dirs, files in os.walk(GLOSSARIO_DIR):
        for file in files:
            if file.endswith('.md') and file != 'index.md':
                file_path = Path(root) / file
                relative_path = file_path.relative_to(GLOSSARIO_DIR)
                
                # Nome do arquivo sem extensão
                file_name = file[:-3]
                
                # Caminho relativo para o link wikilink
                link_path = str(relative_path)[:-3]  # Remove .md
                
                # Adiciona variações do nome
                variations = [
                    file_name,
                    file_name.replace('_', ' '),
                    file_name.replace('_', ' ').title(),
                ]
                
                for var in variations:
                    if var not in FILE_MAP:
                        FILE_MAP[var] = (link_path, str(file_path))

def get_terms_to_link() -> Dict[str, Tuple[str, str]]:
    """
    Retorna um dicionário de termos que devem ser transformados em links.
    Chave: termo em texto, Valor: (caminho do link, caminho completo do arquivo)
    """
    terms = {}
    
    # Componentes
    components = [
        ('toast', 'Componentes/toast'),
        ('toasts', 'Componentes/toast'),
        ('snackbar', 'Componentes/toast'),
        ('snackbars', 'Componentes/toast'),
        ('dialog', 'Componentes/dialog'),
        ('dialogs', 'Componentes/dialog'),
        ('modal', 'Componentes/dialog'),
        ('modais', 'Componentes/dialog'),
        ('footer', 'Componentes/footer'),
        ('rodapé', 'Componentes/footer'),
        ('header', 'Componentes/header'),
        ('cabeçalho', 'Componentes/header'),
        ('breadcrumbs', 'Componentes/breadcrumbs'),
        ('breadcrumb', 'Componentes/breadcrumbs'),
        ('badges', 'Componentes/badges'),
        ('badge', 'Componentes/badges'),
        ('data tables', 'Componentes/data_tables'),
        ('tabela de dados', 'Componentes/data_tables'),
        ('tabelas de dados', 'Componentes/data_tables'),
        ('loading spinner', 'Componentes/loading_spinner'),
        ('spinner', 'Componentes/loading_spinner'),
        ('menu', 'Componentes/menu'),
        ('menus', 'Componentes/menu'),
        ('messaging', 'Componentes/messaging'),
        ('mensagens', 'Componentes/messaging'),
        ('inline error', 'Componentes/inline_error'),
        ('erro inline', 'Componentes/inline_error'),
        ('erros inline', 'Componentes/inline_error'),
        ('cards', 'Componentes/cards'),
        ('card', 'Componentes/cards'),
        ('cartões', 'Componentes/cards'),
        ('filters', 'Componentes/filters'),
        ('filtros', 'Componentes/filters'),
        ('calendar picker', 'Componentes/calendar_picker'),
        ('seletor de calendário', 'Componentes/calendar_picker'),
        ('drawer accordion', 'Componentes/drawer_accordion'),
        ('accordion', 'Componentes/drawer_accordion'),
        ('cookie notification', 'Componentes/cookie_notification'),
        ('notificação de cookies', 'Componentes/cookie_notification'),
        ('action bar sheet', 'Componentes/action_bar_sheet'),
        ('back to top', 'Componentes/back_to_top'),
        ('block container', 'Componentes/block_container'),
        ('caption', 'Componentes/caption'),
        ('chat live', 'Componentes/chat_live'),
        ('code block', 'Componentes/code_block'),
        ('comments', 'Componentes/comments'),
        ('comentários', 'Componentes/comments'),
        ('contact us', 'Componentes/contact_us'),
        ('footnotes', 'Componentes/footnotes'),
        ('notas de rodapé', 'Componentes/footnotes'),
        ('hero billboard', 'Componentes/hero_billboard'),
        ('hero carousel', 'Componentes/hero_carousel'),
        ('legend', 'Componentes/legend'),
        ('legenda', 'Componentes/legend'),
        ('local navigation', 'Componentes/local_navigation'),
        ('maps', 'Componentes/maps'),
        ('mapas', 'Componentes/maps'),
    ]
    
    # Elementos
    elements = [
        ('botões', 'Elementos/botoes'),
        ('botão', 'Elementos/botoes'),
        ('button', 'Elementos/botoes'),
        ('buttons', 'Elementos/botoes'),
        ('controles de formulário', 'Elementos/form_controls'),
        ('form controls', 'Elementos/form_controls'),
        ('campo de texto', 'Elementos/form_controls'),
        ('campos de texto', 'Elementos/form_controls'),
        ('text input', 'Elementos/form_controls'),
        ('checkbox', 'Elementos/form_controls'),
        ('checkboxes', 'Elementos/form_controls'),
        ('caixa de seleção', 'Elementos/form_controls'),
        ('caixas de seleção', 'Elementos/form_controls'),
        ('radio button', 'Elementos/form_controls'),
        ('botão de rádio', 'Elementos/form_controls'),
        ('botões de rádio', 'Elementos/form_controls'),
        ('dropdown', 'Elementos/form_controls'),
        ('menu suspenso', 'Elementos/form_controls'),
        ('menus suspensos', 'Elementos/form_controls'),
        ('select', 'Elementos/form_controls'),
        ('slider', 'Elementos/slider'),
        ('sliders', 'Elementos/slider'),
        ('links', 'Elementos/links'),
        ('link', 'Elementos/links'),
        ('cabeçalhos', 'Elementos/cabecalhos'),
        ('cabeçalho', 'Elementos/cabecalhos'),
        ('headings', 'Elementos/cabecalhos'),
        ('heading', 'Elementos/cabecalhos'),
        ('listas', 'Elementos/listas'),
        ('lista', 'Elementos/listas'),
        ('imagem', 'Elementos/imagem'),
        ('imagens', 'Elementos/imagem'),
        ('interruptor', 'Elementos/interruptor'),
        ('toggle', 'Elementos/interruptor'),
        ('toggles', 'Elementos/interruptor'),
        ('switches', 'Elementos/interruptor'),
        ('switch', 'Elementos/interruptor'),
        ('block quote', 'Elementos/block_quote'),
        ('citação', 'Elementos/block_quote'),
        ('código', 'Elementos/codigo'),
        ('divisor', 'Elementos/divisor'),
        ('lead paragraph', 'Elementos/lead_paragraph'),
        ('parágrafo', 'Elementos/paragrafo'),
        ('parágrafos', 'Elementos/paragrafo'),
    ]
    
    # Padrões
    patterns = [
        ('configurações', 'Padrões/settings'),
        ('settings', 'Padrões/settings'),
        ('estrutura de formulário', 'Padrões/form_structure'),
        ('form structure', 'Padrões/form_structure'),
        ('formulário', 'Padrões/form_structure'),
        ('formulários', 'Padrões/form_structure'),
        ('authentication', 'Padrões/authentication'),
        ('autenticação', 'Padrões/authentication'),
        ('login', 'Padrões/authentication'),
        ('create account', 'Padrões/create_account'),
        ('criação de conta', 'Padrões/create_account'),
        ('registro', 'Padrões/create_account'),
        ('sign-up', 'Padrões/create_account'),
        ('permissions', 'Padrões/permissions'),
        ('permissões', 'Padrões/permissions'),
        ('swipe to refresh', 'Padrões/swipe_to_refresh'),
        ('purchase checkout', 'Padrões/purchase_checkout'),
        ('checkout', 'Padrões/purchase_checkout'),
        ('database connection', 'Padrões/database_connection'),
        ('launch', 'Padrões/launch'),
        ('onboarding', 'Padrões/launch'),
        ('site app structure', 'Padrões/site_app_structure'),
        ('estrutura do site', 'Padrões/site_app_structure'),
    ]
    
    # Linguagem Visual
    visual = [
        ('cor', 'Linguagem Visual/cor'),
        ('cores', 'Linguagem Visual/cor'),
        ('color', 'Linguagem Visual/cor'),
        ('espaçamento', 'Linguagem Visual/espacamento'),
        ('spacing', 'Linguagem Visual/espacamento'),
        ('iconografia', 'Linguagem Visual/iconografia'),
        ('ícones', 'Linguagem Visual/iconografia'),
        ('ícone', 'Linguagem Visual/iconografia'),
        ('icons', 'Linguagem Visual/iconografia'),
        ('tipografia', 'Linguagem Visual/tipografia'),
        ('typography', 'Linguagem Visual/tipografia'),
        ('estrutura layout', 'Linguagem Visual/estrutura_layout'),
        ('fotografia', 'Linguagem Visual/fotografia'),
        ('métricas', 'Linguagem Visual/metricas_e_keylines'),
        ('keylines', 'Linguagem Visual/metricas_e_keylines'),
        ('movimento', 'Linguagem Visual/movimento'),
        ('motion', 'Linguagem Visual/movimento'),
        ('paletas', 'Linguagem Visual/paletas_por_categoria'),
        ('princípios movimento', 'Linguagem Visual/principios_movimento'),
    ]
    
    # Sistemas de Layout
    layout_systems = [
        ('breakpoints', 'Sistemas de Layout/breakpoints'),
        ('containers', 'Sistemas de Layout/containers_wrappers'),
        ('wrappers', 'Sistemas de Layout/containers_wrappers'),
        ('grid system', 'Sistemas de Layout/grid_system'),
        ('sistema de grid', 'Sistemas de Layout/grid_system'),
        ('page structures', 'Sistemas de Layout/page_structures'),
        ('spacing system', 'Sistemas de Layout/spacing_system'),
        ('sistema de espaçamento', 'Sistemas de Layout/spacing_system'),
    ]
    
    # Entregáveis - termos mais genéricos para evitar muitos links
    deliverables = [
        ('persona', 'Entregáveis/persona'),
        ('personas', 'Entregáveis/persona'),
        ('proto persona', 'Entregáveis/proto_persona'),
        ('proto-persona', 'Entregáveis/proto_persona'),
        ('qualitative persona', 'Entregáveis/qualitative_persona'),
        ('persona qualitativa', 'Entregáveis/qualitative_persona'),
        ('statistical persona', 'Entregáveis/statistical_persona'),
        ('persona estatística', 'Entregáveis/statistical_persona'),
        ('antipersona', 'Entregáveis/antipersona'),
        ('anti-persona', 'Entregáveis/antipersona'),
        ('stakeholder persona', 'Entregáveis/stakeholder_persona'),
        ('stakeholder profile', 'Entregáveis/stakeholder_profile'),
        ('wireframe', 'Entregáveis/wireframe'),
        ('wireframes', 'Entregáveis/wireframe'),
        ('prototype', 'Entregáveis/prototype'),
        ('protótipo', 'Entregáveis/prototype'),
        ('protótipos', 'Entregáveis/prototype'),
        ('paper prototype', 'Entregáveis/paper_prototype'),
        ('protótipo de papel', 'Entregáveis/paper_prototype'),
        ('prototype specification', 'Entregáveis/prototype_specification'),
        ('mockup', 'Entregáveis/mockup'),
        ('mockups', 'Entregáveis/mockup'),
        ('journey map', 'Entregáveis/journey_map'),
        ('mapa de jornada', 'Entregáveis/journey_map'),
        ('experience map', 'Entregáveis/experience_map'),
        ('mapa de experiência', 'Entregáveis/experience_map'),
        ('user flow', 'Entregáveis/user_flow'),
        ('fluxo de usuário', 'Entregáveis/user_flow'),
        ('user story map', 'Entregáveis/user_story_map'),
        ('wireflow', 'Entregáveis/wireflow'),
        ('design system', 'Entregáveis/design_system'),
        ('sistema de design', 'Entregáveis/design_system'),
        ('style guide', 'Entregáveis/style_guide'),
        ('guia de estilo', 'Entregáveis/style_guide'),
        ('storyboard', 'Entregáveis/storyboard'),
        ('empathy map', 'Entregáveis/empathy_map'),
        ('mapa de empatia', 'Entregáveis/empathy_map'),
        ('affinity diagram', 'Entregáveis/affinity_diagram'),
        ('diagrama de afinidade', 'Entregáveis/affinity_diagram'),
        ('service blueprint', 'Entregáveis/service_blueprint'),
        ('blueprint de serviço', 'Entregáveis/service_blueprint'),
        ('site map', 'Entregáveis/site_map'),
        ('sitemap', 'Entregáveis/site_map'),
        ('mapa do site', 'Entregáveis/site_map'),
        ('mood board', 'Entregáveis/mood_board'),
        ('moodboard', 'Entregáveis/mood_board'),
        ('painel semântico', 'Entregáveis/mood_board'),
        ('content audit', 'Entregáveis/content_audit'),
        ('auditoria de conteúdo', 'Entregáveis/content_audit'),
        ('content inventory', 'Entregáveis/content_inventory'),
        ('inventário de conteúdo', 'Entregáveis/content_inventory'),
        ('research plan', 'Entregáveis/research_plan'),
        ('plano de pesquisa', 'Entregáveis/research_plan'),
        ('interview guide', 'Entregáveis/interview_guide'),
        ('roteiro de entrevista', 'Entregáveis/interview_guide'),
        ('survey', 'Entregáveis/survey'),
        ('questionário', 'Entregáveis/survey'),
        ('screener', 'Entregáveis/screener'),
        ('questionário de triagem', 'Entregáveis/screener'),
        ('usability report', 'Entregáveis/usability_report'),
        ('relatório de usabilidade', 'Entregáveis/usability_report'),
        ('analytics report', 'Entregáveis/analytics_report'),
        ('relatório de analytics', 'Entregáveis/analytics_report'),
        ('dashboard', 'Entregáveis/dashboard'),
        ('research repository', 'Entregáveis/research_repository'),
        ('repositório de pesquisa', 'Entregáveis/research_repository'),
        ('promptframe', 'Entregáveis/promptframe'),
        ('sketch test', 'Entregáveis/sketch_test'),
        ('archetype', 'Entregáveis/archetype'),
        ('arquétipo', 'Entregáveis/archetype'),
        ('mind map', 'Entregáveis/mind_map'),
        ('mapa mental', 'Entregáveis/mind_map'),
        ('concept map', 'Entregáveis/concept_map'),
        ('mapa conceitual', 'Entregáveis/concept_map'),
        ('cognitive map', 'Entregáveis/cognitive_map'),
        ('mapa cognitivo', 'Entregáveis/cognitive_map'),
        ('process map', 'Entregáveis/process_map'),
        ('mapa de processo', 'Entregáveis/process_map'),
        ('ecosystem map', 'Entregáveis/ecosystem_map'),
        ('mapa de ecossistema', 'Entregáveis/ecosystem_map'),
        ('landscape map', 'Entregáveis/landscape_map'),
        ('chronological map', 'Entregáveis/chronological_map'),
        ('scenario map', 'Entregáveis/scenario_map'),
        ('relationship map', 'Entregáveis/relationship_map'),
        ('asset map', 'Entregáveis/asset_map'),
        ('skill map', 'Entregáveis/skill_map'),
        ('product roadmap', 'Entregáveis/product_roadmap'),
        ('ux roadmap', 'Entregáveis/ux_roadmap'),
        ('field roadmap', 'Entregáveis/field_roadmap'),
        ('specialty roadmap', 'Entregáveis/specialty_roadmap'),
        ('job to be done', 'Entregáveis/job_to_be_done'),
        ('jtbd', 'Entregáveis/job_to_be_done'),
        ('story ux', 'Entregáveis/story_ux'),
        ('história ux', 'Entregáveis/story_ux'),
        ('kano model', 'Entregáveis/kano_model'),
        ('modelo kano', 'Entregáveis/kano_model'),
        ('hta diagram', 'Entregáveis/hta_diagram'),
        ('csd matrix', 'Entregáveis/csd_matrix'),
        ('matriz csd', 'Entregáveis/csd_matrix'),
        ('impact effort matrix', 'Entregáveis/impact_effort_matrix'),
        ('matriz impacto esforço', 'Entregáveis/impact_effort_matrix'),
        ('raci matrix', 'Entregáveis/raci_matrix'),
        ('matriz raci', 'Entregáveis/raci_matrix'),
        ('moscow analysis', 'Entregáveis/moscow_analysis'),
        ('análise moscow', 'Entregáveis/moscow_analysis'),
        ('rice method', 'Entregáveis/rice_method'),
        ('método rice', 'Entregáveis/rice_method'),
        ('feasibility desirability viability scorecard', 'Entregáveis/feasibility_desirability_viability_scorecard'),
    ]
    
    all_terms = components + elements + patterns + visual + layout_systems + deliverables
    
    for term, path in all_terms:
        full_path = str(GLOSSARIO_DIR / f"{path}.md")
        if os.path.exists(full_path):
            terms[term] = (path, full_path)
    
    return terms

def add_links_to_file(file_path: str, terms: Dict[str, Tuple[str, str]]) -> bool:
    """
    Adiciona links wikilink a um arquivo.
    Retorna True se o arquivo foi modificado.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    current_file_relative = str(Path(file_path).relative_to(GLOSSARIO_DIR))[:-3]
    
    # Evita linkar para si mesmo
    terms_to_process = {k: v for k, v in terms.items() if v[0] != current_file_relative}
    
    # Ordena os termos por tamanho (maior primeiro) para evitar substituições parciais
    sorted_terms = sorted(terms_to_process.items(), key=lambda x: len(x[0]), reverse=True)
    
    for term, (link_path, _) in sorted_terms:
        # Padrões para encontrar o termo sem já ter um link
        # Evita adicionar links dentro de:
        # - Links existentes [[...]]
        # - Código `...` ou ```...```
        # - URLs
        
        # Regex para encontrar o termo, mas não dentro de links wikilink ou código
        # Pattern: termo que não está dentro de [[ ]] ou ` `
        pattern = r'(?<!\[\[)(?<!`)\b(' + re.escape(term) + r')\b(?!`|]])'
        
        # Função para substituir, mas verificar contexto
        def replace_term(match):
            start = max(0, match.start() - 10)
            end = min(len(content), match.end() + 10)
            context = content[start:end]
            
            # Não substituir se já estiver em um link wikilink
            if '[[' in context[:10] or ']]' in context[-10:]:
                return match.group(0)
            
            # Não substituir se estiver em código inline
            if '`' in context[:10] or '`' in context[-10:]:
                return match.group(0)
            
            # Não substituir em blocos de código (aproximação)
            line_start = content.rfind('\n', 0, match.start())
            line_end = content.find('\n', match.end())
            line = content[line_start:line_end] if line_end != -1 else content[line_start:]
            if line.strip().startswith('```') or '    ' in line[:4]:
                return match.group(0)
            
            # Não substituir dentro de [texto] para links markdown
            # Verifica se está dentro de colchetes de link markdown
            context_before = content[max(0, match.start() - 50):match.start()]
            context_after = content[match.end():min(len(content), match.end() + 50)]
            
            # Se há um [ antes sem ] no meio, e um ] depois sem [ no meio
            last_bracket_open = context_before.rfind('[')
            last_bracket_close = context_before.rfind(']')
            next_bracket_close = context_after.find(']')
            next_bracket_open = context_after.find('[')
            
            if last_bracket_open > last_bracket_close:
                # Estamos dentro de um [...]
                if next_bracket_close != -1 and (next_bracket_open == -1 or next_bracket_close < next_bracket_open):
                    # E há um ] fechando
                    return match.group(0)
            
            # Criar o link wikilink com prefixo Glossário/
            return f'[[Glossário/{link_path}|{match.group(1)}]]'
        
        content = re.sub(pattern, replace_term, content, flags=re.IGNORECASE)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def process_all_files():
    """Processa todos os arquivos markdown no glossário."""
    terms = get_terms_to_link()
    modified_count = 0
    
    print(f"Processando arquivos no diretório: {GLOSSARIO_DIR}")
    print(f"Total de termos para linkar: {len(terms)}\n")
    
    for root, dirs, files in os.walk(GLOSSARIO_DIR):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                relative_path = Path(file_path).relative_to(GLOSSARIO_DIR)
                
                if add_links_to_file(file_path, terms):
                    print(f"✓ Modificado: {relative_path}")
                    modified_count += 1
                else:
                    print(f"  Sem mudanças: {relative_path}")
    
    print(f"\n{'='*60}")
    print(f"Total de arquivos modificados: {modified_count}")
    print(f"{'='*60}")

if __name__ == "__main__":
    if not GLOSSARIO_DIR.exists():
        print(f"Erro: Diretório {GLOSSARIO_DIR} não encontrado!")
        exit(1)
    
    print("Iniciando processamento de links no glossário...\n")
    process_all_files()
    print("\nProcessamento concluído!")
