---
title: "Header (Cabeçalho de Página/Seção)"
description: "O componente Header (Cabeçalho), neste contexto, refere-se a uma área no topo de uma página, seção ou componente (como um Card ou Modal) que introduz o conteúdo subsequente."
tags:
  - tema/ui
  - tipo/glossario
---

## Header (Cabeçalho de Página/Seção)

O componente Header ([[Glossário/Elementos/cabecalhos|Cabeçalho]]), neste contexto, refere-se a uma área no topo de uma página, seção ou componente (como um [[Glossário/Componentes/cards|Card]] ou [[Glossário/Componentes/dialog|Modal]]) que introduz o conteúdo subsequente. Ele é distinto do "Global Header/Navbar" (cabeçalho de navegação principal do site).

## Casos de Uso

-   **Cabeçalho de Página:** Contém o título principal da página (H1), possivelmente um subtítulo ou [[Glossário/Componentes/breadcrumbs|breadcrumbs]].
-   **Cabeçalho de Seção:** Introduz uma seção específica dentro de uma página com um título (H2, H3, etc.) e, opcionalmente, uma breve descrição ou ações relacionadas à seção.
-   **Cabeçalho de Card:** Título de um card, possivelmente com um avatar, [[Glossário/Linguagem Visual/iconografia|ícone]] ou ações ([[Glossário/Componentes/menu|menu]] kebab).
-   **Cabeçalho de Modal/Dialog:** Título do modal e, frequentemente, um [[Glossário/Elementos/botoes|botão]] de fechar.
-   **Cabeçalho de Tabela:** Pode incluir o título da tabela, controles de filtro ou busca, e ações em lote.

## Elementos Comuns

![Cabeçalho de página anotado com breadcrumb, título h1, subtítulo e ações; ao lado, a escada de níveis h1, h2 e h3 e o erro de pular de h2 para h4](attachments/glossario-cabecalho-de-pagina.svg)

-   **Título:** O elemento principal, usando a tag de cabeçalho HTML apropriada (`<h1>` a `<h6>`).
-   **Subtítulo/Descrição (Opcional):** Texto adicional abaixo do título para fornecer mais contexto.
-   **Ícone ou Avatar (Opcional):** Associado ao título.
-   **Ações (Opcional):** Botões, menus [[Glossário/Elementos/form_controls|dropdown]], ou [[Glossário/Elementos/links|links]] relacionados ao conteúdo que o cabeçalho introduz (ex: "Adicionar Novo", "Editar", "Exportar").
-   **Breadcrumbs (Opcional, para cabeçalhos de página):** Para mostrar a localização na hierarquia do site.
-   **Botão de Fechar (Opcional, para Modais/Drawers):** Ícone "X".

## Melhores Práticas

-   **Hierarquia Clara:** Usar níveis de cabeçalho HTML (`<h1>`-`<h6>`) corretamente para indicar a estrutura e importância do conteúdo.
    *   Geralmente, uma página deve ter apenas um `<h1>` (para o título principal da página).
-   **Concisão do Título:** O título deve ser breve e descritivo.
-   **Consistência Visual:** Manter um estilo consistente para cabeçalhos de mesmo nível hierárquico.
-   **[[Glossário/Linguagem Visual/espacamento|Espaçamento]]:** Usar espaçamento adequado acima e abaixo do cabeçalho para separá-lo visualmente do conteúdo anterior e posterior.
-   **Acessibilidade (a11y):**
    *   Utilizar as tags de cabeçalho semânticas (`<h1>` a `<h6>`) corretamente. Não pular níveis de cabeçalho (ex: de `<h2>` para `<h4>`).
    *   Garantir que o texto do cabeçalho seja legível e tenha bom contraste.
    *   Se houver ações, elas devem ser acessíveis por teclado.
-   **Responsividade:** O tamanho da fonte e o layout dos elementos do cabeçalho (ex: ações) devem se ajustar a diferentes tamanhos de tela.

## Variações

-   **Cabeçalho Simples:** Apenas o título.
-   **Cabeçalho com Ações:** Título e botões/menus à direita.
-   **Cabeçalho com [[Glossário/Elementos/imagem|Imagem]] de Fundo/Banner (Page Hero Header):** Mais elaborado, geralmente para topos de página inicial ou páginas de destino.
-   **Cabeçalho Fixo/Sticky (para seções ou tabelas):** O cabeçalho permanece visível enquanto o usuário rola o conteúdo da seção/tabela.

## O Que Evitar

-   Usar tags de cabeçalho apenas para estilização de texto (sem considerar a semântica).
-   Títulos excessivamente longos ou truncados de forma inadequada.
-   Cabeçalhos que não se destacam suficientemente do resto do conteúdo.
-   Inconsistência nos níveis de cabeçalho ou no estilo visual.
