---
title: "chat live"

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

-   **Exibição de [[Glossário/Componentes/messaging|Mensagens]]:** [[Glossário/Elementos/listas|Lista]] de [[Glossário/Componentes/messaging|mensagens]] em ordem cronológica (geralmente as mais recentes no final).
    -   Nome/avatar do remetente.
    -   Conteúdo da mensagem (texto, emojis, opcionalmente [[Glossário/Elementos/imagem|imagens]]/arquivos).
    -   Timestamp da mensagem.
-   **Entrada de Mensagem:** [[Glossário/Elementos/form_controls|Campo de texto]] para digitar e enviar novas [[Glossário/Componentes/messaging|mensagens]].
    -   [[Glossário/Elementos/botoes|Botão]] de envio.
    -   (Opcional) Indicador de "digitando...".
-   **Notificações:** Alertas sonoros e/ou visuais para novas [[Glossário/Componentes/messaging|mensagens]], especialmente se a janela de chat não estiver em foco.
-   **Scroll (Rolagem):** Rolagem automática para a mensagem mais recente e capacidade de rolar para cima para ver o histórico.
-   **Indicadores de Status:**
    *   Status do usuário (online, offline, ausente).
    *   Confirmação de entrega/leitura de [[Glossário/Componentes/messaging|mensagens]] (opcional).

## Melhores Práticas

-   **Clareza Visual:** Diferenciar claramente as [[Glossário/Componentes/messaging|mensagens]] enviadas pelo usuário das [[Glossário/Componentes/messaging|mensagens]] recebidas.
    *   Alinhamento (ex: [[Glossário/Componentes/messaging|mensagens]] do usuário à direita, outras à esquerda).
    *   [[Glossário/Linguagem Visual/cor|Cores]] de fundo diferentes para as "bolhas" de mensagem.
-   **Feedback Imediato:** O usuário deve ver sua mensagem aparecer na interface assim que a envia. Qualquer atraso ou falha no envio deve ser comunicado.
-   **Desempenho:** O chat deve ser rápido e responsivo, mesmo com um grande volume de [[Glossário/Componentes/messaging|mensagens]] ou participantes.
-   **Acessibilidade (a11y):**
    *   Novas [[Glossário/Componentes/messaging|mensagens]] devem ser anunciadas por leitores de tela (usando `aria-live` regions).
    *   O campo de entrada e o [[Glossário/Elementos/botoes|botão]] de envio devem ser acessíveis e operáveis por teclado.
    *   Permitir o uso de zoom sem quebrar o layout.
    *   Garantir bom contraste de [[Glossário/Linguagem Visual/cor|cores]].
-   **Privacidade e Segurança:** Informar os usuários sobre políticas de privacidade, especialmente se as conversas forem gravadas. Usar criptografia para dados sensíveis.
-   **Tratamento de Erros:** Informar o usuário sobre problemas de conexão ou falhas no envio de [[Glossário/Componentes/messaging|mensagens]].
-   **Histórico de [[Glossário/Componentes/messaging|Mensagens]]:** Permitir o acesso a [[Glossário/Componentes/messaging|mensagens]] anteriores (se aplicável à política de retenção).
-   **Responsividade:** A interface do chat deve se adaptar a diferentes tamanhos de tela, mantendo a usabilidade.

## Funcionalidades Adicionais (Opcionais)

-   Envio de arquivos e [[Glossário/Elementos/imagem|imagens]].
-   Emojis e GIFs.
-   Respostas a [[Glossário/Componentes/messaging|mensagens]] específicas (threads).
-   Edição e exclusão de [[Glossário/Componentes/messaging|mensagens]] (com moderação e indicações claras).
-   Busca no histórico de [[Glossário/Componentes/messaging|mensagens]].
-   Transcrição do chat (opção para salvar ou enviar por e-mail).
-   Avatares dos usuários.
-   Reações a [[Glossário/Componentes/messaging|mensagens]].

## Estrutura Comum

-   **[[Glossário/Elementos/cabecalhos|Cabeçalho]]:** Nome do contato/grupo, status, opções (ex: fechar chat, informações do contato).
-   **Área de [[Glossário/Componentes/messaging|Mensagens]]:** [[Glossário/Elementos/listas|Lista]] rolável das [[Glossário/Componentes/messaging|mensagens]].
-   **[[Glossário/Componentes/footer|Rodapé]]/Área de Entrada:** [[Glossário/Elementos/form_controls|Campo de texto]] para nova mensagem, [[Glossário/Elementos/botoes|botão]] de enviar, (opcional) anexar arquivo.

## O Que Evitar

-   Notificações excessivas ou irritantes.
-   Interface desorganizada ou difícil de ler.
-   Falta de feedback sobre o status das [[Glossário/Componentes/messaging|mensagens]] ou conexão.
-   Rolagem automática que impede o usuário de ler [[Glossário/Componentes/messaging|mensagens]] mais antigas.
-   Não informar os usuários se o chat é com um bot ou um humano.
