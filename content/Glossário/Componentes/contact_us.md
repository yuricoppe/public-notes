---
title: "contact us"

---

## Contact Us (Fale Conosco)

O componente ou seção "Contact Us" (Fale Conosco) fornece aos usuários os meios para entrar em contato com a organização ou equipe de suporte. Pode variar de um simples [[Glossário/Elementos/links|link]] para uma página de contato a um [[Glossário/Padrões/form_structure|formulário]] de contato integrado.

## Casos de Uso

-   Páginas de "Contato" ou "Suporte".
-   Rodapés de sites para acesso rápido a informações de contato.
-   Dentro de seções de ajuda ou FAQs.
-   Como um CTA (Call to Action) para obter mais informações ou solicitar um serviço.

## Elementos Comuns

Dependendo da complexidade, pode incluir:

1.  **[[Glossário/Padrões/form_structure|Formulário]] de Contato:**
    *   Campo para Nome.
    *   Campo para E-mail.
    *   Campo para Assunto (opcional).
    *   Campo de Mensagem (textarea).
    *   (Opcional) Campo para Telefone.
    *   (Opcional) [[Glossário/Elementos/form_controls|Dropdown]] para tipo de consulta (ex: Vendas, Suporte, Imprensa).
    *   (Opcional) [[Glossário/Elementos/form_controls|Checkbox]] de consentimento para política de privacidade/termos.
    *   [[Glossário/Elementos/botoes|Botão]] de Enviar.

2.  **Informações de Contato Direto:**
    *   Endereço de e-mail clicável.
    *   Número de telefone clicável (`tel:` link).
    *   Endereço físico (com [[Glossário/Elementos/links|link]] para mapa, se aplicável).
    *   Horário de atendimento.

3.  **[[Glossário/Elementos/links|Links]] para Redes Sociais.**

4.  **[[Glossário/Elementos/links|Links]] para FAQs ou Base de Conhecimento.**

## Melhores Práticas

-   **Clareza de Propósito:** Deixar claro qual o objetivo do contato (suporte, vendas, etc.) e para onde a mensagem será direcionada.
-   **Simplicidade do [[Glossário/Padrões/form_structure|Formulário]]:** Pedir apenas as informações estritamente necessárias.
-   **Feedback de Submissão:** Após o envio do [[Glossário/Padrões/form_structure|formulário]], fornecer uma mensagem clara de confirmação (ex: "Sua mensagem foi enviada com sucesso! Entraremos em contato em breve.") ou de erro.
-   **Validação de Campos:** Validar os campos do [[Glossário/Padrões/form_structure|formulário]] (ex: formato de e-mail, campos obrigatórios) e fornecer [[Glossário/Componentes/messaging|mensagens]] de erro úteis.
-   **Acessibilidade (a11y):**
    *   Todos os campos do [[Glossário/Padrões/form_structure|formulário]] devem ter labels (`<label>`) associadas corretamente.
    *   Usar `<fieldset>` e `<legend>` se houver grupos de campos relacionados.
    *   Garantir que os [[Glossário/Elementos/botoes|botões]] sejam acessíveis e operáveis por teclado.
    *   [[Glossário/Componentes/messaging|Mensagens]] de erro e sucesso devem ser anunciadas por leitores de tela (ex: usando `aria-live`).
-   **Múltiplos Canais (se aplicável):** Oferecer diferentes formas de contato se disponíveis ([[Glossário/Padrões/form_structure|formulário]], e-mail, telefone, chat).
-   **Responsividade:** O [[Glossário/Padrões/form_structure|formulário]] e as informações de contato devem ser facilmente utilizáveis em todos os dispositivos.
-   **Proteção contra Spam:** Usar técnicas como CAPTCHA (com moderação, priorizando opções acessíveis como reCAPTCHA v3) ou honeypots para [[Glossário/Padrões/form_structure|formulários]].

## Variações

-   **Widget Flutuante:** Um [[Glossário/Elementos/botoes|botão]] "Fale Conosco" ou "Ajuda" que abre um [[Glossário/Padrões/form_structure|formulário]] ou opções de contato em um [[Glossário/Componentes/dialog|modal]]/pop-up.
-   **[[Glossário/Padrões/form_structure|Formulário]] Multi-Etapas:** Para coletas de informação mais complexas.
-   **Integração com Chatbots:** Oferecer uma opção de chatbot antes de encaminhar para um [[Glossário/Padrões/form_structure|formulário]] ou agente humano.

## O Que Evitar

-   [[Glossário/Padrões/form_structure|Formulários]] excessivamente longos ou com perguntas desnecessárias.
-   Falta de confirmação após o envio.
-   [[Glossário/Elementos/links|Links]] de e-mail ou telefone que não funcionam.
-   Esconder as informações de contato ou dificultar o processo.
-   Não responder aos contatos recebidos de forma oportuna.
