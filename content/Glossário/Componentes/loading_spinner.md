# Loading / Spinner (Indicador de Carregamento)

O componente Loading / Spinner (Indicador de Carregamento) é um elemento visual animado que informa ao usuário que uma ação está em progresso e que o sistema está trabalhando em segundo plano. Ele ajuda a gerenciar as expectativas do usuário durante períodos de espera.

## Casos de Uso

-   Carregamento inicial de uma página ou seção.
-   Submissão de [[Glossário/Padrões/form_structure|formulários]].
-   Busca de dados ou aplicação de [[Glossário/Componentes/filters|filtros]].
-   Carregamento de conteúdo assíncrono (ex: [[Glossário/Elementos/imagem|imagens]], dados em uma tabela).
-   Qualquer operação que leve um tempo perceptível para ser concluída (geralmente > 200-500ms).

## Tipos Comuns

1.  **Spinner (Animação Circular):** Um dos mais comuns. Um círculo ou conjunto de pontos que giram.
2.  **Progress Bar (Barra de Progresso):**
    *   **Indeterminada:** Uma barra que anima para frente e para trás ou com um padrão pulsante, indicando atividade sem mostrar o progresso exato.
    *   **Determinada:** Uma barra que preenche de 0% a 100% para mostrar o progresso de uma tarefa com duração conhecida (ex: upload de arquivo).
3.  **Skeleton Screens (Telas de Esqueleto):** Placeholders que imitam a estrutura do conteúdo que será carregado, dando uma percepção de carregamento mais rápido.
4.  **Animações Personalizadas:** Animações mais elaboradas ou que refletem a marca.
5.  **Texto Simples:** (ex: "Carregando...", "Processando..."). Pode acompanhar um spinner.

## Melhores Práticas

-   **Feedback Imediato (mas não muito cedo):** Para operações muito rápidas (<200ms), um spinner pode piscar e ser mais distrativo do que útil. Mostrar apenas se a espera for perceptível.
-   **Clareza:** O indicador deve ser claramente visível e compreensível como um sinal de que o sistema está ocupado.
-   **Não Intrusivo (quando apropriado):**
    *   Para carregamento de página inteira ou [[Glossário/Componentes/dialog|modal]], um overlay com spinner centralizado pode ser adequado.
    *   Para carregamento de pequenas seções ou [[Glossário/Elementos/botoes|botões]], um spinner menor e localizado próximo ao elemento é melhor.
-   **Consistência:** Usar o mesmo estilo de indicador de carregamento para operações semelhantes em todo o produto.
-   **Performance da Animação:** A animação do spinner em si deve ser suave e leve (CSS animations são preferíveis a GIFs pesados ou JavaScript complexo para animações simples).
-   **Acessibilidade (a11y):**
    *   Anunciar o início e o fim do carregamento para usuários de leitores de tela usando `aria-live` regions (ex: "Carregando conteúdo da tabela", "Tabela carregada").
    *   O spinner em si pode ter `role="status"` ou `role="progressbar"` (se for uma barra de progresso).
    *   Para progress bars determinadas, usar `aria-valuenow`, `aria-valuemin`, `aria-valuemax`.
    *   Garantir que a animação não seja a única forma de perceber que algo está carregando; o texto "Carregando..." é um bom complemento.
    *   Evitar animações que piscam em frequências que podem causar convulsões (WCAG).
-   **Contexto:** O indicador deve, se possível, estar próximo da área que está sendo carregada.
-   **Evitar Bloqueio Desnecessário:** Se apenas uma parte da interface está carregando, o resto deve permanecer interativo, se possível.

## Variações de Estilo

-   **Tamanho:** Spinners podem variar de pequenos (para [[Glossário/Elementos/botoes|botões]]) a grandes (para carregamento de página).
-   **[[Glossário/Linguagem Visual/cor|Cor]]:** Alinhada com a paleta da marca.
-   **Velocidade da Animação.**

## O Que Evitar

-   Indicadores de carregamento que não desaparecem após a conclusão da tarefa.
-   Spinners para operações instantâneas.
-   Animações de carregamento excessivamente complexas ou que consomem muitos recursos.
-   Falta de qualquer feedback durante esperas longas.
-   Indicadores de carregamento enganosos (ex: uma barra de progresso que para em 99% por muito tempo).
-   Bloquear a interface inteira por uma pequena operação em segundo plano. 