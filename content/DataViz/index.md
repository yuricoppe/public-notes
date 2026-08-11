---
title: "DataViz"
description: "Índice das anotações sobre visualização de dados: os cinco artigos, as fontes com a pesquisa por trás de cada regra, e as ferramentas"
tags:
  - tema/dataviz
  - tipo/indice
aliases:
  - "DataViz"
---

Esta pasta reúne o que estudei sobre **visualização de dados** — a parte que decide se um gráfico informa, não informa ou informa errado.

O fio que atravessa os cinco artigos é que quase toda regra de dataviz tem pesquisa medida por trás, e que a maior parte das discussões de gosto some quando alguém traz o número. Onde a evidência é ambígua — e há casos importantes — está dito que é ambígua.

## Comece por aqui

**[[Escolher a forma]]** — a hierarquia de precisão perceptual de Cleveland e McGill, as nove relações de dados do Visual Vocabulary, e as três situações em que o gráfico certo é não fazer gráfico.

**[[Cor em gráfico]]** — os quatro trabalhos que a cor faz, por que conferir daltonismo no olho não funciona (com as distâncias calculadas), e a regra de acertar em preto e branco.

**[[Como um gráfico mente]]** — eixo truncado, eixo invertido, dois eixos verticais, área — com o que a pesquisa mediu de cada um, incluindo o achado de que marcar a quebra do eixo **não** desfaz a distorção.

**[[Acessibilidade em dataviz]]** — as seis camadas de um gráfico acessível, o que a auditoria dos painéis eleitorais de 2024 encontrou, e as técnicas que a Apple usa e quase ninguém copia.

**[[Tabelas e painéis]]** — quando tabela é melhor que gráfico, como ela sobrevive à tela pequena, e por que a maioria dos painéis é uma lista de gráficos sem pergunta.

**[[20 ideias para gráficos melhores]]** — leitura anotada da lista mais compartilhada da área: os vinte itens, a pesquisa por trás de cada um, as duas correções que ele merece e as quatro coisas que a lista não cobre.

## Fontes

Todas verificadas em 11 ago 2026.

### A base perceptual

