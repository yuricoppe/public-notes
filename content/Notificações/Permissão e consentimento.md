---
title: "Permissão e consentimento"
description: "O prompt nativo só pode ser mostrado uma vez. O que fazer antes dele, o que fazer se for negado, e por que o consentimento não termina no aceite"
tags:
  - tema/ux
  - dominio/notificacoes
  - tipo/artigo
---

Existe uma assimetria no pedido de permissão de notificação que muda todo o resto do desenho: **o prompt nativo do sistema só pode ser mostrado uma vez**. Se a pessoa recusa, o caminho de volta é ir nas configurações do sistema operacional ou do navegador — um percurso que quase ninguém faz, e ninguém faz por vontade própria.

Isso significa que o pedido não é um passo de fluxo. É um recurso escasso e não renovável, e gastá-lo mal é a decisão mais cara que se toma nessa área.

## O duplo pedido

A resposta conhecida é separar a pergunta em duas, com a interface antes do sistema.

![Fluxo do duplo pedido: convite na interface, prompt nativo apenas para quem aceitou, e página de recuperação para quem bloqueou](attachments/notificacoes-duplo-opt-in.svg)

O primeiro pedido acontece dentro do seu produto, com o seu design, e serve para explicar o que a pessoa ganha. Recusar aqui não custa nada: dá para perguntar de novo depois, em contexto melhor. O segundo — o prompt nativo — é disparado **só para quem já disse sim**. Você gasta a chance única com quem já demonstrou interesse.

Vitaly Friedman resume a lógica como pedir permissão apenas quando há alta probabilidade de aceite. E o momento importa tanto quanto a explicação: um pedido de localização faz sentido na página de lojas próximas; um pedido de notificação faz sentido depois de uma compra concluída, quando existe algo real para avisar.

Alita Kendrick, do Nielsen Norman Group, lista os erros na ordem em que aparecem, e os dois primeiros são sobre isso: pedir logo depois da primeira abertura, quando a pessoa ainda não sabe se o app vale alguma coisa; e não dizer sobre o que serão as notificações, o que torna impossível avaliar se aceitar compensa.

O convite precisa dizer três coisas concretas:

- **Sobre o que** você vai avisar — em exemplos reais, não em categorias vagas. "Avisamos quando seu pedido sair para entrega" funciona; "receba atualizações importantes" não diz nada.
- **Com que frequência.** Uma estimativa honesta vale mais do que uma promessa de moderação.
- **Que dá para desligar depois, e onde.** É o que reduz o custo percebido do sim.

## Quando a resposta é não

O erro que sobra depois de acertar o duplo pedido é não ter plano B. Se a pessoa bloqueou no nível do sistema, o produto precisa de uma tela que explique como reverter — e, principalmente, de um **canal alternativo**. Na web, a Permissions API permite consultar o estado atual da permissão e ajustar a interface de acordo, em vez de continuar oferecendo um botão que não faz nada.

Isso importa porque bloquear é sinal de desconfiança, não de desinteresse momentâneo. A documentação do Chrome é explícita ao tratar bloqueio e aceite como as duas métricas que realmente contam, e ao interpretar o bloqueio como "não entendi o valor" ou "não confio neste site".

## O navegador já tomou partido

A web push acumulou tanto abuso que os navegadores passaram a intervir no próprio mecanismo de pedido.

O Chrome introduziu em 2020 a **interface silenciosa de permissão**: em vez do diálogo, um ícone discreto. Sites com taxa de aceite muito baixa são inscritos automaticamente nesse modo — e a inscrição é separada por tipo de dispositivo, porque o comportamento em celular e em desktop difere. O Firefox foi por caminho parecido, escondendo o pedido atrás de um ícone até haver interação. A regra prática é dura: **pedir permissão sem interação da pessoa deixou de funcionar, tecnicamente**.

Vale entender o que motivou isso, porque descreve o que não fazer. Os padrões que o Chrome classifica como abusivos incluem disfarçar o pedido de outra coisa (uma janela de chat, um aviso de cookie), condicionar o conteúdo do site ao aceite, e tentar contornar os mecanismos de prevenção existentes.

O Chrome distingue quatro respostas possíveis, e a distinção é útil para qualquer análise: **aceitar**, **bloquear**, **dispensar** (fechar o diálogo sem responder) e **ignorar** (não interagir; navegar para outro lugar conta como ignorar). Aceite e bloqueio são os dois que importam — dispensar e ignorar são desinteresse; bloquear é rejeição.

## O que muda em cada plataforma

O terreno é desigual e muda com frequência, então a arquitetura precisa aguentar variação.

