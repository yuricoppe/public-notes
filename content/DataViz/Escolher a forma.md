---
title: "Escolher a forma"
description: "A hierarquia de precisão perceptual, as nove relações de dados do Financial Times, e as três situações em que o gráfico certo é não fazer gráfico"
tags:
  - tema/dataviz
  - tipo/artigo
---

A pergunta com que todo mundo começa — "que gráfico eu uso aqui?" — não tem resposta, porque falta a informação que a determina. A pergunta que tem resposta é outra: **que relação entre números eu preciso mostrar, e para quem?**

## O que o olho mede bem

Existe uma resposta empírica anterior a qualquer preferência estética. Em 1984, William Cleveland e Robert McGill publicaram um experimento que ordenou as tarefas perceptuais elementares — as operações que alguém executa ao extrair um valor de um gráfico — pela precisão com que as pessoas as executam.

![A hierarquia de precisão perceptual de Cleveland e McGill: posição em escala comum, posição em escalas não alinhadas, comprimento, ângulo, área, e por último volume, curvatura e cor](attachments/dataviz-hierarquia-perceptiva.svg)

A ordem, do mais preciso para o menos:

1. **Posição numa escala comum** — barras, linhas, dispersão
2. **Posição em escalas não alinhadas** — pequenos múltiplos
3. **Comprimento** — barras empilhadas
4. **Ângulo e inclinação** — pizza
5. **Área** — bolhas, treemap
6. **Volume, curvatura, cor** — mapas de calor, coropléticos

Vale ler essa lista pelo que ela é e não pelo que costumam fazer com ela. Não é uma proibição: é uma **tabela de custos**. Quanto mais baixo o nível, mais o gráfico depende de rótulo explícito para ser lido — e é por isso que mapa de calor sem número e pizza sem porcentagem quase sempre falham, enquanto os mesmos gráficos com rótulo funcionam.

A lista também explica por que a recomendação de painel do Nielsen Norman Group insiste em gráficos lineares: comprimento e posição em duas dimensões são processados **pré-atentivamente**, isto é, antes de a pessoa dirigir atenção consciente ao gráfico. Área não é. Volume muito menos. Em painel, onde o objetivo é entender o estado das coisas em segundos, essa diferença decide.

E há uma consequência direta e sem exceção: **nada de 3D, sombra ou perspectiva**. Perspectiva distorce comprimento e área — exatamente as duas coisas que o gráfico existe para comparar.

## Nove relações

Se a hierarquia diz o custo de cada codificação, o **Visual Vocabulary** do Financial Times diz por onde começar a escolha. Ele organiza os gráficos por **relação de dados**, não por aparência:

![As nove relações do Visual Vocabulary: desvio, correlação, ranking, distribuição, mudança no tempo, magnitude, parte e todo, espacial e fluxo](attachments/dataviz-vocabulario-visual.svg)

**Desvio** — quanto se afasta de uma referência: meta, zero, média. **Correlação** — se duas medidas andam juntas. **Ranking** — onde cada item fica em relação aos outros. **Distribuição** — o formato dos dados, onde se concentram e onde faltam. **Mudança no tempo** — tendência. **Magnitude** — comparação de tamanho, contagem e não taxa. **Parte e todo** — como um inteiro se divide. **Espacial** — só quando o lugar importa mais que qualquer outra coisa. **Fluxo** — volume e intensidade do movimento entre estados.

O ganho de trabalhar assim é que a escolha vira uma pergunta com resposta. "Preciso de um gráfico de vendas" não decide nada; "preciso mostrar como cada região se desvia da meta" já elimina oito das nove categorias e deixa três ou quatro gráficos candidatos.

Duas armadilhas que a categorização ajuda a evitar:

**Espacial é a mais escolhida pelo motivo errado.** Mapa é bonito e todo mundo entende que é um mapa. Mas mapa codifica dado em **área geográfica**, que não tem relação nenhuma com a grandeza mostrada — um estado enorme e vazio domina visualmente um estado pequeno e populoso. Só use mapa quando a pergunta for genuinamente sobre lugar. Se a pergunta é "onde é maior?", um ranking em barras responde melhor.

**Magnitude e ranking se confundem.** Se a pergunta é "quem é o maior?", ordene as barras. Se é "quanto cada um tem?", a ordem pode ser outra — alfabética, cronológica, a que a pessoa já conhece.

## Quando o gráfico é a resposta errada

A parte menos praticada da disciplina.

![Três casos em que gráfico é a resposta errada: uma barra sozinha, pizza de duas fatias, e gráfico para consultar valores exatos](attachments/dataviz-nao-e-grafico.svg)

**Um número só não é um gráfico.** Uma barra sozinha não tem com o que ser comparada — o comprimento não codifica nada, porque não há segundo comprimento. O componente certo é um cartão com o número grande e o rótulo embaixo.

**Duas fatias não são uma pizza.** Pedir que alguém compare dois ângulos para descobrir algo que uma frase resolve — "68% renovaram; um em cada três saiu" — é gastar a codificação mais imprecisa da lista no caso mais fácil que existe.

**Gráfico não serve para consultar.** Este é o mais importante e o mais violado. A pergunta que antecede tudo é se a pessoa vem **perceber um padrão** ou **consultar um valor**. Padrão pede gráfico; consulta pede tabela. Quando alguém precisa saber quanto exatamente foi o faturamento de março, uma barra é um obstáculo entre ela e o número — ela vai ter que passar o mouse, ler o tooltip e confiar. Uma tabela responde direto, é ordenável e dá para copiar.

Muito painel ruim nasce de tentar atender aos dois com o mesmo componente. A saída costuma ser oferecer os dois: o gráfico para ver a forma, a tabela logo abaixo para ler o número — o que, de quebra, resolve boa parte do problema de [[Acessibilidade em dataviz|acessibilidade]].

## Uma sequência que funciona

1. **Escreva a frase** que o gráfico precisa provar. Se ela não existe, o gráfico não tem trabalho a fazer.
2. **Identifique a relação** — qual das nove.
3. **Escolha a codificação mais alta da hierarquia** que dê conta dessa relação.
4. **Pergunte se é mesmo um gráfico** — cartão, frase ou tabela podem ser melhores.
5. **Só então** pense em cor, que é o assunto de [[Cor em gráfico]].

O passo 1 é o que mais economiza tempo, porque frequentemente revela que não há nada a mostrar. Um gráfico sem afirmação é um gráfico decorativo — e decoração em painel custa atenção de alguém que estava tentando decidir algo.

---

**Continua em:** [[Cor em gráfico]] · [[Como um gráfico mente]] · [[Tabelas e painéis]]
