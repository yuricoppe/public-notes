---
title: "header"

---

## Header ([[Glossário/Elementos/cabecalhos|Cabeçalho]] de Página/Seção)

O componente Header ([[Glossário/Elementos/cabecalhos|Cabeçalho]]), neste contexto, refere-se a uma área no topo de uma página, seção ou componente (como um [[Glossário/Componentes/cards|Card]] ou [[Glossário/Componentes/dialog|Modal]]) que introduz o conteúdo subsequente. Ele é distinto do "Global Header/Navbar" ([[Glossário/Elementos/cabecalhos|cabeçalho]] de navegação principal do site).

## Casos de Uso

-   **[[Glossário/Elementos/cabecalhos|Cabeçalho]] de Página:** Contém o título principal da página (H1), possivelmente um subtítulo ou [[Glossário/Componentes/breadcrumbs|breadcrumbs]].
-   **[[Glossário/Elementos/cabecalhos|Cabeçalho]] de Seção:** Introduz uma seção específica dentro de uma página com um título (H2, H3, etc.) e, opcionalmente, uma breve descrição ou ações relacionadas à seção.
-   **[[Glossário/Elementos/cabecalhos|Cabeçalho]] de [[Glossário/Componentes/cards|Card]]:** Título de um [[Glossário/Componentes/cards|card]], possivelmente com um avatar, [[Glossário/Linguagem Visual/iconografia|ícone]] ou ações ([[Glossário/Componentes/menu|menu]] kebab).
-   **[[Glossário/Elementos/cabecalhos|Cabeçalho]] de [[Glossário/Componentes/dialog|Modal]]/[[Glossário/Componentes/dialog|Dialog]]:** Título do [[Glossário/Componentes/dialog|modal]] e, frequentemente, um [[Glossário/Elementos/botoes|botão]] de fechar.
-   **[[Glossário/Elementos/cabecalhos|Cabeçalho]] de Tabela:** Pode incluir o título da tabela, controles de filtro ou busca, e ações em lote.

## Elementos Comuns

-   **Título:** O elemento principal, usando a tag de [[Glossário/Elementos/cabecalhos|cabeçalho]] HTML apropriada (`<h1>` a `<h6>`).
-   **Subtítulo/Descrição (Opcional):** Texto adicional abaixo do título para fornecer mais contexto.
-   **[[Glossário/Linguagem Visual/iconografia|Ícone]] ou Avatar (Opcional):** Associado ao título.
-   **Ações (Opcional):** [[Glossário/Elementos/botoes|Botões]], [[Glossário/Componentes/menu|menus]] [[Glossário/Elementos/form_controls|dropdown]], ou [[Glossário/Elementos/links|links]] relacionados ao conteúdo que o [[Glossário/Elementos/cabecalhos|cabeçalho]] introduz (ex: "Adicionar Novo", "Editar", "Exportar").
-   **[[Glossário/Componentes/breadcrumbs|Breadcrumbs]] (Opcional, para [[Glossário/Elementos/cabecalhos|cabeçalhos]] de página):** Para mostrar a localização na hierarquia do site.
-   **[[Glossário/Elementos/botoes|Botão]] de Fechar (Opcional, para [[Glossário/Componentes/dialog|Modais]]/Drawers):** [[Glossário/Linguagem Visual/iconografia|Ícone]] "X".

## Melhores Práticas

-   **Hierarquia Clara:** Usar níveis de cabeçalho HTML (`<h1>`-`<h6>`) corretamente para indicar a estrutura e importância do conteúdo.
    *   Geralmente, uma página deve ter apenas um `<h1>` (para o título principal da página).
-   **Concisão do Título:** O título deve ser breve e descritivo.
-   **Consistência Visual:** Manter um estilo consistente para [[Glossário/Elementos/cabecalhos|cabeçalhos]] de mesmo nível hierárquico.
-   **[[Glossário/Linguagem Visual/espacamento|Espaçamento]]:** Usar [[Glossário/Linguagem Visual/espacamento|espaçamento]] adequado acima e abaixo do [[Glossário/Elementos/cabecalhos|cabeçalho]] para separá-lo visualmente do conteúdo anterior e posterior.
-   **Acessibilidade (a11y):**
    *   Utilizar as tags de [[Glossário/Elementos/cabecalhos|cabeçalho]] semânticas (`<h1>` a `<h6>`) corretamente. Não pular níveis de cabeçalho (ex: de `<h2>` para `<h4>`).
    *   Garantir que o texto do [[Glossário/Elementos/cabecalhos|cabeçalho]] seja legível e tenha bom contraste.
    *   Se houver ações, elas devem ser acessíveis por teclado.
-   **Responsividade:** O tamanho da fonte e o layout dos elementos do [[Glossário/Elementos/cabecalhos|cabeçalho]] (ex: ações) devem se ajustar a diferentes tamanhos de tela.

## Variações

-   **[[Glossário/Elementos/cabecalhos|Cabeçalho]] Simples:** Apenas o título.
-   **[[Glossário/Elementos/cabecalhos|Cabeçalho]] com Ações:** Título e [[Glossário/Elementos/botoes|botões]]/[[Glossário/Componentes/menu|menus]] à direita.
-   **[[Glossário/Elementos/cabecalhos|Cabeçalho]] com [[Glossário/Elementos/imagem|Imagem]] de Fundo/Banner (Page Hero Header):** Mais elaborado, geralmente para topos de página inicial ou páginas de destino.
-   **[[Glossário/Elementos/cabecalhos|Cabeçalho]] Fixo/Sticky (para seções ou tabelas):** O [[Glossário/Elementos/cabecalhos|cabeçalho]] permanece visível enquanto o usuário rola o conteúdo da seção/tabela.

## O Que Evitar

-   Usar tags de [[Glossário/Elementos/cabecalhos|cabeçalho]] apenas para estilização de texto (sem considerar a semântica).
-   Títulos excessivamente longos ou truncados de forma inadequada.
-   [[Glossário/Elementos/cabecalhos|Cabeçalhos]] que não se destacam suficientemente do resto do conteúdo.
-   Inconsistência nos níveis de [[Glossário/Elementos/cabecalhos|cabeçalho]] ou no estilo visual.