- **[Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods](https://www.tandfonline.com/doi/abs/10.1080/01621459.1984.10478080)** · William Cleveland e Robert McGill, *Journal of the American Statistical Association*, 1984
  O experimento que ordenou as tarefas perceptuais por precisão: posição em escala comum, posição em escalas não alinhadas, comprimento, ângulo, área, volume e cor. É a base empírica de quase toda escolha de gráfico feita desde então. Pago; o achado principal circula amplamente.

- **[Dashboards: Making Charts and Graphs Easier to Understand](https://www.nngroup.com/articles/dashboards-preattentive/)** · Page Laubheimer, Nielsen Norman Group, 2017
  Processamento pré-atentivo aplicado a painel: por que comprimento e posição funcionam em segundos e área não, e por que pizza, rosca, treemap e 3D são escolhas ruins nesse contexto específico.

- **[Choosing Chart Types: Consider Context](https://www.nngroup.com/articles/choosing-chart-types/)** · Nielsen Norman Group
  A pergunta que antecede a escolha: qual é o objetivo, que ponto se quer fazer, que ação se espera de quem lê.

- **[Visual Vocabulary](https://ft-interactive.github.io/visual-vocabulary/)** · Financial Times
  O mapa de qual gráfico para qual relação de dados, organizado em nove categorias — desvio, correlação, ranking, distribuição, mudança no tempo, magnitude, parte e todo, espacial e fluxo. A referência mais direta quando bate a dúvida. O [pôster e os arquivos-fonte](https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary) estão no repositório do Chart Doctor.

- **[Data Viz Project](https://datavizproject.com/)** · datavizproject.com
  Catálogo de tipos de visualização, útil para descobrir formas que não vêm à cabeça.

### Cor

- **[How your colorblind and colorweak readers see your colors](https://www.datawrapper.de/blog/colorblindness-part1)** · Lisa Charlotte Muth, Datawrapper, 2020
  A primeira de uma série de três. Explica o que acontece na percepção e por que a intuição de quem enxerga cores falha aqui.

- **[What to consider when visualizing data for colorblind readers](https://www.datawrapper.de/blog/colorblindness-part2)** · Lisa Charlotte Muth, Datawrapper, 2020
  A parte acionável: azul com laranja ou vermelho é o par mais seguro; evitar verde com laranja, verde com vermelho e verde com azul na mesma luminosidade; limitar a três ou quatro cores; e a regra de bolso que resolve a maior parte dos casos — **acerte em preto e branco**.

- **[What's it like to be colorblind](https://www.datawrapper.de/blog/colorblindness-part3)** · Datawrapper
  Relatos em primeira pessoa. É a parte que muda a atitude, não a técnica.

- **[Datawrapper now checks your colors, so you don't have to](https://www.datawrapper.de/blog/colorblind-check)** · Datawrapper
  A verificação automática embutida na ferramenta — e o argumento de que isso não deveria ser opcional.

- **[How to pick more beautiful colors for your data visualizations](https://www.datawrapper.de/blog/beautifulcolors)** · Lisa Charlotte Muth, Datawrapper
  Sobre a parte estética, que também existe: saturação, matizes vizinhos, cinzas que não parecem sujos.

- **[Machado, Oliveira & Fernandes, 2009](https://www.inf.ufrgs.br/~oliveira/pubs_files/CVD_Simulation/CVD_Simulation.html)** · UFRGS
  O modelo de simulação de deficiência de visão de cores que a maioria das ferramentas usa por baixo. As cores simuladas no diagrama do artigo de cor foram calculadas com essas matrizes.

### Como um gráfico engana

- **[Truncating the Y-Axis: Threat or Menace?](https://arxiv.org/abs/1907.02035)** · Michael Correll, Enrico Bertini e Steven Franconeri, CHI 2020
  O trabalho mais útil sobre truncamento, e o mais desconfortável: marcar a quebra do eixo — símbolo de corte, barras interrompidas — **não** reduz o exagero percebido, porque o julgamento de magnitude é visual e não aritmético. E os autores recusam a regra de sempre incluir o zero, defendendo que a escala deve derivar de qual diferença importa naquele domínio.

- **How Deceptive are Deceptive Visualizations?** · Anshul Vikram Pandey e colegas, CHI 2015
  Estudo com 330 participantes sobre duas famílias de distorção — exagero e reversão de mensagem — confirmando que o efeito existe e é grande. Inclui o caso do eixo invertido, que não exagera a conclusão: inverte.

- **The Visual Display of Quantitative Information** · Edward Tufte, 1983 · livro
  A origem de *chartjunk* e da proporção tinta-dado. Continua sendo o melhor conselho de primeira passada — com a ressalva, levantada por pesquisa posterior, de que gráfico completamente despido nem sempre é o mais memorável para público amplo.

### Acessibilidade

- **[Sarah L. Fossheim — artigos sobre dataviz](https://fossheim.io/writing/tag/dataviz/)** · fossheim.io
  A melhor fonte única desta lista. Sete artigos, de 2020 a 2024, que combinam princípio e auditoria concreta:

  - **[An intro to designing accessible data visualizations](https://fossheim.io/writing/posts/accessible-dataviz-design/)** (2020) — os dez do's and don'ts, incluindo dois raramente citados: cores muito vivas cansam e causam desconforto sensorial, e informação escondida atrás de interação exclui celular, teclado e leitor de tela.
  - **[Dataviz accessibility principles, demonstrated by the 2024 presidential election dashboards](https://fossheim.io/writing/posts/2024-dataviz-a11y-elections)** (2024) — a auditoria de nove veículos, com os erros nomeados um a um. Um painel com 870 problemas. A conclusão sobre o que isso diz do processo é a parte mais importante.
  - **[Dataviz accessibility review: the Norwegian 2023 election graphs](https://fossheim.io/writing/posts/dataviz-accessibility-review-norwegian-elections-2023)** (2023)
  - **[What we can learn from Apple's dataviz accessibility](https://fossheim.io/writing/posts/apple-health-dataviz-a11y)** (2021) — o catálogo positivo: navegação estruturada, rótulo que carrega o contexto do eixo, gráficos sonoros, resumo em texto acima do gráfico.
  - **[How to create a screen reader accessible graph like Apple's with D3.js](https://fossheim.io/writing/posts/apple-dataviz-a11y-tutorial)** (2021) — o tutorial técnico correspondente.
  - **[An introduction to accessible data visualizations with D3.js](https://fossheim.io/writing/posts/accessible-dataviz-d3-intro)** (2020)
  - **[How (not) to make accessible data visualizations, illustrated by the US presidential election](https://fossheim.io/writing/posts/accessible-dataviz-us-elections)** (2020) — a auditoria de 2020, que serve de linha de base para comparar com a de 2024. Quase nada mudou entre as duas.

- **[Chartability](https://chartability.fizz.studio/)** · Frank Elavsky
  Cerca de cinquenta heurísticas em forma de perguntas testáveis, em sete princípios: os quatro do WCAG mais **comprometedor, assistivo e flexível**. Aplicável a artefato de qualquer maturidade — inclusive a um desenho em Figma, antes de existir código.

- **[Mobile Tables: Comparisons and Other Data Tables](https://www.nngroup.com/articles/mobile-tables/)** · Nielsen Norman Group
  Travar cabeçalho e primeira coluna, e deixar a pessoa escolher um subconjunto das colunas, é o que torna tabela grande usável em tela pequena.

### Prática e inspiração

- **[Datawrapper Blog](https://www.datawrapper.de/blog)** · Datawrapper
  Recursos novos e a série Weekly Charts. A [seção de cor](https://www.datawrapper.de/blog/category/color-in-data-vis) sozinha vale a assinatura do feed.

- **[20 ideas for better data visualization](https://uxdesign.cc/20-ideas-for-better-data-visualization-73f7e3c2782d)** · Taras Bakusevych, UX Collective, 2021
  A lista de verificação mais compartilhada da área. Destrinchada item por item em [[20 ideias para gráficos melhores]].

- **[Designing user-friendly data tables for mobile devices](https://medium.com/design-bootcamp/designing-user-friendly-data-tables-for-mobile-devices-c470c82403ad)** · Bootcamp

- **[The Pudding](https://pudding.cool/)** · pudding.cool
  Ensaios visuais. Vale menos como referência de técnica e mais para ver o que acontece quando a visualização é o argumento, e não a ilustração do argumento.

## Vídeo

- **[Explore Explain](https://www.youtube.com/channel/UCIPsLvCpZYwvSurkb1DLLZg)** · Andy Kirk · canal e podcast
  O melhor material em vídeo sobre dataviz que encontrei. Cada episódio é uma conversa longa — 50 a 60 minutos — com quem fez **uma** visualização específica, destrinchando as decisões pequenas por trás dela. Nove episódios por temporada, seis temporadas até agora, com convidados como Cole Nussbaumer Knaflic. Informações e lista de episódios em [visualisingdata.com/podcast](https://visualisingdata.com/podcast/).

- **[Tracking COVID-19 with the Financial Times](https://www.youtube.com/watch?v=FASGCbN5jXs)** · John Burn-Murdoch · CIVICA Data Science Seminar
  O chefe de dados do FT sobre os gráficos de pandemia — escala logarítmica, alinhamento por dia zero, e as decisões editoriais por trás de gráficos vistos por milhões. Há também a [conversa no Explore Explain](https://www.youtube.com/watch?v=rplwvdOmKKc) sobre o mesmo projeto.

- **[Clutter-Free Charts](https://www.nngroup.com/videos/chartjunk/)** e **[Data Visualizations for Dashboards](https://www.nngroup.com/videos/data-visualizations-dashboards/)** · Nielsen Norman Group
  Curtos e diretos, bons para mandar para quem não vai ler um artigo.

- **[Storytelling with Data](https://www.youtube.com/@storytellingwithdata)** · Cole Nussbaumer Knaflic · canal
  Foco em contexto, remoção de ruído e direcionamento de atenção com atributos pré-atentivos. Mais voltado a apresentação de negócio do que a produto, e útil justamente por isso.

## Ferramentas

- **[Datawrapper](https://www.datawrapper.de/)** — gráficos para publicação, com verificação de daltonismo embutida.
- **[Coblis](https://www.color-blindness.com/coblis-color-blindness-simulator/)** e **[Color Oracle](https://colororacle.org/)** — simuladores de deficiência de visão de cores.
- **[Viz Palette](https://projects.susielu.com/viz-palette)** · Susie Lu — testa uma paleta em contextos reais de gráfico e sob simulação.
- **[ColorBrewer](https://colorbrewer2.org/)** — paletas sequenciais, divergentes e qualitativas com filtro de segurança para daltonismo e para impressão.

## Relacionados

[[UX Healthcare/Visualização de dados em saúde|Visualização de dados em saúde]] · [[Dashboard]] · [[Análise de Dados]] · [[Acessibilidade/index|Acessibilidade]] · [[Design System/index|Design System]]

---
