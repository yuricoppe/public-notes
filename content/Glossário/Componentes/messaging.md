---
title: "Messaging (Sistemas de Mensagens)"
description: "O componente de Messaging (Sistemas de Mensagens) refere-se a diversos elementos de UI usados para comunicar informações importantes, feedback, alertas ou status ao usuário."
tags:
  - tema/ui
  - tipo/glossario
---

## Messaging (Sistemas de Mensagens)

O componente de Messaging (Sistemas de Mensagens) refere-se a diversos elementos de UI usados para comunicar informações importantes, feedback, alertas ou status ao usuário. Isso pode variar de mensagens inline discretas a notificações mais proeminentes.

Este é um conceito guarda-chuva. Componentes específicos como `Toast/Snackbar`, `Alerts Inline`, e `Global Banners` são tipos de Messaging.

> Esta página é a definição de glossário. O tratamento longo do assunto — como decidir o que merece interromper alguém, permissão, frequência, escrita e acessibilidade — está em **[[Notificações/index|Notificações]]**.

## Casos de Uso Comuns

-   **Feedback de Ação:** Informar se uma operação foi bem-sucedida (ex: "Item salvo com sucesso!") ou falhou (ex: "Erro ao enviar [[Glossário/Padrões/form_structure|formulário]].").
-   **Alertas e Avisos:** Chamar a atenção para informações importantes ou condições que requerem ação (ex: "Sua sessão irá expirar em 5 minutos.", "Você tem itens não salvos.").
-   **Informações Contextuais:** Fornecer dicas ou informações relevantes para a tarefa atual.
-   **Validação de Formulário:** Exibir erros de validação próximos aos campos correspondentes.
-   **Notificações do Sistema:** Atualizações, novos recursos, manutenções programadas.

## Tipos Comuns de Componentes de Mensagens

![Os quatro tipos de mensagem ordenados por quanto interrompem — alerta inline, toast, banner global e modal — cada um com uma amostra desenhada e a regra de quando usar](attachments/glossario-tipos-de-mensagem.svg)

1.  **Alerts/Notificações Inline (Inline Alerts/Notifications):**
    *   Mensagens que aparecem dentro do fluxo da página, geralmente associadas a uma seção ou formulário específico.
    *   Podem ser persistentes até que o usuário as dispense (se houver um [[Glossário/Elementos/botoes|botão]] de fechar) ou a condição mude.
    *   Comumente usadas para feedback de formulários, erros de validação, ou informações contextuais.
    *   [[Glossário/Linguagem Visual/cor|Cores]] semânticas (sucesso, erro, aviso, informação) são frequentemente usadas.

2.  **[[Glossário/Componentes/toast|Toasts]]/[[Glossário/Componentes/toast|Snackbars]]:**
    *   Mensagens curtas e temporárias que aparecem (geralmente na parte inferior ou superior da tela) para fornecer feedback breve sobre uma ação. Elas desaparecem automaticamente após alguns segundos ou podem ser dispensadas pelo usuário.
    *   Menos intrusivas que [[Glossário/Componentes/dialog|dialogs]].
    *   Ver documentação específica de `toast.md`.

3.  **Banners Globais/Notificações de Site (Global Banners/Site Notifications):**
    *   Mensagens importantes que são exibidas em um local proeminente (ex: topo da página) e podem ser persistentes em várias páginas.
    *   Usadas para anúncios importantes, alertas de manutenção, ou promoções.

4.  **Dialogs de Alerta/Confirmação (Alert/Confirm Dialogs):**
    *   Modais que interrompem o fluxo para garantir que o usuário veja uma mensagem crítica ou confirme uma ação.
    *   Usar com moderação. Ver documentação de `dialog.md`.

5.  **Badges/Indicadores com Contagem (em Notificações):**
    *   Pequenos indicadores em [[Glossário/Linguagem Visual/iconografia|ícones]] de sino ou e-mail mostrando o número de novas notificações não lidas.

## Melhores Práticas

-   **Clareza e Concisão:** A mensagem deve ser fácil de entender e ir direto ao ponto.
-   **Relevância e Contexto:** A mensagem deve ser relevante para a tarefa atual do usuário ou para o estado do sistema.
-   **Nível de Urgência Apropriado:** Usar o tipo de mensagem correto para o nível de importância e urgência.
    *   Não usar um dialog modal para uma simples mensagem de sucesso que um toast resolveria.
-   **Cores Semânticas Consistentes:** Usar cores padrão para indicar sucesso (verde), erro (vermelho), aviso (amarelo/laranja), informação (azul).
-   **Acessibilidade (a11y):**
    *   Mensagens dinâmicas (especialmente erros, alertas e toasts) devem ser anunciadas por leitores de tela usando `aria-live` regions (ex: `aria-live="polite"` para feedback não urgente, `aria-live="assertive"` para erros urgentes).
    *   Garantir bom contraste de cores.
    *   Se a mensagem incluir um botão de fechar ou ações, eles devem ser acessíveis por teclado.
    *   Para erros de formulário inline, associar a mensagem de erro ao campo de formulário correspondente usando `aria-describedby`.
-   **Não Incomodar:** Evitar mensagens excessivas, muito frequentes ou que interrompem desnecessariamente.
-   **Opção de Dispensar:** Para mensagens persistentes (como banners ou alertas inline), fornecer um meio claro para o usuário dispensá-las, se apropriado.

## O Que Evitar

-   Mensagens vagas ou técnicas que o usuário não entenderá.
-   Usar cores de forma inconsistente ou que não sigam as convenções semânticas.
-   Interromper o usuário com modais para informações triviais.
-   Mensagens que desaparecem muito rápido para serem lidas (no caso de toasts).
-   Falta de feedback quando o usuário espera (ex: após submeter um formulário).
