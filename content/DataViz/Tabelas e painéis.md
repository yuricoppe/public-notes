---
title: "Tabelas e painéis"
description: "Quando tabela é melhor que gráfico, como ela sobrevive à tela pequena, e por que a maior parte dos painéis é uma lista de gráficos sem pergunta"
tags:
  - tema/dataviz
  - tipo/artigo
---

Tabela é o componente de visualização de dados menos glamouroso e mais usado. Painel é o mais construído e o menos avaliado. Os dois compartilham a mesma origem de problema: são montados a partir do que o sistema tem para mostrar, e não a partir da pergunta de quem chega.

## Tabela não é o prêmio de consolação

A tabela é a forma certa quando a pessoa precisa **consultar um valor**, comparar itens em várias dimensões ao mesmo tempo, ou levar o dado embora. Gráfico responde "qual é a forma disso"; tabela responde "quanto exatamente é isso".

O que faz uma tabela funcionar é pouca coisa e quase sempre falta:

**Números alinhados à direita, com a mesma quantidade de casas.** É o que permite comparar magnitude pela largura do número, sem ler. Texto à esquerda, número à direita — e dígitos de largura fixa, para as colunas de fato alinharem.

**Cabeçalho que gruda.** Rolar dez linhas e não saber mais de que coluna é o número é o defeito número um de tabela longa.

**Zebra ou linha divisória, não os dois.** Escolha um mecanismo de separação e mantenha-o discreto. Grade completa em torno de cada célula é ruído.

**Ordenação em toda coluna que faça sentido ordenar** — e um indicador visível de por qual coluna está ordenado agora. Tabela ordenável sem indicador de estado engana.

**Unidade no cabeçalho, não em cada célula.** "Receita (R$ mil)" uma vez, em vez de "R$" repetido duzentas vezes.

E um recurso subestimado: **barras dentro da célula**. Uma barra fininha atrás do número dá a leitura de magnitude sem tirar a precisão — a tabela passa a responder às duas perguntas ao mesmo tempo. É o caso raro em que não é preciso escolher entre gráfico e tabela.

## Tela pequena

![Três padrões para tabela grande em tela pequena: fixar e rolar, escolher colunas, e transformar linha em cartão](attachments/dataviz-tabela-mobile.svg)

O Nielsen Norman Group testou tabelas de comparação em celular, e a recomendação central é uma combinação: **travar o cabeçalho e a primeira coluna, e deixar a pessoa escolher um subconjunto das colunas.**

O travamento resolve a desorientação — sem ele, ao rolar na horizontal, a pessoa perde de qual linha é o valor que está vendo. A escolha de colunas resolve o volume: uma tabela de onze colunas não cabe em nenhuma tela pequena, e a pessoa normalmente só quer três delas.

O terceiro padrão — **cada linha vira um cartão** — é o mais adotado e o menos examinado. Ele torna cada registro legível e **destrói a comparação**, que costuma ser a razão de existir da tabela: os preços deixam de estar alinhados numa coluna que dá para varrer. Às vezes é a escolha certa, quando a tarefa é olhar um item por vez. Quando a tarefa é comparar, é uma regressão disfarçada de responsividade.

Nos três casos, uma condição não negociável: continua sendo **tabela de verdade na marcação**, com cabeçalho associado às células. Tabela feita de `div` é invisível para quem usa leitor de tela, independentemente de como parece.

## Painéis

Quase todo painel ruim tem a mesma origem: foi montado a partir dos dados disponíveis, e não de uma pergunta. O sintoma é reconhecível — doze gráficos, nenhum com título que afirme alguma coisa, e ninguém no time consegue dizer qual decisão o painel apoia.

O que ajuda:

**Uma pergunta por painel.** Se são três perguntas diferentes, são três painéis ou três abas. "Visão geral" não é pergunta.

**Títulos que afirmam.** "Conversão caiu 8% desde a mudança de checkout" trabalha; "Conversão" não. O título é onde mora a informação que a pessoa vai levar embora.

**Codificação linear.** Barra, linha, dispersão. Painel é lido em segundos, e comprimento e posição são as únicas codificações processadas pré-atentivamente — a recomendação do NN/g de evitar pizza, rosca e treemap em painel vem daí, não de gosto.

**Um filtro para tudo.** Uma faixa de filtros acima, que reescala todos os gráficos. Filtro dentro de cada cartão produz painéis cujos números não conversam entre si — e ninguém percebe que está comparando períodos diferentes.

**Sem rolagem, se possível.** O que exige rolar não faz parte do panorama; faz parte do detalhe, e detalhe tem outro lugar.

**A tabela embaixo.** Gráfico para ver a forma, tabela para ler o valor. Resolve a tarefa de consulta e resolve boa parte da acessibilidade de uma vez.

## Duas coisas a cortar

**Comparação sem referência.** "1.284 pedidos" não informa nada sozinho. Comparado com o período anterior, com a meta ou com a média, vira informação. Todo número em painel merece a pergunta "comparado com o quê?".

**Precisão falsa.** "R$ 1.284.937,42" num cartão de panorama. Ninguém decide nada com os centavos, e eles custam a legibilidade dos dígitos que importam. "R$ 1,28 mi" comunica o mesmo e é lido mais rápido — a precisão inteira mora na tabela, para quem precisar dela.

---

**Antes:** [[Escolher a forma]] · [[Acessibilidade em dataviz]]

**Ver também:** [[Dashboard]] · [[Análise de Dados]]
