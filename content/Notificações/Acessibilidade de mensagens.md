---
title: "Acessibilidade de mensagens"
description: "Como fazer uma mensagem dinâmica existir para quem usa leitor de tela — e por que o toast que some sozinho é o componente mais problemático dessa família"
tags:
  - tema/acessibilidade
  - dominio/notificacoes
  - tipo/artigo
---

Uma mensagem que aparece na tela depois do carregamento não existe automaticamente para quem usa leitor de tela. Ela precisa ser anunciada, e o anúncio precisa ser declarado no HTML **antes** de haver o que anunciar. Essa inversão é a origem da maior parte dos bugs de acessibilidade dessa família de componentes.

## O critério que rege isso

O WCAG 4.1.3 (*Status Messages*, nível AA) diz que mensagens de status precisam ser determináveis programaticamente por papel ou propriedade, de modo que possam ser apresentadas por tecnologia assistiva **sem receber foco**.

Duas condições definem o que conta como mensagem de status: ela informa sucesso ou resultado de uma ação, estado de espera, progresso de um processo ou existência de erros; e não é entregue por meio de uma mudança de contexto. Exemplos típicos: "18 resultados encontrados", "5 itens no carrinho", "entrada inválida", uma barra de progresso.

O que **não** conta: um diálogo de erro que rouba o foco (isso é mudança de contexto, e tem outras regras), a expansão de um acordeão (mudança de estado de componente), ou campos novos que aparecem condicionalmente.

A falha catalogada correspondente, F103, é exatamente o caso comum: mostrar a mensagem visualmente e não expor papel nem propriedade nenhuma.

## Escolher o papel

![Árvore de decisão entre role=alertdialog, role=alert e role=status para anunciar mensagens dinâmicas](attachments/notificacoes-aria-live.svg)

A pergunta certa não é "quão importante é a mensagem", e sim **"vale interromper a frase que o leitor de tela está falando agora?"**.

**`role="status"`** — o padrão para quase tudo. Equivale a `aria-live="polite"`: o anúncio espera a pessoa ficar ociosa. Sucesso, progresso, contagem de resultados, salvamento automático.

**`role="alert"`** — equivale a `aria-live="assertive"`: interrompe o que estiver sendo lido. Reservado para o que impede a pessoa de continuar. Usar `assertive` em conteúdo não crítico é uma falha por excesso, não por falta: atrapalha mais do que a ausência de anúncio.

**`role="log"`** — para listas que crescem: chat, console, histórico.

**`role="alertdialog"`** — quando a mensagem bloqueia a tarefa. Aí não é região viva nenhuma: é diálogo, recebe foco, tem título e botões navegáveis.

A separação entre `alert` e `alertdialog` é explícita no ARIA Authoring Practices Guide: **um alerta não deve afetar o foco do teclado**. Se for necessário interromper o fluxo de trabalho, o componente é o diálogo de alerta.

Na prática, vale manter o `aria-live` redundante junto ao papel (`role="status" aria-live="polite"`), porque a compatibilidade entre leitores de tela ainda é irregular. A exceção conhecida é `role="alert"` no VoiceOver do iOS, onde a combinação pode causar anúncio duplicado.

## As três coisas que quebram

**A região precisa existir vazia no HTML antes.** Tecnologias assistivas anunciam *mudanças* dentro de uma região viva. Inserir no DOM um elemento que já vem com `aria-live` e com o texto dentro é a receita para o silêncio. A exceção é `role="alert"`, que costuma ser anunciado mesmo quando já está na marcação inicial — e é justamente por isso que ele é sobreutilizado.

**Texto igual não dispara anúncio.** Se a pessoa erra o mesmo campo duas vezes seguidas e a mensagem é idêntica, o segundo anúncio pode simplesmente não acontecer. A saída é limpar a região antes de reescrever, com um ciclo de renderização entre as duas operações.

**Sumir por tempo corta o anúncio.** Um toast que desaparece em quatro segundos pode ser removido do DOM antes de o leitor de tela terminar a frase.

