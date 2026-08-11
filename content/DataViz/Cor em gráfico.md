---
title: "Cor em gráfico"
description: "Os quatro trabalhos que a cor faz, por que conferir daltonismo no olho não funciona, e o número que separa duas cores de verdade"
tags:
  - tema/dataviz
  - tema/acessibilidade
  - tipo/artigo
---

Cor é a última decisão de um gráfico e quase sempre é a primeira. A inversão é cara porque cor não é acabamento: é uma **codificação de dado**, com regras diferentes conforme o trabalho que ela está fazendo.

## Os quatro trabalhos

Antes de escolher qualquer tom, decida qual dos quatro se aplica. Cada um tem uma regra e elas não se misturam.

**Identidade (categórica).** Cores diferentes para coisas diferentes — produtos, times, regiões. Sem ordem entre elas. A regra: uma ordem fixa de cores, atribuída à **entidade**, nunca à posição. Se um filtro remove uma série e as que sobram trocam de cor, quem aprendeu "a região Sul é azul" foi enganado.

**Magnitude (sequencial).** Uma quantidade que cresce. A regra: **uma cor só, do claro ao escuro.** Arco-íris para magnitude é o erro mais comum de mapa de calor e de coroplético, e o motivo é simples — matiz não tem ordem natural. Ninguém sabe dizer se verde é mais ou menos que laranja sem consultar a legenda a cada célula.

**Polaridade (divergente).** Algo que vai para os dois lados a partir de um meio — acima e abaixo da meta, ganho e perda. A regra: **duas cores opostas em temperatura e um cinza neutro no meio.** Azul e vermelho funcionam; azul e turquesa não, porque as duas são frias e o gráfico perde o sentido de oposição. E o ponto médio precisa ser neutro: uma cor no meio faz o "nada acontecendo" parecer alguma coisa.

**Estado (semântica).** Bom, atenção, grave, crítico. A regra: essas cores são **reservadas**. Se vermelho significa erro no seu produto, ele não pode ser também a cor da série 4 no gráfico ao lado. E estado nunca vai só na cor — vai com ícone e com palavra.

## Por que conferir no olho não funciona

Aqui está a parte que mais muda a prática. Existe um número que diz se duas cores se separam de verdade, e ele é calculável.

![Vermelho e verde comparados com azul e laranja, em visão normal e simulados para deuteranopia, com as distâncias perceptuais calculadas](attachments/dataviz-daltonismo.svg)

O par vermelho-e-verde é o mais usado do mundo para "bom e ruim". Em visão normal, a distância perceptual entre `#e03131` e `#2f9e44` é **32,5** — praticamente o máximo, cores absolutamente distintas. Simulados para deuteranopia, os mesmos dois viram `#938429` e `#93874b`: distância **3,0**. Isto é, a mesma cor. Não parecida — a mesma.

O par azul-e-laranja, com a mesma checagem, mantém **28,5** sob simulação de protanopia. Continua legível.

A régua prática: acima de 8 duas cores se separam; abaixo disso não dá para contar com elas. E o ponto que interessa não é decorar pares bons — é que **essa conta existe e leva segundos**. Não há motivo para adivinhar. Simuladores de daltonismo e verificadores de contraste são gratuitos, e o próprio Datawrapper passou a checar a paleta automaticamente.

Vale notar que os números acima foram calculados, não estimados, usando as matrizes de simulação de Machado e colegas (2009) — as mesmas que os simuladores usam por baixo.

## A regra que resolve sem calculadora

Lisa Charlotte Muth, do Datawrapper, resume numa frase que serve de teste de bolso: **acerte em preto e branco.** Se o gráfico continua legível impresso em escala de cinza, ele funciona para leitores daltônicos.

O motivo é que a maior parte dos problemas de daltonismo é de **matiz**, não de luminosidade. Pares que quebram são os que têm brilho parecido: vermelho e verde, laranja e verde, amarelo e rosa, azul e verde. Se as cores diferem bastante em claro-escuro, a distinção sobrevive.

Daí as recomendações concretas que ela dá:

- **Azul com laranja ou vermelho** é a combinação mais segura para duas cores. Azul é a cor percebida de forma mais parecida por todos os tipos de visão.
- **Evite verde com laranja, verde com vermelho e verde com azul** na mesma luminosidade.
- **Limite a três ou quatro cores** de identidade. Além disso, mesmo com visão típica, adjacentes começam a se embaralhar.
- **Destaque só o que importa** — uma série na cor, o resto em cinza — em vez de dar cor a tudo.

## O que fazer além da cor

Nenhuma paleta resolve sozinha. A saída é **redundância**: o dado codificado em mais de um canal.

- **Rótulo direto** na ponta da linha ou da barra, eliminando a dependência da legenda. É a solução mais forte e a menos usada.
- **Forma** — círculo, triângulo, quadrado — em dispersão e em séries de linha.
- **Padrão** — listras, pontos, hachura — em áreas. Com moderação: padrão denso cansa e pode causar desconforto vestibular.
- **Traço** — cheio, tracejado, pontilhado; espessura diferente.
- **Posição e ordem**, que não dependem de percepção de cor nenhuma.

Sarah Fossheim acrescenta duas advertências que não são sobre daltonismo e são igualmente importantes: **cores muito vivas cansam a vista** e podem provocar desconforto sensorial, especialmente em painéis densos; e **contraste baixo** derruba a legibilidade para todo mundo. Gráfico não é lugar para saturação máxima.

## Uma lista de verificação

- [ ] Sei qual dos quatro trabalhos a cor está fazendo neste gráfico
- [ ] Sequencial usa uma cor só, do claro ao escuro
- [ ] Divergente tem duas temperaturas opostas e cinza no meio
- [ ] A cor pertence à entidade, não à posição no ranking
- [ ] As cores de estado não estão sendo usadas como identidade
- [ ] Rodei um simulador de daltonismo — não confiei no olho
- [ ] O gráfico sobrevive em escala de cinza
- [ ] Existe um segundo canal além da cor: rótulo, forma, padrão ou posição
- [ ] Contraste conferido: 4,5:1 para texto, 3:1 para elementos gráficos
- [ ] O modo escuro tem paleta própria, e não a mesma invertida

O último item costuma passar batido. Modo escuro não é o modo claro com as cores trocadas: o contraste contra o fundo muda, e uma paleta que passava no claro pode falhar no escuro. São duas checagens, não uma.

---

**Antes:** [[Escolher a forma]] · **Continua em:** [[Como um gráfico mente]] · [[Acessibilidade em dataviz]]
