---
title: "Comments (Comentários)"
description: "O componente de Comentários permite que os usuários publiquem e visualizem feedback, discussões ou anotações relacionadas a um conteúdo específico, como um artigo, produto,…"
tags:
  - tema/ui
  - tipo/glossario
---

## Comments (Comentários)

O componente de Comentários permite que os usuários publiquem e visualizem feedback, discussões ou anotações relacionadas a um conteúdo específico, como um artigo, produto, postagem de blog ou tarefa.

## Casos de Uso

-   Seção de comentários em artigos de blog ou notícias.
-   Avaliações e opiniões de usuários sobre produtos.
-   Discussões em fóruns ou comunidades.
-   Feedback em [[Glossário/Entregáveis/prototype|protótipos]] ou designs.
-   Anotações em documentos ou tarefas colaborativas.

## Funcionalidades Essenciais

![Fila de comentários anotada: ordenação, autor com data, resposta aninhada em um nível, ação de denunciar e botão carregar mais](attachments/glossario-thread-comentarios.svg)

-   **Exibição de Comentários:**
    *   [[Glossário/Elementos/listas|Lista]] de comentários, geralmente em ordem cronológica ou por relevância.
    *   Nome/avatar do autor do comentário.
    *   Conteúdo do comentário.
    *   Timestamp (data e hora) da postagem.
-   **[[Glossário/Padrões/form_structure|Formulário]] para Novo Comentário:**
    *   [[Glossário/Elementos/form_controls|Campo de texto]] (textarea) para o usuário digitar o comentário.
    *   [[Glossário/Elementos/botoes|Botão]] para submeter/publicar o comentário.
-   **Identificação do Usuário:** Para usuários logados, o nome/avatar é preenchido automaticamente. Para anônimos (se permitido), pode haver campos para nome e e-mail.
-   **Respostas/Threads (Opcional, mas Comum):** Permitir que usuários respondam a comentários específicos, criando uma discussão aninhada.
-   **Paginação ou "Carregar Mais":** Para lidar com um grande número de comentários.

## Melhores Práticas

-   **Clareza e Legibilidade:** Comentários devem ser fáceis de ler, com bom [[Glossário/Linguagem Visual/espacamento|espaçamento]] e [[Glossário/Linguagem Visual/tipografia|tipografia]] clara.
-   **Moderação:** Implementar ou ter planos para moderação de comentários (manual ou automatizada) para evitar spam, abuso e conteúdo inadequado.
    *   Opções de denúncia (report) de comentários.
-   **Feedback de Submissão:** Informar ao usuário se o comentário foi publicado com sucesso, está aguardando moderação ou se houve um erro.
-   **Ordenação:** Oferecer opções de ordenação (ex: mais recentes, mais antigos, mais votados) se apropriado.
-   **Acessibilidade (a11y):**
    *   O formulário de comentário deve ser acessível, com labels para os campos e botões operáveis por teclado.
    *   Comentários devem ser estruturados de forma semântica (ex: cada comentário como um `<article>` ou `<li>` dentro de uma lista).
    *   Ações como responder, curtir, denunciar devem ser botões acessíveis.
-   **Notificações (Opcional):** Notificar usuários sobre respostas aos seus comentários.
-   **[[Glossário/Elementos/links|Links]] em Comentários:** Decidir se links são permitidos e como são tratados (ex: `rel="nofollow"`, abrir em nova aba).

## Funcionalidades Adicionais (Opcionais)

-   **Curtir/Descurtir (Upvote/Downvote):** Permitir que usuários avaliem comentários.
-   **Edição/Exclusão de Comentários:** Permitir que autores (ou moderadores) editem ou excluam seus próprios comentários (com limites de tempo ou indicações de edição).
-   **Avatares dos Usuários.**
-   **Contador de Comentários.**
-   **Destaque de Comentários:** (ex: pelo autor do post, por moderadores).
-   **Suporte a Markdown ou Rich Text Básico:** Para formatação de texto nos comentários.
-   **[[Glossário/Padrões/authentication|Login]] Social para Comentar.**

## Estrutura Comum

-   **Título da Seção** (ex: "Comentários", "Discussão").
-   **(Opcional) Resumo/Contador de Comentários.**
-   **Formulário de Novo Comentário.**
-   **Lista de Comentários:**
    *   Cada comentário individual com:
        *   Avatar/Nome do Autor
        *   Timestamp
        *   Corpo do Comentário
        *   Ações (Responder, Curtir, etc.)
        *   (Opcional) Respostas aninhadas.
-   **(Opcional) Paginação ou Botão "Carregar Mais".**

## O Que Evitar

-   Formulários de comentário complexos ou que exigem muita informação.
-   Falta de moderação ou ferramentas para lidar com abuso.
-   Interface de comentários desorganizada ou difícil de acompanhar as discussões.
-   Não permitir que usuários anônimos (se desejado) participem facilmente (ex: exigindo login para tudo).
