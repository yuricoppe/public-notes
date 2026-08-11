---
title: "Filters (Filtros)"
description: "Filtros são componentes de interface que permitem aos usuários refinar e reduzir um conjunto de dados (como uma lista de produtos, resultados de busca, itens em uma tabela) com…"
tags:
  - tema/ui
  - tipo/glossario
---

## Filters (Filtros)

Filtros são componentes de interface que permitem aos usuários refinar e reduzir um conjunto de dados (como uma [[Glossário/Elementos/listas|lista]] de produtos, resultados de busca, itens em uma tabela) com base em critérios específicos. Eles ajudam os usuários a encontrar o que procuram de forma mais rápida e eficiente.

## Casos de Uso

-   E-commerce: filtrar produtos por categoria, preço, marca, tamanho, [[Glossário/Linguagem Visual/cor|cor]], etc.
-   Resultados de Busca: refinar resultados por tipo de conteúdo, data, relevância.
-   [[Glossário/Componentes/data_tables|Tabelas de Dados]] e Listagens: filtrar por status, data, categoria ou qualquer outro atributo dos itens.
-   Dashboards: filtrar dados de gráficos e visualizações.
-   [[Glossário/Componentes/maps|Mapas]]: filtrar pontos de interesse.

## Tipos Comuns de Controles de Filtro

Filtros podem ser compostos por diversos elementos de UI:

-   **[[Glossário/Elementos/form_controls|Checkboxes]]:** Para selecionar múltiplas opções de um atributo (ex: filtrar por várias marcas).
-   **Radio [[Glossário/Elementos/botoes|Buttons]]:** Para selecionar uma única opção de um atributo (ex: filtrar por "Em estoque" ou "Fora de estoque", se forem mutuamente exclusivos).
-   **Dropdowns/Selects:** Para selecionar uma ou múltiplas opções de uma lista, especialmente útil quando há muitas opções.
-   **[[Glossário/Elementos/slider|Sliders]] (Deslizantes):** Para selecionar um intervalo de valores numéricos (ex: faixa de preço, avaliação).
-   **Campos de Texto/Busca:** Para filtrar por termos de pesquisa dentro de um atributo (ex: buscar nome do produto).
-   **Botões de [[Glossário/Elementos/interruptor|Toggle]]/Chips:** Para aplicar ou remover rapidamente filtros de categorias comuns.
-   **Seletores de Data/Período (Date Pickers):** Para filtrar por data ou intervalo de datas.
-   **Seletores de Cor (Color Swatches):** Para filtrar por cor.

## Layouts Comuns para Filtros

-   **Barra Lateral (Sidebar):** Filtros são exibidos em uma coluna lateral, comum em e-commerce e listagens complexas.
-   **Barra Horizontal (Toolbar):** Filtros são exibidos acima do conteúdo que está sendo filtrado, geralmente para um número menor de opções principais.
-   **[[Glossário/Componentes/dialog|Modal]]/Drawer:** Filtros são apresentados em um dialog ou drawer, especialmente em telas mobile para economizar espaço.
-   **Filtros Inline:** Opções de filtro diretamente incorporadas no conteúdo (ex: [[Glossário/Elementos/cabecalhos|cabeçalhos]] de tabela clicáveis que também filtram).

## Melhores Práticas

![Painel de filtros anotado: chips de filtros ativos com limpar tudo, contagem de resultados, contagem por opção e aviso de atualização para leitores de tela](attachments/glossario-anatomia-filtros.svg)

-   **Visibilidade e Acesso Fácil:** Os filtros devem ser fáceis de encontrar e usar.
-   **Feedback Imediato:** O conjunto de dados deve ser atualizado (ou mostrar um indicador de carregamento) assim que um filtro é aplicado ou alterado.
    *   Alguns sistemas usam um botão "Aplicar Filtros" para permitir múltiplas seleções antes de atualizar, especialmente se a atualização for custosa.
-   **Indicação de Filtros Ativos:** Mostrar claramente quais filtros estão aplicados no momento e oferecer uma maneira fácil de removê-los (individualmente ou todos de uma vez - "Limpar Filtros").
-   **Contagem de Resultados (Opcional):** Mostrar quantos itens correspondem aos filtros selecionados, idealmente atualizado dinamicamente.
-   **Relevância:** Mostrar primeiro os filtros mais importantes ou usados com frequência.
-   **Desempenho:** A aplicação de filtros deve ser rápida.
-   **Acessibilidade (a11y):**
    *   Todos os controles de filtro (checkboxes, selects, etc.) devem ser acessíveis por teclado e ter rótulos claros.
    *   Se os filtros estão em uma seção, ela deve ter um título apropriado (ex: `<h2>Filtros</h2>` ou `<fieldset><legend>Filtros</legend>...</fieldset>`).
    *   A atualização dos resultados deve ser comunicada a usuários de leitores de tela (ex: usando `aria-live` regions).
-   **Consistência:** Manter a aparência e o comportamento dos filtros consistentes.
-   **Evitar "Becos sem Saída":** Não permitir que o usuário selecione uma combinação de filtros que sempre resulte em zero resultados, se possível (ou, se acontecer, fornecer uma mensagem clara e sugestões).

## O Que Evitar

-   Excesso de opções de filtro que sobrecarregam o usuário.
-   Filtros escondidos ou difíceis de encontrar.
-   Falta de feedback sobre quais filtros estão ativos ou como limpá-los.
-   Atualização lenta dos resultados após aplicar um filtro.
-   Controles de filtro que não são adequados para o tipo de dado (ex: usar checkboxes para uma seleção única obrigatória).
