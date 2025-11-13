# Estruturas de Página Comuns

## Descrição Geral
Este documento descreve padrões de layout para as seções estruturais mais comuns encontradas nas páginas do nosso portal, como [[Glossário/Elementos/cabecalhos|cabeçalhos]], rodapés, áreas de conteúdo principal e barras laterais. O objetivo é garantir consistência na disposição dessas macro-áreas em diferentes templates de página.

Estas estruturas são construídas utilizando nosso Sistema de Grid (`grid_system.md`) e Sistema de Espaçamento (`spacing_system.md`).

## Princípios Chave
- **Consistência:** As principais seções estruturais devem ter uma aparência e posicionamento familiares em todo o portal.
- **Clareza Funcional:** Cada seção deve ter um propósito claro e bem definido.
- **Flexibilidade dentro da Estrutura:** Embora a estrutura geral seja consistente, o conteúdo dentro de cada seção variará.
- **Responsividade:** As estruturas devem se adaptar de forma inteligente aos diferentes breakpoints (`breakpoints.md`).

## Estruturas Padrão

### 1. [[Glossário/Elementos/cabecalhos|Cabeçalho]] ([[Glossário/Componentes/header|Header]])
- **Propósito:** Fornecer identidade da marca (logo), navegação principal, busca e, possivelmente, [[Glossário/Elementos/links|links]] de conta/[[Glossário/Padrões/authentication|login]].
- **Posicionamento:** Geralmente fixo no topo da página ou rola com o conteúdo.
- **Layout Típico:**
    - Logo à esquerda.
    - Navegação principal centralizada ou à direita do logo.
    - Busca e [[Glossário/Linguagem Visual/iconografia|ícones]] de conta/carrinho à direita.
- **Responsividade:**
    - Em telas menores, a navegação principal pode ser substituída por um [[Glossário/Componentes/menu|menu]] "hambúrguer".
    - Elementos podem ser reorganizados ou simplificados.
- **Componentes Comuns:** Logo, [[Glossário/Elementos/links|Links]] de Navegação, Campo de Busca, [[Glossário/Elementos/botoes|Botão]] de [[Glossário/Componentes/menu|Menu]] Mobile, [[Glossário/Linguagem Visual/iconografia|Ícones]].

### 2. [[Glossário/Componentes/footer|Rodapé]] ([[Glossário/Componentes/footer|Footer]])
- **Propósito:** Fornecer navegação secundária, informações de contato, [[Glossário/Elementos/links|links]] legais (termos, privacidade), direitos autorais e, possivelmente, [[Glossário/Elementos/links|links]] para redes sociais.
- **Posicionamento:** Sempre na parte inferior da página.
- **Layout Típico:**
    - Pode ser dividido em múltiplas colunas para organizar os [[Glossário/Elementos/links|links]].
    - Informações de direitos autorais geralmente centralizadas ou alinhadas à esquerda na base.
- **Responsividade:**
    - Colunas podem ser empilhadas em telas menores.
    - O [[Glossário/Linguagem Visual/espacamento|espaçamento]] pode ser reduzido.
- **Componentes Comuns:** [[Glossário/Elementos/links|Links]] de Navegação, Texto de Copyright, [[Glossário/Linguagem Visual/iconografia|Ícones]] de Redes Sociais, Logo (opcional, menor).

### 3. Área de Conteúdo Principal (Main Content Area)
- **Propósito:** Exibir o conteúdo primário da página (artigo, [[Glossário/Elementos/listas|lista]] de produtos, [[Glossário/Padrões/form_structure|formulário]], etc.).
- **Posicionamento:** Entre o [[Glossário/Elementos/cabecalhos|cabeçalho]] e o [[Glossário/Componentes/footer|rodapé]]. Pode estar ao lado de uma barra lateral.
- **Layout Típico:**
    - Ocupa a maior parte da largura disponível no grid, especialmente em layouts sem barra lateral.
    - O layout interno varia enormemente dependendo do template da página (`page_templates/`).
- **Responsividade:**
    - O conteúdo deve fluir e se ajustar para manter a legibilidade e usabilidade.
    - [[Glossário/Elementos/imagem|Imagens]] e mídias devem ser responsivas.

### 4. Barra Lateral (Sidebar)
- **Propósito:** Fornecer navegação contextual, [[Glossário/Componentes/filters|filtros]], informações relacionadas, anúncios ou ações secundárias.
- **Posicionamento:** Geralmente à esquerda ou à direita da área de conteúdo principal.
- **Layout Típico:**
    - Ocupa um número menor de colunas do grid (ex: 3 ou 4 de 12 colunas).
    - O conteúdo é disposto verticalmente.
- **Responsividade:**
    - Em telas menores (ex: mobile), a barra lateral é frequentemente ocultada, movida para baixo do conteúdo principal ou acessível através de um [[Glossário/Elementos/botoes|botão]].
- **Componentes Comuns:** [[Glossário/Componentes/menu|Menus]] de Navegação Secundária, [[Glossário/Elementos/listas|Listas]] de [[Glossário/Componentes/filters|Filtros]], [[Glossário/Componentes/cards|Cards]] de Informação, CTAs Secundários.

## Combinações Comuns
- **Página de Largura Total:** [[Glossário/Elementos/cabecalhos|Cabeçalho]], Área de Conteúdo Principal, [[Glossário/Componentes/footer|Rodapé]].
- **Página com Barra Lateral à Direita:** [[Glossário/Elementos/cabecalhos|Cabeçalho]], Área de Conteúdo Principal (esquerda), Barra Lateral (direita), [[Glossário/Componentes/footer|Rodapé]].
- **Página com Barra Lateral à Esquerda:** [[Glossário/Elementos/cabecalhos|Cabeçalho]], Barra Lateral (esquerda), Área de Conteúdo Principal (direita), [[Glossário/Componentes/footer|Rodapé]].

## Diretrizes
- **Hierarquia Clara:** Use o sistema de [[Glossário/Linguagem Visual/espacamento|espaçamento]] para definir claramente os limites entre essas grandes seções.
- **Consistência no Posicionamento:** Por exemplo, se a barra lateral é usada, tente manter seu posicionamento (esquerda/direita) consistente em seções relacionadas do portal.
- **Foco no Conteúdo:** A estrutura deve servir ao conteúdo, não o contrário.

## Recursos Adicionais / Figma
- [[[Glossário/Elementos/links|Link]] para exemplos de estruturas de página no Figma]
- [Templates de página (`page_templates/`) que demonstram essas estruturas] 