**Android.** Desde a versão 8, cada notificação precisa pertencer a um **canal** declarado pelo app, e a pessoa configura som, vibração e visibilidade por canal, no sistema. Um detalhe de desenho importa muito: uma vez criado, o app **não pode aumentar** a importância de um canal — só a pessoa pode. Isso obriga a pensar a granularidade dos canais antes de publicar, porque errar aí é irreversível pelo lado de quem constrói. Desde a versão 13, o envio de notificação também exige uma permissão em tempo de execução (`POST_NOTIFICATIONS`), o que aproximou o Android do modelo do iOS.

**iOS.** Existe autorização provisória: o app começa entregando de forma discreta, direto na central e sem som, e a pessoa decide depois se promove ou desliga. É a materialização do "deixe experimentar antes de pedir". Existem também os níveis de interrupção — incluindo os que atravessam modos de foco — que devem ser tratados como o topo da pirâmide de prioridade, não como configuração padrão.

**Web.** É o terreno mais hostil: taxas de aceite historicamente muito abaixo das de aplicativo, prompt sujeito a supressão automática pelo navegador, e ausência de suporte em parte dos contextos (modo anônimo, por exemplo).

## Sobre os números de opt-in

Há muitos benchmarks circulando e eles discordam entre si — inclusive para o mesmo ano e a mesma plataforma. Convém tratá-los com desconfiança e usá-los só para ordem de grandeza.

O que sustenta as diferenças é metodológico: cada fornecedor mede a própria base de clientes, que não é uma amostra de nada; a definição de "opt-in" varia (proporção de instalações? de sessões? de quem chegou a ver o prompt?); e mudanças de plataforma deslocam a série inteira de um ano para o outro. Quando a Apple alterou o comportamento do prompt no iOS 18.2, os números de iOS mudaram de patamar sem que nenhum produto tivesse mudado nada.

O padrão que sobrevive a todas as fontes é este, e é o único que vale levar para uma discussão de projeto:

- Aplicativo nativo aceita **muito mais** que web push.
- Android historicamente aceita mais que iOS, por causa do histórico de inscrição automática — diferença que vem encolhendo desde o Android 13.
- A variação **entre categorias de app** é maior que a variação entre plataformas. Utilidade e produtividade aceitam mais; mídia e social, menos.

O que isso significa na prática é que benchmark externo serve para calibrar expectativa, não para definir meta. A comparação que interessa é com a sua própria série histórica, segmentada por onde e quando você pede.

## Consentimento não termina no aceite

O aceite de notificação é um caso particular de um problema maior, e vale herdar dele o vocabulário. Os princípios de consentimento consolidados pelo GDPR — e resumidos por Friedman a partir do trabalho de Claire Barrett — pedem que o consentimento seja ativo (nada pré-marcado), **granular** (um consentimento por finalidade), fácil de retirar a qualquer momento, separado dos termos de uso, e acompanhado da explicação do benefício.

Traduzido para notificação, isso quer dizer algo bem concreto: **um sim para "avise quando meu pedido chegar" não é um sim para "mande promoções"**. Empacotar os dois numa permissão só é a razão pela qual as pessoas desligam o canal inteiro — elas não têm como desligar apenas o que incomoda.

Daí uma decisão de arquitetura que precisa ser tomada cedo: os controles de preferência precisam existir **dentro do produto**, com granularidade por tipo de mensagem, e não apenas na tela de configurações do sistema. Friedman é direto quanto ao que acontece quando eles são difíceis de achar: as pessoas bloqueiam no nível do sistema operacional ou marcam como spam — desfechos dos quais é muito difícil voltar.

E há um princípio adjacente que se aplica bem aqui: coletar e pedir **just in time**, no momento em que a permissão é necessária e com a explicação ao lado. Pedir tudo na abertura é o equivalente, em permissão, ao formulário que pede vinte campos antes de mostrar qualquer valor.

## Um teste rápido

Antes de mostrar qualquer pedido, três perguntas:

1. **A pessoa já viu valor?** Se ela não usou o produto o suficiente para saber o que ele faz, o pedido é cedo demais.
2. **Existe uma primeira notificação concreta esperando?** Se você não consegue nomear a mensagem que vai chegar e quando, não peça ainda.
3. **O não custa caro?** Se recusar o seu pedido significa perder o canal para sempre, você está pedindo no lugar errado. Ponha uma pergunta sua na frente.

---

**Continua em:** [[Frequência, agrupamento e controle]] · [[Escrever a mensagem]]

**Antes:** [[Anatomia de um sistema de mensagens]] · [[A disciplina perdida do alarme]]
