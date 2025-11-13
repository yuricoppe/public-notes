---
title: "dialog"

---

## Dialog (Caixa de Diálogo ou Modal)

Dialogs (também conhecidos como Modals ou Pop-ups) são janelas ou overlays que aparecem sobre o conteúdo principal da página, exigindo a interação do usuário antes que ele possa retornar à interface principal. Eles são usados para apresentar informações importantes, solicitar confirmação, ou obter entrada do usuário para uma tarefa específica.

## Casos de Uso

-   **Confirmação de Ações Destrutivas:** (ex: "Você tem certeza que deseja excluir este item?").
-   **Alertas Importantes:** Para informações críticas que o usuário precisa ver.
-   **[[Glossário/Padrões/form_structure|Formulários]] Curtos:** (ex: [[Glossário/Padrões/authentication|login]], cadastro rápido, adicionar um item simples).
-   **Visualização de Conteúdo Detalhado:** (ex: visualizar uma [[Glossário/Elementos/imagem|imagem]] em tamanho maior, detalhes de um produto sem sair da listagem).
-   **Notificações que Exigem Ação.**
-   **Seletores ou Pickers Complexos:** (ex: um seletor de arquivos avançado).

## Tipos Comuns

1.  **Modal de Alerta (Alert Dialog):** Informa o usuário sobre uma situação e geralmente tem apenas um [[Glossário/Elementos/botoes|botão]] de "OK" ou "Fechar".
2.  **Modal de Confirmação (Confirm Dialog):** Pede ao usuário para confirmar uma ação. Geralmente tem dois [[Glossário/Elementos/botoes|botões]] (ex: "Sim/Não", "Confirmar/Cancelar").
3.  **Modal de Prompt/Entrada (Prompt Dialog):** Solicita uma entrada de dados do usuário através de um ou mais campos de [[Glossário/Padrões/form_structure|formulário]].
4.  **Modal Informativo/Passivo:** Apresenta informações sem necessariamente exigir uma ação além de fechar (ex: tour guiado, novidades).

## Elementos Essenciais

-   **Overlay de Fundo:** Escurece ou desfoca o conteúdo da página principal para dar foco ao dialog.
-   **Contêiner do Dialog:** A janela em si.
-   **Título (Recomendado):** Um texto claro que descreve o propósito do dialog.
-   **Conteúdo Principal:** A mensagem, [[Glossário/Padrões/form_structure|formulário]] ou informação a ser apresentada.
-   **[[Glossário/Elementos/botoes|Botões]] de Ação:** (ex: Confirmar, Cancelar, Salvar, Fechar).
-   **Mecanismo de Fechamento:**
    *   Um [[Glossário/Elementos/botoes|botão]] "Fechar" explícito (geralmente um "X" no canto superior direito).
    *   Ação de um dos [[Glossário/Elementos/botoes|botões]] principais (ex: "Cancelar" fecha o dialog).
    *   (Opcional) Clicar no overlay de fundo para fechar.
    *   (Opcional) Pressionar a tecla `Escape` para fechar.

## Melhores Práticas

-   **Uso Moderado:** Evitar o uso excessivo de dialogs, pois podem interromper o fluxo do usuário.
-   **Propósito Claro:** O usuário deve entender imediatamente por que o dialog apareceu e o que é esperado dele.
-   **Conteúdo Conciso:** Manter o conteúdo do dialog o mais breve e focado possível.
-   **Foco no Dialog:** Quando um dialog está aberto, o foco do teclado deve ser movido para dentro dele, e o conteúdo da página principal não deve ser interativo (efeito "armadilha de foco").
-   **Mecanismos de Fechamento Claros e Consistentes:** O usuário deve conseguir fechar o dialog facilmente.
-   **Acessibilidade (a11y):**
    *   Usar `role="dialog"` ou `role="alertdialog"` no contêiner do dialog.
    *   Usar `aria-modal="true"` para indicar que o conteúdo fora do dialog está inerte.
    *   Usar `aria-labelledby` para associar o título ao dialog e `aria-describedby` para associar o conteúdo principal (se aplicável).
    *   Gerenciar o foco: ao abrir, o foco vai para o primeiro elemento interativo no dialog; ao fechar, o foco retorna para o elemento que o abriu.
    *   Garantir que seja fechável com a tecla `Escape`.
-   **Responsividade:** Dialogs devem se adaptar a diferentes tamanhos de tela, evitando barras de rolagem desnecessárias dentro do dialog e garantindo que os [[Glossário/Elementos/botoes|botões]] de ação estejam sempre visíveis.
-   **Evitar Dialogs sobre Dialogs:** Geralmente é uma má prática de UX, pois pode confundir o usuário.

## O Que Evitar

-   Usar dialogs para informações não críticas que poderiam ser apresentadas inline.
-   Dialogs com muito conteúdo ou que exigem rolagem excessiva.
-   Impedir o fechamento do dialog sem uma razão muito forte (ex: erro crítico que precisa ser resolvido).
-   Múltiplos dialogs abertos ao mesmo tempo.
-   Abrir dialogs inesperadamente (ex: ao carregar a página, a menos que seja para algo crucial como consentimento de cookies ou um alerta crítico).
