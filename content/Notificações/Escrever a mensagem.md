---
title: "Escrever a mensagem"
description: "O que dizer quando só há um título, quanto espaço existe de verdade em cada plataforma, e por que quase toda mensagem de erro está errada"
tags:
  - tema/conteudo
  - dominio/notificacoes
  - tipo/artigo
---

Depois de decidir se a mensagem deve existir, por qual canal e em que componente, sobra o pedaço que costuma ser feito por último e em cima da hora: o texto. É também o pedaço com a maior razão entre impacto e custo — reescrever uma frase é barato, e uma frase ruim desperdiça toda a atenção que os passos anteriores gastaram para conquistar.

## Três coisas, nesta ordem

![Comparação entre uma mensagem de erro ruim, que só informa um código técnico, e uma boa, que nomeia o que aconteceu, o efeito e a próxima ação](attachments/notificacoes-anatomia-mensagem.svg)

Toda mensagem precisa responder três perguntas, e quase toda mensagem ruim responde só a primeira:

**O que aconteceu.** Em palavras da pessoa, não do sistema. "Request failed with status code 500" descreve o evento com precisão e não comunica nada.

**O que isso significa para quem está lendo.** Especialmente o estado do dado: o que foi salvo, o que se perdeu, o que continua valendo. É a informação que as pessoas mais procuram e a que menos aparece.

**Qual é a próxima ação.** Um verbo. Uma ação só. Dentro da própria mensagem, se possível — resolver sem sair dali é o maior ganho que uma notificação pode oferecer.

O Carbon põe a mesma ideia em quatro instruções curtas: usar linguagem clara e concisa; não usar jargão técnico; garantir que a pessoa saiba como agir quando for necessário; nunca deixá-la sem próximo passo.

Vale uma nota sobre contexto, que muda a dose: mensagens **geradas por tarefa** não precisam de muito preâmbulo, porque a pessoa acabou de fazer a coisa. Mensagens **geradas pelo sistema** chegam sem relação com o que ela está fazendo e precisam se situar sozinhas.

## O teste do título sozinho

Escreva para o título como se ele fosse a mensagem inteira. Na maioria dos casos, ele é.

![Anatomia de uma notificação push anotada, com os limites práticos de caracteres de título e corpo e o número de botões de ação em iOS, Android e web push](attachments/notificacoes-anatomia-push.svg)

O corpo trunca sem aviso, e onde ele trunca depende de sistema, versão, tamanho de tela, tamanho de fonte escolhido pela pessoa e se a tela está bloqueada. Os números que circulam — algo em torno de 25 a 50 caracteres de título no iOS, ~50 no Android, 60 a 80 na web; corpo perto de 120 a 150 — servem como teto de segurança, não como promessa. A régua já mudou e vai mudar de novo.

A consequência prática é uma regra de escrita, não de contagem: **ponha a palavra mais importante no começo.** Não "Temos uma novidade sobre o seu pedido #4821"; e sim "Pedido a caminho — sai para entrega hoje".

O mesmo vale para o número de ações. iOS aceita até quatro botões, Android até três, web push até dois — e a recomendação do Carbon para notificação em tela é ainda mais restritiva: **uma ação só**, com rótulo de no máximo duas palavras. Mais de uma ação transforma uma mensagem numa decisão, e decisão é justamente o que uma notificação não deveria exigir.

## Tom proporcional à consequência

O tom é a parte em que a maioria dos guias de conteúdo erra por excesso de personalidade. A regra simples: **o tom acompanha a gravidade, e a gravidade é definida pela consequência para quem lê — não pela importância que o time atribui ao evento.**

Numa mensagem de erro, isso significa sobriedade. Nada de exclamação, nada de humor, nada de pedido de desculpa no lugar da solução. Uma pessoa que acabou de perder trabalho não quer simpatia; quer saber se dá para recuperar.

Numa mensagem de sucesso, significa brevidade. Sucesso confirmado em três palavras é melhor que sucesso celebrado em duas linhas — a pessoa já quer seguir.

Numa mensagem de aviso, significa nomear a consequência sem dramatizar. Aviso é sobre um caminho que leva a um lugar indesejado; dizer qual é o lugar é o conteúdo inteiro.

E há o caso especial das mensagens que chegam fora do produto. Um push aparece na tela de bloqueio, potencialmente na frente de outras pessoas. Duas consequências: **nada sensível no corpo** — valores, diagnósticos, conteúdo de mensagem privada, se o app não estiver configurado para esconder prévia; e nada que dependa de contexto que a pessoa não tem naquele momento.

## Erros de formulário são um caso à parte

A validação tem regras próprias porque a pessoa está no meio de uma tarefa e o erro é dela.

Diga **qual campo**, **o que está errado** e **como corrigir**. As três coisas. "Campo inválido" só cumpre a primeira, e mal.

Não descreva a regra — descreva a saída. "A senha deve conter ao menos um caractere especial" é melhor do que "senha inválida", mas ainda pior do que mostrar a regra **antes** de a pessoa digitar, que é quando a informação seria útil.

E mantenha a mensagem junto ao campo, associada a ele programaticamente. Isso não é preferência estética: é o que faz a mensagem existir para quem usa leitor de tela, e está detalhado em [[Acessibilidade de mensagens]].

## O que cortar

**Códigos internos**, a menos que exista um suporte que peça por eles — e, nesse caso, o código vai discreto, depois da frase que a pessoa precisa entender.

**Voz passiva** que esconde quem faz o quê. "Um erro foi encontrado" versus "não deu para salvar".

**Palavras que descrevem a interface** em vez do mundo. Ninguém tem um problema com um "registro"; tem um problema com um pedido, uma foto, um pagamento.

**"Por favor, tente novamente"** sozinho, sem dizer se algo mudou. Se tentar de novo tem a mesma chance de falhar, você está pedindo à pessoa que repita um erro.

**Exclamação em mensagem de erro.** Nunca combina.

## Um teste rápido

Leia só o título em voz alta. Se, ouvindo apenas aquilo, a pessoa sabe **se precisa fazer alguma coisa**, a mensagem está pronta. Se ela precisa abrir para descobrir se aquilo era importante, a mensagem já custou uma interrupção antes de ter entregue qualquer valor — e é essa a interrupção que as pessoas contabilizam quando decidem desligar o canal.

---

**Continua em:** [[Acessibilidade de mensagens]]

**Antes:** [[Anatomia de um sistema de mensagens]] · [[Frequência, agrupamento e controle]]
