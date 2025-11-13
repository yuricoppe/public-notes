---
title: "toast"

---

## Toast / Snackbar

Toasts (também conhecidos como Snackbars, especialmente no Material Design) são [[Glossário/Componentes/messaging|mensagens]] curtas e não intrusivas que fornecem feedback breve sobre uma operação. Eles geralmente aparecem temporariamente na tela (na parte inferior ou superior) e desaparecem sozinhos após alguns segundos, ou podem ser dispensados pelo usuário.

## Casos de Uso

-   Confirmar ações bem-sucedidas (ex: "Item adicionado ao carrinho", "[[Glossário/Padrões/settings|Configurações]] salvas", "E-mail enviado").
-   Fornecer feedback sobre operações em segundo plano (ex: "Baixando arquivo...").
-   Alertas de baixa prioridade ou informativos que não requerem interrupção do fluxo do usuário.
-   (Menos comum) Erros leves que não impedem o usuário de continuar.

## Elementos Comuns

-   **Contêiner do Toast:** A "caixa" da mensagem.
-   **Texto da Mensagem:** Curto e direto ao ponto.
-   **(Opcional) [[Glossário/Linguagem Visual/iconografia|Ícone]]:** Para indicar o tipo de mensagem (sucesso, informação, etc.), embora toasts sejam frequentemente apenas textuais.
-   **(Opcional) [[Glossário/Elementos/botoes|Botão]] de Ação:** Um [[Glossário/Elementos/links|link]] ou [[Glossário/Elementos/botoes|botão]] para uma ação contextual (ex: "Desfazer" após excluir um item, "Ver Detalhes").
-   **(Opcional) [[Glossário/Elementos/botoes|Botão]] Fechar/Dispensar ("X"):** Para permitir que o usuário feche o toast antes que ele desapareça automaticamente.

## Melhores Práticas

-   **Brevidade:** [[Glossário/Componentes/messaging|Mensagens]] devem ser muito curtas.
-   **Não Intrusivo:** Toasts não devem cobrir informações importantes ou exigir interação imediata para continuar usando a aplicação.
-   **Tempo de Exibição Adequado:** Deve permanecer na tela tempo suficiente para ser lido (geralmente entre 4 a 10 segundos), mas não tanto a ponto de se tornar irritante. O tempo pode variar com base na quantidade de texto.
-   **Posicionamento Consistente:** Escolher uma posição (ex: canto inferior esquerdo, canto inferior central, canto superior direito) e usá-la consistentemente.
-   **Empilhamento (Stacking):** Se múltiplos toasts puderem aparecer em rápida sucessão, eles devem empilhar de forma organizada (geralmente verticalmente) em vez de se sobreporem.
-   **Acessibilidade (a11y):**
    *   Anunciar toasts para usuários de leitores de tela usando `aria-live="polite"` (ou `aria-live="assertive"` se o feedback for crítico, embora toasts sejam geralmente para feedback menos crítico).
    *   O conteúdo do toast deve ter `role="status"` ou `role="alert"` dependendo da urgência.
    *   Se houver um [[Glossário/Elementos/botoes|botão]] de ação ou fechar, ele deve ser acessível por teclado.
    *   Garantir que o usuário tenha tempo suficiente para ler, ou fornecer um mecanismo para pausar/dispensar manualmente.
-   **Evitar para Erros Críticos:** Para erros que impedem o usuário de prosseguir ou que requerem ação imediata, um [[Glossário/Componentes/dialog|Dialog]] ou mensagem inline mais proeminente é geralmente mais apropriado.
-   **Ação Opcional Clara:** Se houver um [[Glossário/Elementos/botoes|botão]] de ação, ele deve ser óbvio e o texto deve ser claro sobre o que acontece.

## Variações

-   **Toast Simples (Apenas Texto).**
-   **Toast com Ação.**
-   **Toast com [[Glossário/Linguagem Visual/iconografia|Ícone]].**
-   **[[Glossário/Linguagem Visual/cor|Cores]] Semânticas (Sucesso, Erro, Aviso, Info):** Embora menos comuns em toasts do que em alertas inline, podem ser usados com moderação.

## O Que Evitar

-   Usar toasts para informações complexas ou que exigem muita leitura.
-   Toasts que desaparecem rápido demais.
-   Muitos toasts aparecendo ao mesmo tempo e poluindo a tela.
-   Toasts que cobrem elementos interativos importantes.
-   Usar toasts para erros críticos ou [[Glossário/Componentes/messaging|mensagens]] que exigem uma decisão do usuário (para isso, use [[Glossário/Componentes/dialog|Dialogs]]).
-   Falta de feedback via `aria-live` para usuários de leitores de tela.