Há ainda `aria-atomic`, que decide se o leitor anuncia a região inteira ou só o pedaço que mudou. O padrão é anunciar só o que mudou — o que produz anúncios sem sentido quando a região tem partes interdependentes ("34" em vez de "17:34"). Use `aria-atomic="true"` quando o pedaço isolado não se sustenta.

## O toast é o problema

O componente que some sozinho concentra quase todas as tensões dessa página.

O ARIA Authoring Practices Guide diz para **evitar alertas que desaparecem automaticamente**, porque isso arrisca violar o WCAG 2.2.3 (*No Timing*). O Carbon põe a mesma regra em duas linhas na seção de acessibilidade: não use notificações com temporizador para mensagens críticas ou de emergência, porque algumas pessoas precisam de mais tempo para ler ou interagir. E acrescenta a outra metade: as pessoas devem poder gerenciar ou limitar as notificações não críticas, o que reduz distração — o que ajuda especialmente quem tem limitação cognitiva (WCAG 2.2.4, *Interruptions*).

O conjunto de regras que sai daí é bem definido:

- **Toast com ação nunca some sozinho.** Precisa persistir até ser dispensado. Um botão que desaparece antes de ser alcançável não é um botão.
- **Erro que exige ação não vai em toast.** Vai inline, perto do que precisa ser corrigido, e permanece.
- **Toast que some sozinho serve para confirmação passageira** cujo conteúdo continue disponível em outro lugar — tipicamente a central de notificações.
- **Duração é tempo de leitura, não tempo de animação.** Mensagens mais longas precisam de mais tempo, e ainda assim vão ser curtas demais para parte das pessoas.
- **Pausar ao receber foco ou ao passar o ponteiro** é o mínimo aceitável, e não substitui o botão de fechar.

O jeito mais honesto de olhar para isso: o toast é um componente que troca garantia de leitura por baixo custo de atenção. É uma troca legítima — desde que a informação não seja crítica e desde que exista um lugar onde ela permaneça.

## Formulário: associar, não só posicionar

Para erro de campo, proximidade visual não basta. A mensagem precisa estar associada ao campo por `aria-describedby`, e o campo marcado com `aria-invalid="true"`. Sem isso, quem navega campo a campo com leitor de tela ouve o rótulo e não ouve o erro — a mensagem está na tela, a dois centímetros, e é invisível.

Quando há um resumo de erros no topo do formulário, ele deve ser focável e cada item deve levar ao campo correspondente. Resumo que não leva a lugar nenhum é decoração.

## Não confiar só na cor

Vale repetir o óbvio porque continua sendo o defeito mais frequente: a distinção entre sucesso, aviso e erro não pode depender apenas da cor. Ícone, texto e o próprio conteúdo da frase precisam carregar a informação. Uma mensagem que só é reconhecível como erro por ser vermelha não é reconhecível como erro para uma parte considerável das pessoas.

O contraste do texto e o do ícone precisam passar nos limites do WCAG, o que é justamente onde as paletas semânticas costumam falhar — amarelo de aviso sobre fundo claro é o caso clássico.

## Checklist

- [ ] A região viva existe no HTML antes de a mensagem chegar
- [ ] `role="status"` por padrão; `role="alert"` só para o que impede continuar
- [ ] Mensagem que bloqueia usa `alertdialog`, com foco e navegação por teclado
- [ ] Nada que exija ação some por tempo
- [ ] Texto repetido é limpo antes de ser reescrito
- [ ] Erro de campo associado por `aria-describedby` + `aria-invalid`
- [ ] Botão de fechar alcançável por teclado, com rótulo acessível
- [ ] Status distinguível sem cor
- [ ] Contraste de texto e ícone verificado nos quatro status
- [ ] Existe onde ler de novo o que sumiu

---

**Antes:** [[Anatomia de um sistema de mensagens]] · [[Escrever a mensagem]]

**Ver também:** [[Acessibilidade/index|Acessibilidade]]
