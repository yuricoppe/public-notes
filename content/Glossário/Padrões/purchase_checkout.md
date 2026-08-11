---
title: "purchase checkout"
description: "O padrão de compra/checkout descreve o processo pelo qual um usuário seleciona produtos ou serviços, fornece informações de pagamento e envio (se aplicável), revisa seu pedido…"
tags:
  - tema/ux
  - tipo/glossario
---

## Compra / Checkout (Purchase/Checkout)

## Descrição Geral

O padrão de compra/checkout descreve o processo pelo qual um usuário seleciona produtos ou serviços, fornece informações de pagamento e envio (se aplicável), revisa seu pedido e finaliza uma transação comercial. É uma das interações mais críticas em portais de e-commerce ou serviços pagos, onde a clareza, segurança e eficiência são primordiais para evitar o abandono do carrinho.

## Princípios Chave / Objetivos

- **Confiança e Segurança:** Assegurar ao usuário que suas informações de pagamento e dados pessoais estão seguros.
- **Clareza e Transparência:** Apresentar todas as informações relevantes de forma clara (produtos, preços, taxas, impostos, prazos de entrega).
- **Eficiência e Simplicidade:** Minimizar o número de etapas e a quantidade de informação solicitada, tornando o processo rápido e fácil.
- **Prevenção de Erros:** Ajudar o usuário a evitar erros, especialmente no preenchimento de informações de pagamento e endereço.
- **Flexibilidade:** Oferecer múltiplas opções de pagamento e, se aplicável, de envio.
- **Confirmação:** Fornecer feedback claro de que o pedido foi concluído com sucesso.

## Elementos Comuns / Estrutura Típica

![Estrutura de um checkout: indicador de progresso em cinco etapas, formulário de pagamento à esquerda e resumo do pedido com o total sempre visível à direita](attachments/glossario-checkout-etapas.svg)

- **Revisão do Carrinho/Pedido:** [[Glossário/Elementos/listas|Lista]] detalhada dos itens, quantidades, preços unitários e subtotais.
- **Informações de Envio (se aplicável):**
    - Campos para endereço de entrega.
    - Opções de métodos de envio com custos e prazos estimados.
- **Informações de Pagamento:**
    - Seleção do método de pagamento (cartão de crédito, boleto, PayPal, etc.).
    - Campos para detalhes do cartão (número, validade, CVV).
    - Opções para salvar informações de pagamento para compras futuras (com consentimento).
- **Resumo do Pedido:** Custo total, incluindo impostos, taxas e frete.
- **Campo para [[Glossário/Elementos/codigo|Código]] Promocional/Cupom.**
- **[[Glossário/Elementos/botoes|Botão]] de Ação Primário:** (ex: "Finalizar Compra", "Pagar Agora").
- **[[Glossário/Elementos/links|Links]] para Políticas:** (Política de Devolução, Termos de Serviço, Privacidade).
- **Indicador de Progresso:** (especialmente para checkouts multi-etapas).
- **Informações de Contato do Cliente.**

## Comportamento e Interação

1. O usuário adiciona itens ao carrinho e prossegue para o checkout.
2. O sistema guia o usuário através das etapas (ex: informações pessoais/envio, detalhes do pagamento, revisão).
3. O usuário preenche os [[Glossário/Padrões/form_structure|formulários]] necessários.
4. Validação em tempo real ajuda a corrigir erros de entrada.
5. O sistema calcula totais, impostos e frete dinamicamente.
6. O usuário revisa todas as informações antes de submeter.
7. Ao clicar em "Finalizar Compra", o sistema processa o pagamento.
8.  - **Sucesso:** Uma página de confirmação do pedido é exibida com detalhes da compra e próximos passos (ex: email de confirmação será enviado). O usuário pode ser redirecionado para uma página de "Obrigado".
    - **Falha no Pagamento:** Uma mensagem de erro clara é exibida, permitindo ao usuário tentar novamente ou usar outro método de pagamento.

## Diretrizes de Uso e Boas Práticas

### Faça

- Mantenha o processo o mais curto e linear possível. Idealmente, um checkout de página única ou poucas etapas bem definidas.
- Indique claramente o progresso através das etapas do checkout.
- Mostre um resumo do pedido sempre visível ou facilmente acessível.
- Permita checkout como convidado (sem necessidade de criar conta), se possível.
- Valide endereços e dados de cartão em tempo real para reduzir erros.
- Exiba selos de segurança e confiança para tranquilizar o usuário.
- Forneça estimativas claras de entrega e custos de frete antes da etapa final de pagamento.
- Envie um email de confirmação detalhado imediatamente após a compra.
- Otimize para dispositivos móveis (formulários fáceis de preencher, botões grandes).

### Não Faça

- Não surpreenda o usuário com custos inesperados no final do processo.
- Não exija [[Glossário/Padrões/create_account|registro]] obrigatório para comprar, se puder evitar.
- Não peça informações redundantes ou desnecessárias.
- Não torne difícil a edição de itens no carrinho durante o checkout.
- Não use um design confuso ou desorganizado.
- Não redirecione para fora do site para pagamento sem um aviso claro (exceto para provedores de pagamento conhecidos como PayPal).

## Considerações de Acessibilidade

- Todos os campos de formulário devem ter rótulos claros e associados (`<label for>`).
- Mensagens de erro e sucesso devem ser acessíveis e associadas aos campos relevantes.
- Garanta que todos os elementos interativos sejam operáveis via teclado.
- Mantenha bom contraste de [[Glossário/Linguagem Visual/cor|cores]].
- O resumo do pedido e todas as informações financeiras devem ser apresentadas de forma clara e compreensível por leitores de tela.
- Se usar um indicador de progresso, garanta que ele seja acessível.

## Exemplos / Cenários de Uso

- Compra de produtos físicos em uma loja virtual.
- Assinatura de um serviço online (SaaS, streaming).
- Pagamento de uma fatura ou taxa em um portal de serviços.
- Compra de ingressos para eventos.

## Variações Comuns

- **Checkout de Página Única (One-Page Checkout):** Todos os campos e informações em uma única página, geralmente usando seções expansíveis (accordions).
- **Checkout Multi-Etapas (Multi-Step Checkout):** Processo dividido em várias páginas ou abas (ex: 1. Informações Pessoais, 2. Envio, 3. Pagamento, 4. Revisão).
- **Checkout Expresso/Rápido:** Para usuários com contas e informações salvas, permitindo finalizar a compra com poucos cliques.
- **Checkout Incorporado (Embedded Checkout):** Componentes de pagamento de terceiros (ex: Stripe Elements, PayPal buttons) integrados diretamente na página.

## Status

A definir

## Recursos Adicionais / Figma

- [Link para os designs das telas de carrinho e checkout no Figma]
- [Link para protótipos do fluxo de compra]
- [Link para a documentação da API de pagamento, se aplicável]
