# Data Tables (Tabelas de Dados)

Data Tables são componentes usados para exibir conjuntos de dados estruturados em linhas e colunas, permitindo fácil visualização, comparação, e frequentemente, interação com os dados (como ordenação, filtragem e paginação).

## Casos de Uso

-   Listagem de usuários, produtos, pedidos, transações.
-   Relatórios financeiros ou analíticos.
-   Configurações de sistema que envolvem múltiplos itens.
-   Qualquer situação onde dados tabulares precisam ser apresentados de forma organizada.

## Funcionalidades Essenciais

-   **Cabeçalhos de Coluna (Headers):** Rótulos claros para cada coluna, indicando o tipo de dado que ela contém.
-   **Linhas de Dados (Rows):** Cada linha representa um item ou registro.
-   **Células (Cells):** Interseção de uma linha e uma coluna, contendo um valor de dado específico.
-   **Bordas (Opcional, mas Comum):** Linhas que separam colunas e/ou linhas para melhorar a legibilidade.
-   **Alinhamento de Texto:** Consistente dentro das colunas (ex: texto à esquerda, números à direita).

## Funcionalidades Avançadas (Comuns)

-   **Ordenação (Sorting):** Permitir que o usuário clique nos cabeçalhos das colunas para ordenar os dados em ordem ascendente ou descendente.
-   **Paginação (Pagination):** Dividir grandes conjuntos de dados em várias páginas para melhorar o desempenho e a usabilidade.
-   **Filtragem (Filtering):** Oferecer opções para filtrar os dados com base em critérios específicos (ex: busca por texto, seleção de status).
-   **Seleção de Linhas (Row Selection):** Permitir que o usuário selecione uma ou mais linhas para realizar ações em lote (ex: deletar, editar, exportar).
    *   Checkboxes para seleção múltipla.
-   **Ações por Linha (Row Actions):** Botões ou menus de contexto em cada linha para ações específicas daquele item (ex: Editar, Ver Detalhes, Excluir).
-   **Scroll Horizontal:** Para tabelas com muitas colunas que não cabem na largura da tela.
-   **Colunas Fixas (Fixed Columns):** Manter uma ou mais colunas visíveis durante a rolagem horizontal (ex: coluna de ID ou de ações).

## Melhores Práticas

-   **Legibilidade:** Usar tipografia clara, espaçamento adequado (padding nas células) e contraste suficiente.
-   **Escaneabilidade:** Facilitar a leitura rápida dos dados. Listras de zebra (alternar cor de fundo das linhas) podem ajudar.
-   **Responsividade:** Tabelas são notoriamente difíceis de tornar responsivas.
    *   **Abordagens Comuns:** Rolagem horizontal, colapsar colunas menos importantes em um menu "mais", transformar linhas em cards em telas pequenas, ou priorizar colunas.
-   **Performance:** Para tabelas muito grandes, considerar virtualização de linhas/colunas (renderizar apenas o que está visível) ou paginação do lado do servidor.
-   **Acessibilidade (a11y):**
    *   Usar a marcação HTML correta: `<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>` (com atributo `scope="col"` ou `scope="row"`), e `<td>`.
    *   Fornecer um `<caption>` para a tabela, descrevendo seu propósito.
    *   Garantir que todas as funcionalidades interativas (ordenação, paginação, filtros, seleções, ações) sejam acessíveis e operáveis por teclado.
    *   Indicar o estado de ordenação atual (ex: com um ícone e `aria-sort` no `<th>`).
-   **Clareza nos Cabeçalhos:** Devem ser concisos e descritivos.
-   **Consistência de Dados:** Formatar dados de forma consistente dentro de cada coluna (ex: datas, moedas).

## Variações

-   **Tabela Simples (Apenas Exibição).**
-   **Tabela Interativa (com ordenação, filtragem, paginação).**
-   **Tabela com Linhas Expansíveis:** Para mostrar detalhes adicionais de uma linha.
-   **Tabela com Edição Inline:** Permitir a edição de dados diretamente nas células.

## O Que Evitar

-   Tabelas excessivamente largas que exigem muita rolagem horizontal sem colunas fixas importantes.
-   Densidade de informação muito alta ou muito baixa.
-   Falta de feedback claro para ações como ordenação ou filtragem.
-   Design responsivo pobre que torna a tabela inutilizável em telas menores.
-   Não usar a semântica HTML correta, prejudicando a acessibilidade. 