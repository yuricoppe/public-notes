---
title: "O que é e quando não vale a pena"
description: "As definições que os times confundem, o que um design system realmente custa, e as situações em que construir um é a decisão errada"
tags:
  - tema/design-system
  - tipo/artigo
---

Quase toda discussão sobre design system começa errada porque quatro palavras diferentes estão sendo usadas como sinônimo. Vale gastar dois minutos separando-as, porque a confusão não é semântica — ela leva times a acharem que já têm um sistema quando têm um arquivo, e a acharem que precisam de um quando precisam de uma paleta.

## As quatro coisas

![Diagrama mostrando que o design system contém guia de estilo, biblioteca de componentes e biblioteca de padrões, e que o que o distingue dos três é ter um time e um processo de decisão](attachments/design-system-vocabulario.svg)

Therese Fessenden, do Nielsen Norman Group, define **design system** como um conjunto completo de padrões destinado a gerir design em escala, por meio de componentes e padrões reutilizáveis. As outras três palavras nomeiam partes dele:

**Guia de estilo** cobre marca, cor, tipografia, tom de voz e as normas de interação. Diz como as coisas parecem.

**Biblioteca de componentes** guarda os elementos de UI reutilizáveis, com nome, descrição, atributos, estados e trechos de código. Diz do que as coisas são feitas.

**Biblioteca de padrões** guarda agrupamentos e arranjos maiores: estruturas de conteúdo, templates, o formulário, o checkout, a página de erro. Diz como as peças se juntam.

E há um quarto item na lista da NN/g que costuma ser lido como detalhe operacional e é, na verdade, o que define a categoria: **um time dedicado**, com pelo menos um designer de interação, um designer visual e uma pessoa de desenvolvimento.

É essa faixa que separa acervo de sistema. Um conjunto de arquivos bem organizados sem ninguém responsável por mantê-lo é uma biblioteca — útil, mas que começa a apodrecer no dia seguinte à publicação. Vira sistema quando existe alguém encarregado e um caminho conhecido para mudá-lo.

## O que ele custa

A conversa sobre benefício é fácil e já foi feita mil vezes: consistência, velocidade, uma linguagem comum entre times, e liberar tempo de design para problemas que não são "como é o botão".

Há dados quantitativos, e vale citá-los com a ressalva de que quase todos vêm de quem vende ferramenta ou serviço. A Figma reporta que designers usando design system completaram tarefas 34% mais rápido; a Vanguard, atualizações de design 50% mais rápidas; a Headspace, economia de 20% a 30% em tarefas simples e até 50% em projetos complexos. Números assim servem para conseguir orçamento e para pouco mais — nenhum deles é replicável nem controlado.

O custo é menos discutido e mais previsível:

**Manutenção contínua, por gente dedicada.** Não é um projeto que termina. A pesquisa da Sparkbox de 2022 encontrou que quase 80% dos sistemas considerados bem-sucedidos eram mantidos por um time parcial ou totalmente dedicado — não por uma ferramenta, não pelas horas vagas de quem tiver disponibilidade.

**Tempo de treinar as pessoas.** Que é o custo mais subestimado de todos, e o assunto de [[Adoção e maturidade]].

**Resistência organizacional**, especialmente onde cada projeto é tratado como peça única.

Um sintoma que aparece cedo: na mesma pesquisa da Sparkbox, **dívida técnica** era o maior desafio relatado (43%) enquanto era prioridade para apenas 31%. A distância entre as duas colunas é o retrato de um time que sabe do problema e não consegue chegar nele.

## Quando não vale a pena

A recomendação da NN/g é direta e vale repetir porque quase nunca é levada a sério: design systems compensam quando a organização antecipa **anos** de trabalho de design replicável em escala. Não servem para provas de conceito nem para iniciativas de curto prazo. O retorno melhora com escala organizacional e produção sustentada ao longo do tempo.

Traduzido em situações concretas, construir um design system é a decisão errada quando:

**Existe um produto só, com um time só.** O que se ganha aqui é organização de arquivo, não sistema. Faça a biblioteca de componentes, pule a governança, e não chame de design system — porque o nome traz junto uma expectativa de processo que ninguém vai sustentar.

**A linguagem visual ainda não estabilizou.** Sistematizar antes de decidir é congelar uma resposta provisória e depois pagar para descongelar. A ordem certa é o contrário: repetir até saber o que se repete.

**Não há quem mantenha.** Um sistema sem dono é pior do que não ter sistema, porque ele acumula autoridade sem acumular cuidado. Times passam a seguir uma coisa desatualizada porque ela está escrita.

**O problema real é outro.** Inconsistência costuma ser sintoma. Quando a causa é que cinco times não se falam, ou que não há critério de qualidade, ou que ninguém revisa nada, o design system vira o lugar onde essa disfunção é reencenada — só que agora com um repositório no meio.

Há um teste simples e desconfortável: se o sistema fosse publicado hoje, quem seria o responsável por responder à primeira pergunta que chegasse na semana que vem? Se não há um nome, ainda não é hora.

## O sistema é um produto

O enquadramento que resolve boa parte dos problemas seguintes é tratar o design system como produto, com as consequências completas disso: tem roadmap, backlog, dono, orçamento e — o mais esquecido — **clientes**, que são os times internos.

Isso muda o que conta como sucesso. Um sistema não é bom porque tem muitos componentes. É bom porque os times conseguem usá-lo, confiam nele e voltam. Um sistema completo e ignorado falhou; um sistema pequeno e adotado funcionou.

Brad Frost fecha um texto sobre arquitetura de design systems com a frase que resume o assunto melhor do que qualquer diagrama: design systems são menos sobre ativos e a relação entre eles, e mais sobre pessoas e a relação entre elas.

## Por onde começar, se for começar

Duas ideias que sobrevivem ao contato com a realidade:

**Comece pelo que já se repete, não pelo que seria bom ter.** Um inventário de interface — sair capturando tudo que existe hoje e agrupando o que é a mesma coisa com aparências diferentes — dá tanto a lista inicial quanto o argumento para o orçamento. É difícil defender um sistema em abstrato e fácil defender dezessete tipos de botão numa mesma tela.

**Deixe o sistema ser simples pelo tempo que der.** A Lei de Gall, que Frost usa para enquadrar a arquitetura em camadas: um sistema complexo que funciona invariavelmente evoluiu de um sistema simples que funcionava. A complexidade se acrescenta quando aparece a necessidade real, e não antes — o que é o assunto de [[A anatomia em camadas]].

---

**Continua em:** [[A anatomia em camadas]] · [[Governança e contribuição]] · [[Adoção e maturidade]]

**Ver também:** [[Tokens]] · [[Glossário/Entregáveis/design_system|Design System (Glossário)]]
