# Header ([[Elementos/cabecalhos|Cabeçalho]] de Página/Seção)

O componente Header ([[Elementos/cabecalhos|Cabeçalho]]), neste contexto, refere-se a uma área no topo de uma página, seção ou componente (como um [[Componentes/cards|Card]] ou [[Componentes/dialog|Modal]]) que introduz o conteúdo subsequente. Ele é distinto do "Global Header/Navbar" ([[Elementos/cabecalhos|cabeçalho]] de navegação principal do site).

## Casos de Uso

-   **[[Elementos/cabecalhos|Cabeçalho]] de Página:** Contém o título principal da página (H1), possivelmente um subtítulo ou [[Componentes/breadcrumbs|breadcrumbs]].
-   **[[Elementos/cabecalhos|Cabeçalho]] de Seção:** Introduz uma seção específica dentro de uma página com um título (H2, H3, etc.) e, opcionalmente, uma breve descrição ou ações relacionadas à seção.
-   **[[Elementos/cabecalhos|Cabeçalho]] de [[Componentes/cards|Card]]:** Título de um [[Componentes/cards|card]], possivelmente com um avatar, [[Linguagem Visual/iconografia|ícone]] ou ações ([[Componentes/menu|menu]] kebab).
-   **[[Elementos/cabecalhos|Cabeçalho]] de [[Componentes/dialog|Modal]]/[[Componentes/dialog|Dialog]]:** Título do [[Componentes/dialog|modal]] e, frequentemente, um [[Elementos/botoes|botão]] de fechar.
-   **[[Elementos/cabecalhos|Cabeçalho]] de Tabela:** Pode incluir o título da tabela, controles de filtro ou busca, e ações em lote.

## Elementos Comuns

-   **Título:** O elemento principal, usando a tag de [[Elementos/cabecalhos|cabeçalho]] HTML apropriada (`<h1>` a `<h6>`).
-   **Subtítulo/Descrição (Opcional):** Texto adicional abaixo do título para fornecer mais contexto.
-   **[[Linguagem Visual/iconografia|Ícone]] ou Avatar (Opcional):** Associado ao título.
-   **Ações (Opcional):** [[Elementos/botoes|Botões]], [[Componentes/menu|menus]] [[Elementos/form_controls|dropdown]], ou [[Elementos/links|links]] relacionados ao conteúdo que o [[Elementos/cabecalhos|cabeçalho]] introduz (ex: "Adicionar Novo", "Editar", "Exportar").
-   **[[Componentes/breadcrumbs|Breadcrumbs]] (Opcional, para [[Elementos/cabecalhos|cabeçalhos]] de página):** Para mostrar a localização na hierarquia do site.
-   **[[Elementos/botoes|Botão]] de Fechar (Opcional, para [[Componentes/dialog|Modais]]/Drawers):** [[Linguagem Visual/iconografia|Ícone]] "X".

## Melhores Práticas

-   **Hierarquia Clara:** Usar níveis de cabeçalho HTML (`<h1>`-`<h6>`) corretamente para indicar a estrutura e importância do conteúdo.
    *   Geralmente, uma página deve ter apenas um `<h1>` (para o título principal da página).
-   **Concisão do Título:** O título deve ser breve e descritivo.
-   **Consistência Visual:** Manter um estilo consistente para [[Elementos/cabecalhos|cabeçalhos]] de mesmo nível hierárquico.
-   **[[Linguagem Visual/espacamento|Espaçamento]]:** Usar [[Linguagem Visual/espacamento|espaçamento]] adequado acima e abaixo do [[Elementos/cabecalhos|cabeçalho]] para separá-lo visualmente do conteúdo anterior e posterior.
-   **Acessibilidade (a11y):**
    *   Utilizar as tags de [[Elementos/cabecalhos|cabeçalho]] semânticas (`<h1>` a `<h6>`) corretamente. Não pular níveis de cabeçalho (ex: de `<h2>` para `<h4>`).
    *   Garantir que o texto do [[Elementos/cabecalhos|cabeçalho]] seja legível e tenha bom contraste.
    *   Se houver ações, elas devem ser acessíveis por teclado.
-   **Responsividade:** O tamanho da fonte e o layout dos elementos do [[Elementos/cabecalhos|cabeçalho]] (ex: ações) devem se ajustar a diferentes tamanhos de tela.

## Variações

-   **[[Elementos/cabecalhos|Cabeçalho]] Simples:** Apenas o título.
-   **[[Elementos/cabecalhos|Cabeçalho]] com Ações:** Título e [[Elementos/botoes|botões]]/[[Componentes/menu|menus]] à direita.
-   **[[Elementos/cabecalhos|Cabeçalho]] com [[Elementos/imagem|Imagem]] de Fundo/Banner (Page Hero Header):** Mais elaborado, geralmente para topos de página inicial ou páginas de destino.
-   **[[Elementos/cabecalhos|Cabeçalho]] Fixo/Sticky (para seções ou tabelas):** O [[Elementos/cabecalhos|cabeçalho]] permanece visível enquanto o usuário rola o conteúdo da seção/tabela.

## O Que Evitar

-   Usar tags de [[Elementos/cabecalhos|cabeçalho]] apenas para estilização de texto (sem considerar a semântica).
-   Títulos excessivamente longos ou truncados de forma inadequada.
-   [[Elementos/cabecalhos|Cabeçalhos]] que não se destacam suficientemente do resto do conteúdo.
-   Inconsistência nos níveis de [[Elementos/cabecalhos|cabeçalho]] ou no estilo visual. 