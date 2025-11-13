# Drawer / Accordion (Gaveta / Acordeão)

"Drawer" (Gaveta) e "Accordion" (Acordeão) são componentes de interface utilizados para mostrar e ocultar seções de conteúdo, ajudando a organizar informações e reduzir a desordem visual. Embora agrupados aqui pela funcionalidade de revelação de conteúdo, possuem características e usos distintos.

## Drawer (Gaveta)

Drawers, também conhecidos como "Off-Canvas Panels" ou "Sidebars Móveis", são painéis que deslizam para dentro ou para fora da viewport, geralmente a partir da lateral (esquerda ou direita) ou da parte inferior/superior da tela. São muito usados para navegação ou [[Componentes/filters|filtros]] em interfaces mobile.

### Casos de Uso do Drawer:
-   [[Componentes/menu|Menu]] de navegação principal em dispositivos móveis (ex: [[Componentes/menu|menu]] hambúrguer).
-   [[Componentes/filters|Filtros]] e opções de ordenação em listagens.
-   Painéis de [[Padrões/settings|configurações]] rápidas.
-   Carrinho de compras em e-commerce mobile.
-   Notificações ou feeds laterais.

### Elementos Comuns do Drawer:
-   **Gatilho (Trigger):** [[Elementos/botoes|Botão]] (ex: [[Linguagem Visual/iconografia|ícone]] de hambúrguer, [[Linguagem Visual/iconografia|ícone]] de filtro) que abre e fecha o drawer.
-   **Painel do Drawer:** O contêiner que desliza e contém o conteúdo.
-   **Conteúdo:** [[Elementos/links|Links]] de navegação, [[Padrões/form_structure|formulários]] de filtro, [[Padrões/settings|configurações]], etc.
-   **(Opcional) [[Elementos/cabecalhos|Cabeçalho]] no Drawer:** Título e/ou [[Elementos/botoes|botão]] de fechar.
-   **(Opcional) Overlay:** Para escurecer o conteúdo principal quando o drawer está aberto.

### Melhores Práticas do Drawer:
-   **Transição Suave:** A animação de entrada/saída deve ser rápida e fluida.
-   **Fechamento Fácil:** Além do gatilho, permitir fechar clicando no overlay (se houver) ou com a tecla `Escape`.
-   **Foco:** Gerenciar o foco do teclado para dentro do drawer quando aberto.
-   **Estado Visível:** Indicar claramente quando o drawer está ativo/aberto.
-   **Acessibilidade:** Usar `aria-controls`, `aria-expanded` no gatilho. O drawer pode ter `role="dialog"` e `aria-modal="true"` se cobrir toda a tela e impedir interação com o fundo, ou `role="region"` se for complementar.

## Accordion (Acordeão)

Accordions são [[Elementos/listas|listas]] de [[Elementos/cabecalhos|cabeçalhos]] empilhados verticalmente, onde cada [[Elementos/cabecalhos|cabeçalho]] pode ser clicado para revelar ou ocultar uma seção de conteúdo associada abaixo dele. Apenas um (ou múltiplos, dependendo da configuração) painel de conteúdo fica visível por vez.

### Casos de Uso do Accordion:
-   FAQs (Perguntas Frequentes).
-   Sumários de conteúdo longo, permitindo expandir seções.
-   [[Componentes/menu|Menus]] de navegação multinível compactos.
-   [[Padrões/settings|Configurações]] com múltiplas seções.
-   Linhas de tempo ou processos passo a passo.

### Elementos Comuns do Accordion:
-   **Item do Accordion:** Consiste em um [[Elementos/cabecalhos|cabeçalho]] e um painel de conteúdo.
-   **[[Elementos/cabecalhos|Cabeçalho]] ([[Componentes/header|Header]]/Trigger):** Texto do título da seção, clicável para expandir/recolher.
    *   Geralmente inclui um [[Linguagem Visual/iconografia|ícone]] indicador (ex: `+`/`-`, `▼`/`▲`) do estado (expandido/recolhido).
-   **Painel de Conteúdo (Content Panel):** A área que é mostrada/oculta.

### Melhores Práticas do Accordion:
-   **Indicação Clara de Estado:** O [[Linguagem Visual/iconografia|ícone]] no [[Elementos/cabecalhos|cabeçalho]] deve mudar para refletir se o painel está aberto ou fechado.
-   **Transição Suave:** Animação sutil ao abrir/fechar painéis.
-   **Um Painel Aberto por Vez (Comum):** Tradicionalmente, abrir um painel fecha o que estava aberto anteriormente. Permitir múltiplos painéis abertos simultaneamente é uma variação.
-   **Acessibilidade:**
    *   Os [[Elementos/cabecalhos|cabeçalhos]] devem ser botões (`<button>`) ou links, controlando a visibilidade do painel.
    *   Usar `aria-expanded` no gatilho para indicar o estado.
    *   Associar o gatilho ao painel com `aria-controls` (o painel deve ter um `id`).
    *   O painel pode ter `role="region"` e um `aria-labelledby` referenciando o [[Elementos/botoes|botão]] do [[Elementos/cabecalhos|cabeçalho]].
-   **Conteúdo Escaneável:** Mesmo quando recolhido, os títulos dos [[Elementos/cabecalhos|cabeçalhos]] devem dar uma boa ideia do conteúdo dentro de cada seção.

## O Que Evitar (para ambos)

-   Animações lentas ou que travam.
-   Esconder conteúdo crucial que o usuário precisa ver imediatamente.
-   Má gestão do foco do teclado.
-   Indicadores de estado confusos ou ausentes.
-   No Accordion: Ninhos muito profundos de acordeões dentro de acordeões.
-   No Drawer: Usar para conteúdo que deveria estar sempre visível ou que exige muito contexto da página principal. 