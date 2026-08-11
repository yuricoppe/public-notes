---
title: "Legend (Legenda de Gráficos/Mapas)"
description: "O componente Legend (Legenda) é usado para explicar o significado de símbolos, cores, padrões ou outros indicadores visuais utilizados em gráficos, mapas, diagramas ou outras…"
tags:
  - tema/ui
  - tipo/glossario
---

## Legend (Legenda de Gráficos/Mapas)

O componente Legend (Legenda) é usado para explicar o significado de símbolos, [[Glossário/Linguagem Visual/cor|cores]], padrões ou outros indicadores visuais utilizados em gráficos, [[Glossário/Componentes/maps|mapas]], diagramas ou outras visualizações de dados. Ele ajuda os usuários a interpretar corretamente a informação apresentada.

## Casos de Uso

-   **Gráficos:** (ex: gráficos de pizza, barra, linha) para identificar quais cores/padrões correspondem a quais séries de dados.
-   **Mapas:** Para explicar o significado de [[Glossário/Linguagem Visual/iconografia|ícones]], cores de regiões, ou tipos de rota.
-   **Diagramas e Fluxogramas:** Para definir o que cada forma ou cor de conector representa.
-   **Visualizações de Dados Complexas:** Qualquer interface onde elementos visuais são usados para codificar informação.

## Elementos Comuns

-   **Itens da Legenda:** Cada item na legenda geralmente consiste em:
    *   **Amostra Visual (Swatch/Key):** Uma pequena representação do símbolo, cor ou padrão usado na visualização (ex: um pequeno quadrado colorido, um trecho de linha estilizada, um ícone).
    *   **Rótulo (Label):** Texto descritivo que explica o que a amostra visual representa.
-   **Título da Legenda (Opcional):** Um título geral para a legenda se necessário (ex: "Tipos de Unidade", "Status do Projeto").
-   **Layout:** Os itens da legenda podem ser organizados verticalmente ([[Glossário/Elementos/listas|lista]]) ou horizontalmente.

## Melhores Práticas

![Legenda de gráfico: itens com amostra e rótulo, versão com rótulo direto na série e a alternativa com traço distinto para quem não distingue as cores](attachments/glossario-legenda-grafico.svg)

-   **Clareza e Precisão:** Os rótulos devem ser concisos e descrever com precisão o que cada amostra visual significa. A amostra visual deve corresponder exatamente ao que é usado na visualização principal.
-   **Proximidade:** A legenda deve estar posicionada próxima à visualização de dados que ela descreve, para fácil referência.
-   **Visibilidade:** Deve ser fácil de encontrar e ler. Evitar que a legenda sobreponha dados importantes na visualização.
-   **Consistência:** Usar o mesmo estilo e terminologia em todas as legendas semelhantes dentro de um produto.
-   **Interatividade (Opcional):**
    *   **Hover/Click para Destaque:** Em visualizações interativas, passar o mouse ou clicar em um item da legenda pode destacar as séries de dados correspondentes no gráfico/mapa (e vice-versa).
    *   **Filtragem:** Clicar em um item da legenda pode mostrar/ocultar a série de dados correspondente.
-   **Acessibilidade (a11y):**
    *   Garantir que haja contraste suficiente entre o texto dos rótulos e o fundo.
    *   Se as amostras visuais (cores, etc.) são a única forma de distinguir dados, fornecer alternativas textuais ou padrões para daltônicos ou em contextos onde as cores não são visíveis.
    *   Se a legenda for interativa, garantir que as interações sejam acessíveis por teclado.
    *   A legenda pode ser estruturada como uma lista (`<ul>` ou `<dl>`) para semântica.
-   **Não Sobrecarregar:** Se houver muitas séries de dados, a legenda pode se tornar muito longa. Considerar alternativas, como mostrar informações em tooltips diretamente na visualização ou agrupar categorias na legenda.

## Variações

-   **Legenda Estática:** Apenas exibe a informação.
-   **Legenda Interativa:** Permite interações como destaque ou filtragem.
-   **Legenda Integrada:** Incorporada diretamente na área do gráfico/mapa.
-   **Legenda Separada:** Posicionada ao lado ou abaixo da visualização.

## O Que Evitar

-   Rótulos ambíguos ou amostras visuais que não correspondem à visualização.
-   Posicionar a legenda muito longe da visualização, tornando difícil a referência.
-   Legendas muito longas ou desorganizadas.
-   Usar apenas cor para transmitir informação sem alternativas acessíveis.
-   Legendas interativas que não são intuitivas ou acessíveis.
