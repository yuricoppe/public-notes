---
title: "Anatomia de um sistema de mensagens"
description: "O que é indicador, o que é validação, o que é notificação — e como escolher entre inline, toast, banner, push e modal sem gastar atenção que não precisava ser gasta"
tags:
  - tema/ui
  - dominio/notificacoes
  - tipo/artigo
---

Antes de decidir se uma mensagem vira toast ou banner, há uma decisão anterior que quase sempre é pulada: descobrir se aquilo é mesmo uma notificação. Boa parte do ruído de um produto maduro não vem de notificações mal desenhadas. Vem de coisas que nunca deveriam ter sido notificação nenhuma.

## Três formas de comunicar estado, e só uma interrompe

Kim Flaherty, do Nielsen Norman Group, separa três mecanismos que os times costumam tratar como sinônimos:

![Comparação entre indicador, validação e notificação segundo o Nielsen Norman Group, por quem dispara, se exige ação e onde aparece](attachments/notificacoes-tres-comunicacoes.svg)

**Indicador** é um recurso visual que faz um elemento se destacar porque há algo especial nele. Um ponto, um contador, um negrito, um ícone. Dispara porque uma condição existe, não exige ação nenhuma e fica colado no elemento a que se refere. É passivo por definição: espera ser notado.

**Validação** trata do que a pessoa acabou de digitar. Como ela mesma fez a coisa que precisa ser corrigida, a mensagem não precisa ensinar a tarefa — precisa dizer o que está errado e como consertar. Fica no campo, associada a ele.

**Notificação** informa sobre uma ocorrência do sistema. Pode não ter relação nenhuma com o que a pessoa está fazendo agora, e é justamente por isso que ela é a única das três que legitimamente interrompe.

A pergunta que separa as três é simples: **o que disparou isto?** Se a resposta é "a própria pessoa, agora", quase nunca é notificação. É validação ou indicador — e, portanto, não deveria puxar atenção para fora da tarefa.

O erro de casar mal os três é caro nos dois sentidos. Usar notificação para o que era indicador produz ruído. Usar indicador para o que era notificação produz silêncio no momento errado — a mensagem existe, mas ninguém a vê.

## Status e tipo são eixos diferentes

O padrão de notificação do Carbon, da IBM, faz uma separação que vale copiar: toda mensagem tem um **status** e um **tipo**, e eles são decisões independentes.

![Matriz separando status — informativo, sucesso, aviso, erro — de tipo — inline, toast, banner, modal](attachments/notificacoes-tipo-x-status.svg)

O **status** diz o que aconteceu: informativo, sucesso, aviso, erro. É o que define cor e ícone.

O **tipo** diz quanto aquilo pode atrapalhar: inline, toast, banner, modal, painel. É o que define comportamento e permanência.

Confundir os dois produz o defeito mais comum que existe nessa área: **erro dentro de um toast**. Vermelho, com ícone de alerta, mensagem grave — e sumindo sozinho em quatro segundos, sem deixar rastro e sem oferecer nada para fazer. O status era grave; o tipo, descartável.

Vale ainda separar as mensagens por origem, porque isso muda onde elas devem aparecer:

- **Geradas por tarefa** nascem de uma ação da pessoa e devem ficar na região da tela onde ela está trabalhando. Formulário enviado, upload que falhou, credencial não encontrada. Como a pessoa acabou de agir, não é preciso dar muito contexto.
- **Geradas pelo sistema** nascem independentemente da ação da pessoa: conexão caiu, manutenção programada, relatório pronto, sessão prestes a expirar. Como não têm relação com o que ela está fazendo, precisam de **mais** contexto, não menos.

## A escada

Com isso resolvido, a escolha do componente vira uma única pergunta: qual é o degrau mais baixo que ainda entrega a mensagem?

![Escada de interrupção com sete degraus, do indicador ao modal, com o custo de atenção e o uso adequado de cada um](attachments/notificacoes-escada-interrupcao.svg)

**Indicador.** Custo de atenção próximo de zero. Serve para "tem coisa nova aqui". A maior parte do que os produtos mandam por push caberia aqui.

**Notificação inline.** Fica na região a que se refere e persiste até ser resolvida ou dispensada. É o padrão certo para feedback de formulário e estado de seção. Boas práticas do Carbon: colocar perto do item relacionado, manter a mensagem em menos de duas linhas, não cobrir outro conteúdo, e dar o próximo passo.

