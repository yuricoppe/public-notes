---
title: "chat live"
description: "O componente de Chat em Tempo Real permite a comunicação síncrona entre usuários ou entre um usuário e um agente de suporte."
tags:
  - tema/ui
  - tipo/glossario
---

## Chat (Live) (Chat em Tempo Real)

O componente de Chat em Tempo Real permite a comunicação síncrona entre usuários ou entre um usuário e um agente de suporte. É crucial para fornecer assistência imediata, facilitar a colaboração ou criar comunidades interativas.

## Casos de Uso

-   Suporte ao cliente ao vivo.
-   [[Glossário/Componentes/messaging|Mensagens]] diretas entre usuários.
-   Salas de bate-papo em grupo.
-   Ferramentas de colaboração em equipe.
-   Sessões de perguntas e respostas ao vivo (Q&A).

## Funcionalidades Essenciais

![Janela de chat anotada: mensagem recebida à esquerda, mensagem enviada à direita com estado de entrega, indicador de digitando e campo de entrada](attachments/glossario-anatomia-chat.svg)

-   **Exibição de Mensagens:** [[Glossário/Elementos/listas|Lista]] de mensagens em ordem cronológica (geralmente as mais recentes no final).
    -   Nome/avatar do remetente.
    -   Conteúdo da mensagem (texto, emojis, opcionalmente [[Glossário/Elementos/imagem|imagens]]/arquivos).
    -   Timestamp da mensagem.
-   **Entrada de Mensagem:** [[Glossário/Elementos/form_controls|Campo de texto]] para digitar e enviar novas mensagens.
    -   [[Glossário/Elementos/botoes|Botão]] de envio.
    -   (Opcional) Indicador de "digitando...".
-   **Notificações:** Alertas sonoros e/ou visuais para novas mensagens, especialmente se a janela de chat não estiver em foco.
-   **Scroll (Rolagem):** Rolagem automática para a mensagem mais recente e capacidade de rolar para cima para ver o histórico.
-   **Indicadores de Status:**
    *   Status do usuário (online, offline, ausente).
    *   Confirmação de entrega/leitura de mensagens (opcional).

## Melhores Práticas

-   **Clareza Visual:** Diferenciar claramente as mensagens enviadas pelo usuário das mensagens recebidas.
    *   Alinhamento (ex: mensagens do usuário à direita, outras à esquerda).
    *   [[Glossário/Linguagem Visual/cor|Cores]] de fundo diferentes para as "bolhas" de mensagem.
-   **Feedback Imediato:** O usuário deve ver sua mensagem aparecer na interface assim que a envia. Qualquer atraso ou falha no envio deve ser comunicado.
-   **Desempenho:** O chat deve ser rápido e responsivo, mesmo com um grande volume de mensagens ou participantes.
-   **Acessibilidade (a11y):**
    *   Novas mensagens devem ser anunciadas por leitores de tela (usando `aria-live` regions).
    *   O campo de entrada e o botão de envio devem ser acessíveis e operáveis por teclado.
    *   Permitir o uso de zoom sem quebrar o layout.
    *   Garantir bom contraste de cores.
-   **Privacidade e Segurança:** Informar os usuários sobre políticas de privacidade, especialmente se as conversas forem gravadas. Usar criptografia para dados sensíveis.
-   **Tratamento de Erros:** Informar o usuário sobre problemas de conexão ou falhas no envio de mensagens.
-   **Histórico de Mensagens:** Permitir o acesso a mensagens anteriores (se aplicável à política de retenção).
-   **Responsividade:** A interface do chat deve se adaptar a diferentes tamanhos de tela, mantendo a usabilidade.

## Funcionalidades Adicionais (Opcionais)

-   Envio de arquivos e imagens.
-   Emojis e GIFs.
-   Respostas a mensagens específicas (threads).
-   Edição e exclusão de mensagens (com moderação e indicações claras).
-   Busca no histórico de mensagens.
-   Transcrição do chat (opção para salvar ou enviar por e-mail).
-   Avatares dos usuários.
-   Reações a mensagens.

## Estrutura Comum

-   **[[Glossário/Elementos/cabecalhos|Cabeçalho]]:** Nome do contato/grupo, status, opções (ex: fechar chat, informações do contato).
-   **Área de Mensagens:** Lista rolável das mensagens.
-   **[[Glossário/Componentes/footer|Rodapé]]/Área de Entrada:** Campo de texto para nova mensagem, botão de enviar, (opcional) anexar arquivo.

## O Que Evitar

-   Notificações excessivas ou irritantes.
-   Interface desorganizada ou difícil de ler.
-   Falta de feedback sobre o status das mensagens ou conexão.
-   Rolagem automática que impede o usuário de ler mensagens mais antigas.
-   Não informar os usuários se o chat é com um bot ou um humano.
