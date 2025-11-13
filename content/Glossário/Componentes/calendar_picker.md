# Calendar Picker (Seletor de Data)

O Calendar Picker é um componente de interface que permite aos usuários selecionar uma data ou um intervalo de datas de forma visual e intuitiva a partir de um calendário.

## Casos de Uso

-   Agendamento de compromissos, reservas.
-   Seleção de data de nascimento.
-   Definição de prazos ou períodos em tarefas e projetos.
-   Filtragem de dados por data ou período (ex: em relatórios, logs).
-   Reserva de voos, hotéis.

## Funcionalidades Essenciais

-   **Navegação entre Meses/Anos:** Permitir que o usuário avance e retroceda facilmente entre meses e anos.
-   **Seleção de Dia:** Indicação clara do dia selecionado.
-   **Dia Atual:** Destaque para o dia atual.
-   **Dias Desabilitados:** Capacidade de desabilitar datas passadas, futuras ou específicas (ex: fins de semana, feriados, datas indisponíveis).
-   **Seleção de Intervalo (Opcional):** Permitir a seleção de uma data de início e uma data de fim.
-   **Limpeza de Seleção:** Opção para limpar a data selecionada.
-   **Fechamento:** Mecanismo para fechar o seletor (ex: ao selecionar uma data, clicar fora).

## Melhores Práticas

-   **Entrada de Texto Associada:** Geralmente, um seletor de data está associado a um campo de input onde a data selecionada é exibida e, idealmente, também pode ser digitada.
-   **Formato de Data Claro:** Exibir a data selecionada em um formato consistente e compreensível (ex: DD/MM/AAAA).
-   **Feedback Visual:** Fornecer feedback claro sobre o hover, seleção e datas desabilitadas.
-   **Acessibilidade do Teclado:**
    *   Navegação pelos dias, meses e anos usando teclas de seta, Page Up/Down, Home/End.
    *   Seleção de data com Enter ou Espaço.
    *   Fechamento com Escape.
-   **Acessibilidade (a11y):**
    *   Usar roles e atributos ARIA apropriados (ex: `aria-label` para botões de navegação, `aria-selected` para o dia selecionado, `aria-disabled` para dias desabilitados).
    *   O calendário deve ser estruturado como uma tabela (`<table>`) com cabeçalhos (`<th>`) para os dias da semana para semântica correta.
    *   Garantir contraste adequado.
-   **Responsividade:** O calendário deve se adaptar bem a diferentes tamanhos de tela, possivelmente mudando para uma visualização otimizada em dispositivos móveis (ex: exibição de um mês por vez, rolagem vertical).
-   **Localização (i18n):** Suportar diferentes formatos de data, nomes de meses e dias da semana, e o primeiro dia da semana (domingo ou segunda-feira) conforme a localidade do usuário.

## Variações

-   **Seletor de Data Única.**
-   **Seletor de Intervalo de Datas (Date Range Picker).**
-   **Seletor de Data e Hora (Datetime Picker):** Combina a seleção de data com a seleção de hora.
-   **Visualização de Múltiplos Meses:** Exibir dois ou mais meses lado a lado para facilitar a seleção de intervalos que abrangem diferentes meses.
-   **Com Presets:** Oferecer opções de datas pré-definidas (ex: "Hoje", "Últimos 7 dias").

## Estrutura Comum

-   Cabeçalho com nome do mês/ano e botões de navegação (anterior/próximo).
-   Grid do calendário com dias da semana e os dias do mês.
-   (Opcional) Rodapé com botões de ação (ex: "Aplicar", "Cancelar", "Limpar").

## O Que Evitar

-   Interface de navegação de mês/ano confusa ou difícil.
-   Falta de indicação clara do dia atual ou selecionado.
-   Impedir a entrada manual da data no campo de input associado (a menos que haja uma forte razão para isso).
-   Não considerar a localização para formatos de data e linguagem. 