**Callout.** Diferente de todo o resto: não é disparado por ninguém. Carrega junto com a página, é persistente e não pode ser dispensado. Serve para orientar **antes** da tarefa — e, por isso, não tem status de sucesso nem de erro. Não é mecanismo de feedback.

**Toast.** Entra, fica alguns segundos e sai. A regra que decide tudo: **toast com ação precisa persistir até ser dispensado**, senão você está oferecendo um botão e tirando-o da mesa antes que a pessoa consiga alcançá-lo. Toast sem ação pode sumir sozinho. Mensagens curtas — o Carbon sugere não passar de três linhas — e largura fixa; se está esticando para caber, o componente é outro.

**Banner global.** Nível de sistema ou de produto, não de tarefa. Atravessa páginas, persiste até ser dispensado. Manutenção, degradação, cobrança vencida.

**Push.** Alcança a pessoa fora do produto, num contexto que você não vê e não controla. O único degrau em que o custo de errar é externo ao seu produto. Tratado em detalhe em [[Permissão e consentimento]].

**Modal.** Rouba o foco e impede continuar. Justifica-se quando a informação é crítica ou a ação é imediata — na prática, perda irreversível de dado ou decisão que não dá para adiar. Bloquear é disruptivo por definição: se a mensagem não é relevante para a tarefa atual **e** não traz os passos para resolver, ela não deveria bloquear nada.

O erro mais comum não é escolher o componente errado. É escolher um degrau acima do necessário porque o time quer garantir que a mensagem seja vista. Garantir a visualização de tudo é matematicamente o mesmo que não garantir a de nada.

## A central de notificações

Há um componente que não está na escada porque não interrompe: a central, o sino, o inbox. Ela é o lugar onde as mensagens vão morar depois de terem sido — ou não terem sido — mostradas.

Ela resolve dois problemas que nenhum dos outros componentes resolve.

O primeiro é **a mensagem perdida**. Todo toast é uma aposta: se a pessoa estava olhando, ela viu; se não, a informação evaporou. Uma central transforma essa aposta em algo recuperável. Isso significa que a existência de uma central é o que **autoriza** o toast a ser efêmero — sem ela, cada toast é um pequeno risco de perda.

O segundo é **a saída da escada**. Com uma central funcionando, mensagens de prioridade baixa não precisam de canal nenhum. Elas simplesmente aparecem lá, e quem quiser olhar olha. É a diferença entre empurrar e disponibilizar — e é o mecanismo que permite que aqueles 80% de prioridade baixa existam sem custo de atenção.

Uma central que funciona precisa de três coisas que costumam faltar: distinguir lido de não lido de forma confiável, permitir marcar tudo como lido sem drama, e não usar o contador de não lidas como métrica de engajamento. Um badge que nunca zera vira o *alarme permanente* da engenharia de alarmes: parte da paisagem, invisível.

## Antes de desenhar qualquer componente

Um sistema de mensagens não é uma coleção de componentes. É uma alocação de atenção, e a alocação precisa existir antes dos componentes.

A ordem que funciona:

1. **Inventariar os gatilhos.** Todos os eventos que hoje geram alguma mensagem, em qualquer canal. Inclusive os antigos, os de campanha, os que ninguém lembra de ter criado.
2. **Classificar cada um por consequência de ignorar.** Três níveis. Com orçamento.
3. **Só então escolher o canal e o componente**, do degrau mais baixo para cima.
4. **Definir quem pode desligar o quê**, e garantir que o controle exista dentro do produto — não só nas configurações do sistema operacional.

Fazer na ordem inversa — escolher os componentes primeiro e depois tentar decidir o que vai em cada um — é como todo mundo faz, e é por isso que quase todo produto tem um catálogo de componentes bonito e um sistema de mensagens ruidoso.

---

**Continua em:** [[Permissão e consentimento]] · [[Frequência, agrupamento e controle]] · [[Escrever a mensagem]] · [[Acessibilidade de mensagens]]

**Ver também:** [[Glossário/Componentes/messaging|Messaging (Glossário)]] · [[Glossário/Componentes/toast|Toast]] · [[Glossário/Componentes/dialog|Dialog]]
