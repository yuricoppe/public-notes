---
title: "inline error"

---

## Inline Error (Erro Inline)

O componente Inline Error (Erro Inline) é uma mensagem de erro exibida diretamente próxima ao elemento de interface que causou o erro, como um campo de [[Glossário/Padrões/form_structure|formulário]] inválido. Ele fornece feedback contextual e imediato para ajudar o usuário a identificar e corrigir o problema.

## Casos de Uso

-   **Validação de Campos de [[Glossário/Padrões/form_structure|Formulário]]:** Exibir uma mensagem abaixo ou ao lado de um campo de input quando os dados inseridos são inválidos (ex: "E-mail inválido", "Este campo é obrigatório", "A senha deve ter no mínimo 8 caracteres").
-   **Erro em uma Ação Específica:** Informar um problema com uma configuração ou pequena interação que não afeta a página inteira (ex: falha ao salvar uma preferência específica em uma [[Glossário/Elementos/listas|lista]] de [[Glossário/Padrões/settings|configurações]]).
-   **Conflitos de Dados:** Indicar um problema com um valor específico em uma tabela ou [[Glossário/Elementos/listas|lista]] (ex: "Nome de usuário já existe").

## Elementos Comuns

-   **Texto da Mensagem de Erro:** Claro, conciso e específico sobre qual é o problema e, idealmente, como corrigi-lo.
-   **(Opcional) [[Glossário/Linguagem Visual/iconografia|Ícone]] de Erro:** Um pequeno [[Glossário/Linguagem Visual/iconografia|ícone]] (ex: "X", triângulo de aviso) para reforçar visualmente que é uma mensagem de erro.
-   **Posicionamento:** Diretamente abaixo ou ao lado do campo ou elemento ao qual se refere.
-   **Estilo Visual:** [[Glossário/Linguagem Visual/cor|Cor]] de texto distintiva (geralmente vermelho) e, às vezes, uma [[Glossário/Linguagem Visual/cor|cor]] de fundo sutil para destacar a mensagem.

## Melhores Práticas

-   **Imediaticidade e Contexto:** A mensagem de erro deve aparecer assim que a validação falha (ex: ao sair do campo - on blur, ou na tentativa de submissão do [[Glossário/Padrões/form_structure|formulário]]) e estar claramente associada ao campo problemático.
-   **Clareza e Ação:** A mensagem deve ser fácil de entender. Evitar jargões técnicos. Se possível, sugerir como corrigir o erro.
    *   Ruim: "Erro de validação 2a-4f"
    *   Bom: "Por favor, insira um número de telefone válido (ex: (XX) XXXXX-XXXX)."
-   **Visibilidade:** A [[Glossário/Linguagem Visual/cor|cor]] do erro (geralmente vermelha) ajuda na identificação, mas não deve ser a única indicação (para acessibilidade). O texto em si e, opcionalmente, um [[Glossário/Linguagem Visual/iconografia|ícone]] são importantes.
-   **Acessibilidade (a11y):**
    *   Associar a mensagem de erro ao campo de input correspondente usando `aria-describedby`. O campo de input teria `aria-invalid="true"` quando em estado de erro.
        ```html
        <label for="email">E-mail:</label>
        <input type="email" id="email" name="email" aria-invalid="true" aria-describedby="email-error">
        <div id="email-error" role="alert" class="inline-error-message">
          Por favor, insira um endereço de e-mail válido.
        </div>
        ```
    *   A mensagem de erro em si pode ter `role="alert"` se a validação ocorrer dinamicamente e precisar ser anunciada assertivamente por leitores de tela. Se os erros são mostrados após a submissão, um `role="status"` ou simplesmente a associação com `aria-describedby` pode ser suficiente, e o foco pode ser movido para o primeiro campo com erro.
    *   Garantir contraste suficiente para o texto do erro.
-   **Não Intrusivo Demais:** Embora precise ser notado, não deve quebrar o layout da página de forma desajeitada.
-   **Remoção do Erro:** A mensagem de erro deve desaparecer ou ser atualizada assim que o usuário corrigir o problema e o campo se tornar válido.
-   **Consistência:** Usar um estilo e posicionamento consistentes para todas as [[Glossário/Componentes/messaging|mensagens]] de erro inline.

## O Que Evitar

-   [[Glossário/Componentes/messaging|Mensagens]] de erro genéricas que não ajudam o usuário (ex: "Campo inválido").
-   Mostrar erros apenas na submissão do [[Glossário/Padrões/form_structure|formulário]], sem feedback durante o preenchimento (validação inline é geralmente preferível para uma melhor UX).
-   Posicionar a mensagem de erro longe do campo correspondente.
-   Usar apenas [[Glossário/Linguagem Visual/cor|cor]] para indicar o erro.
-   [[Glossário/Componentes/messaging|Mensagens]] de erro que culpam o usuário (ex: "Você digitou errado"). Manter um tom neutro e útil.
-   Não limpar as [[Glossário/Componentes/messaging|mensagens]] de erro quando o problema for corrigido.
