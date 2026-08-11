---
title: "20 ideias para gráficos melhores"
description: "Leitura anotada do artigo de Taras Bakusevych — as vinte recomendações, o que a pesquisa acrescenta a cada uma, onde ele acerta contra o senso comum e o que a lista deixa de fora"
tags:
  - tema/dataviz
  - tipo/artigo
---

*[20 ideas for better data visualization](https://uxdesign.cc/20-ideas-for-better-data-visualization-73f7e3c2782d)*, de Taras Bakusevych, saiu na UX Collective em agosto de 2021 e virou a lista de verificação mais compartilhada da área. São sete minutos de leitura, cada item ilustrado com um par certo-e-errado, e a maior parte do que ele diz está correta.

Esta página existe porque uma lista de sete minutos não mostra de onde as regras vêm — e sem isso não dá para saber quais são leis, quais são convenções e quais têm exceção. O que segue é o artigo inteiro, item por item, com a pesquisa por trás de cada um e as poucas discordâncias que tenho.

![Mapa das 20 ideias agrupadas em oito temas, e o que a lista não cobre: incerteza, tabela, teclado e leitor de tela, e teste](attachments/dataviz-20-ideias-cobertura.svg)

## Forma

**1. Escolha o tipo de gráfico certo.** O argumento é que cair no gráfico mais comum por inércia confunde ou induz a erro, e que o mesmo conjunto de dados admite muitas representações conforme o que a pessoa quer ver. A recomendação prática dele é começar sempre pela revisão do conjunto de dados e por entrevista com quem vai usar.

É a base de [[Escolher a forma]], e o diagrama que acompanha esse item — as quatro perguntas, cada tipo com seu glifo — está redesenhado lá. O que a pesquisa acrescenta é a ordem de precisão de Cleveland e McGill: posição numa escala comum é o que o olho mede melhor, e cor e volume o que ele mede pior. Isso transforma "escolha o certo" em algo verificável.

## Eixos e escalas

É o tema mais forte da lista, e onde ela é mais útil.

**2. Plote negativos e positivos em lados opostos da linha de base.** Numa barra horizontal, negativo à esquerda, positivo à direita. Parece óbvio e é violado com frequência em ferramenta de BI, que às vezes empilha os dois do mesmo lado.

**3. Barra sempre começa no zero.** O exemplo dele é bom: com eixo truncado, a barra B parece mais de três vezes maior que a D, quando a diferença real é bem menor.

**4. Linha usa escala adaptativa.** E aqui está o acerto mais importante do artigo inteiro. Ele **não** aplica a regra do zero às linhas: forçar o zero numa linha frequentemente deixa o gráfico achatado, e como o objetivo da linha é mostrar tendência, a escala deve se adaptar ao conjunto — mantendo a linha ocupando cerca de dois terços da altura.

![Comparação mostrando que barra precisa começar no zero, porque codifica quantidade por comprimento, e que linha não precisa, porque codifica variação e o zero a achata](attachments/dataviz-20-barra-e-linha.svg)

Essa distinção entre barra e linha é o que separa um guia bom de um guia de senso comum. A barra codifica quantidade por **comprimento**, e cortar o comprimento quebra a codificação. A linha codifica **variação**, e o zero muitas vezes é irrelevante.

Vale acrescentar o que a pesquisa mostrou depois, porque complica tudo: Correll, Bertini e Franconeri testaram os remédios usuais para truncamento — símbolo de corte no eixo, barras visivelmente interrompidas — e descobriram que **marcar a quebra não desfaz o exagero percebido**. Julgamento de magnitude é visual, não aritmético. E os autores recusam a regra absoluta de incluir sempre o zero, defendendo que a escala deve derivar de qual diferença importa naquele domínio. É o assunto de [[Como um gráfico mente]].

**7. Evite eixo duplo.** Ele nota que a tentação vem de economizar espaço quando há duas séries da mesma medida com magnitudes diferentes, e que o resultado é uma comparação enganosa, porque quase ninguém confere as escalas — a pessoa varre e conclui.

Concordo inteiramente, e acrescento o motivo formal: o alinhamento entre as duas escalas é **arbitrário**. Quem monta o gráfico decide onde as duas linhas se cruzam, e a correlação aparente muda se alguém mexer no máximo de um dos eixos. As saídas: dois gráficos, pequenos múltiplos, ou indexar as duas séries a uma base comum.

![Negativos e positivos desenhados do mesmo lado da linha de base contra lados opostos, e duas escalas num gráfico só contra dois gráficos empilhados com o mesmo eixo horizontal](attachments/dataviz-20-direcao-e-eixo.svg)

## Linhas

**5. Pense na série temporal antes de usar linha.** O ponto é sutil e pouco citado: a linha liga marcadores, e quem lê presume que os valores entre eles existem. Se a receita é anual mas atualizada mensalmente, as linhas entre os pontos sugerem valores que ninguém mediu. A recomendação dele é usar barras verticais nesses casos.

Esse é o item mais subestimado da lista. A linha faz uma afirmação sobre continuidade que os dados podem não sustentar — e o problema é maior ainda em saúde pública, onde o dado chega com atraso e é revisado depois.

**6. Não use linha suavizada.** Curvas suaves são agradáveis e desonestas: elas inventam valores entre os pontos, e traço muito grosso ainda esconde onde os marcadores realmente estão.

![Dois problemas da linha: medição esparsa desenhada como linha inventa os valores entre as medições e deveria ser barra, e linha suavizada cria mínimos e máximos que não existem](attachments/dataviz-20-linhas.svg)

## Pizza e rosca

Quatro dos vinte itens tratam de pizza — de um gráfico que ele mesmo diz que na maioria dos casos deveria ser uma barra. É um retrato honesto da realidade: ninguém consegue matar a pizza, então mais vale ensinar a fazê-la direito.

![As quatro regras de pizza da lista: número de fatias, rótulo fora e não por cima, maior fatia às 12 horas em ordem decrescente, e rosca larga o bastante para comparar](attachments/dataviz-20-pizza.svg)

**8. Limite as fatias.** Não mais que cinco a sete, agrupando o resto em "Outros".

**10. Não rotule por cima das fatias.** Valores em cima criam problema de legibilidade e ficam impossíveis em fatias finas. Ele sugere rótulos escuros ligados a cada segmento.

**11. Ordene as fatias.** Maior fatia às 12 horas e as seguintes em ordem decrescente no sentido horário; ou a segunda maior logo depois e a terceira às 11 horas, com o resto decrescendo.

**13. Rosca fina é ilegível.** Tirar o miolo libera espaço para informação e sacrifica clareza — levado ao extremo, o gráfico deixa de funcionar.

O que a hierarquia perceptual acrescenta a esses quatro: pizza codifica por **ângulo**, o quarto degrau de seis. Todas as correções acima existem para compensar uma codificação fraca. Quando a comparação importa de verdade, a resposta continua sendo barra.

## Rótulo e ordem

O trio de melhor retorno por esforço da lista inteira.

**9. Rotule direto no gráfico.** Consultar a legenda custa tempo e energia mental para ligar valor e segmento.

Isso é mais importante do que o artigo deixa claro, porque é também uma medida de acessibilidade: rótulo direto elimina a dependência da cor como único canal. Uma ressalva prática que ele não faz — rotular **tudo** vira ruído. Rotule o extremo, o final da linha, a série que importa; deixe o eixo e o tooltip cuidarem do resto.

**12. Fuja da aleatoriedade.** Não use ordem alfabética por padrão: ponha os maiores valores no topo (barra horizontal) ou à esquerda (vertical), para que o mais importante ocupe o espaço mais nobre e o olho percorra menos.

Com uma exceção que vale registrar: quando a pessoa vem **procurar um item específico** — um estado, um produto que ela já sabe qual é —, a ordem alfabética ou uma ordem que ela já conhece ganha da ordem por grandeza. Ordenar por valor serve para descobrir; ordenar por nome serve para localizar.

**18. Barra horizontal em vez de rótulo girado.** Simples e certo. Texto na vertical é mais lento de ler e, em gráfico interativo, é um problema de acessibilidade — o WCAG desaconselha texto rotacionado.

![Legenda separada contra rótulo direto, ordem alfabética contra ordem por valor com o caminho do olho desenhado, e rótulo girado contra barra horizontal](attachments/dataviz-20-rotulo-e-ordem.svg)

## Estilo

**14. Deixe o dado falar.** A lista do que evitar é a do Tufte: 3D, sombreado, sombras, gradientes e distorções de cor, padrões de zebra, excesso de linhas de grade, fontes decorativas, itálico, negrito ou serifadas.

Concordo com quase tudo. Duas notas. A primeira é que a proibição de negrito é forte demais — negrito em subtítulo de seção funciona bem e não atrapalha a leitura do dado; o que atrapalha é negrito **no dado**. A segunda é a ressalva que a pesquisa posterior levantou contra o purismo de tinta-dado: certos elementos memoráveis ajudam na retenção, e gráfico completamente despido nem sempre comunica melhor para público amplo. A regra que sobrevive: rigor por padrão, ornamento como decisão consciente, e nunca em cima da codificação.

**17. Cuide da legibilidade.** Tipografia legível, sem serifa e sem fonte decorativa; evitar itálico, negrito e caixa alta; alto contraste com o fundo; não girar texto.

![Gráfico carregado de 3D, gradiente, sombra, grade tracejada e faixa de fundo contra o mesmo gráfico limpo; e seis defeitos de tipografia contra o rótulo legível](attachments/dataviz-20-estilo.svg)

## Cor

**15. A paleta acompanha a natureza do dado.** Ele descreve três tipos, e a descrição está correta:

- **Qualitativa** para variáveis categóricas, com cores distintas o bastante para serem acessíveis
- **Sequencial** para variáveis numéricas ordenadas, variando matiz, luminosidade ou os dois
- **Divergente** para duas sequenciais com um valor central no meio, geralmente zero — com o cuidado de que a cor combine com a noção de positivo e negativo

Eu trabalho com **quatro** categorias, e a que falta aqui é a mais perigosa na prática: a **semântica de estado** — bom, atenção, grave, crítico. Ela precisa ser reservada. Se vermelho significa erro no seu produto, ele não pode ser também a série 4 do gráfico ao lado. Está em [[Cor em gráfico]].

**16. Projete para acessibilidade.** Duas recomendações: usar saturação e luminosidade diferentes na paleta, e imprimir em preto e branco para conferir contraste e legibilidade.

O teste do preto e branco é o melhor conselho de bolso que existe nesse tema, e é o mesmo que Lisa Charlotte Muth resume como "acerte em preto e branco" — funciona porque a maior parte dos problemas de daltonismo é de matiz, não de luminosidade.

Duas correções, porém. A primeira é um dado: o artigo diz, citando o National Eye Institute, que **cerca de 1 em 12 humanos** é daltônico. O número correto é 1 em 12 **homens** e cerca de 1 em 200 mulheres — a prevalência geral fica perto de 4%, não de 8%. Continua sendo muito gente (algo como 300 milhões de pessoas), mas vale citar certo.

A segunda é de escopo, e é a maior lacuna do artigo: **acessibilidade aqui é só cor**. Não há leitor de tela, teclado, tabela equivalente, zoom nem descrição textual. É o assunto de [[Acessibilidade em dataviz]], e é onde as auditorias reais encontram os problemas mais graves.

![As três paletas do artigo — qualitativa, sequencial e divergente — mais a semântica de estado que ele não cita, e o teste de imprimir em preto e branco](attachments/dataviz-20-paletas.svg)

## Ferramenta e interação

**19. Escolha a biblioteca de gráficos.** O argumento é bom e raramente feito: bibliotecas modernas já trazem muitas dessas regras e interações embutidas, e desenhar a partir de uma biblioteca definida facilita a implementação e sugere ideias de interação.

O critério que falta na lista dele é justamente o de acessibilidade. Bibliotecas variam muito nisso — algumas geram SVG com descrição e navegação por teclado, outras desenham em `canvas`, que é opaco para tecnologia assistiva. Essa diferença deveria pesar tanto quanto a estética.

**20. Vá além do relatório estático.** Deixar a pessoa mudar parâmetros, tipo de visualização e período; tirar conclusões para maximizar o insight. O exemplo dele é o app Saúde do iOS, que combina vários tipos de apresentação do mesmo dado.

O exemplo é bem escolhido — e o app Saúde é, por outros motivos, o melhor caso público de acessibilidade em dataviz, com navegação estruturada por leitor de tela, gráficos sonoros e resumo em texto acima do gráfico.

![Os três níveis: relatar, que só mostra o número; explorar, que deixa mudar o recorte; e concluir, que diz em uma frase o que aquilo significa](attachments/dataviz-20-relatar-explorar-concluir.svg)

Uma ressalva importante que a lista não faz: **não esconda o dado atrás da interação**. Informação que só existe no hover exclui celular, teclado e leitor de tela de uma vez. Interação enriquece; não pode ser o único caminho.

## O que a lista não cobre

Nada disso invalida o artigo — ele é bom no que se propõe, que é uma lista de erros visuais frequentes. Mas convém saber o que procurar em outro lugar:

**Incerteza.** Nenhuma menção a intervalo de confiança, margem de erro ou dado provisório. É a omissão mais séria, e a que a revisão dos painéis de pandemia mostrou custar caro.

**Tabela.** A possibilidade de que a resposta certa seja não fazer gráfico não aparece. Consultar um valor exato não é tratado como tarefa legítima.

**Acessibilidade além da cor.** Já dito acima.

**Teste.** Não há nenhum método para descobrir se o gráfico funcionou. Todas as regras são normativas, nenhuma é verificável com gente.

## O que eu levaria da lista

Se fosse reduzir os vinte a cinco, ficaria com: **rotule direto** (9), **ordene por valor** (12), **nunca eixo duplo** (7), **barra no zero e linha não** (3 e 4), e **teste em preto e branco** (16). Esses cinco resolvem a maior parte do que se vê de errado por aí, e os quatro primeiros são de graça.

---

**Ver também:** [[Escolher a forma]] · [[Cor em gráfico]] · [[Como um gráfico mente]] · [[Acessibilidade em dataviz]] · [[Tabelas e painéis]]

## Fontes

- **[20 ideas for better data visualization](https://uxdesign.cc/20-ideas-for-better-data-visualization-73f7e3c2782d)** · Taras Bakusevych, UX Collective, 17 ago 2021 — o artigo comentado nesta página.
- **[10 rules for better dashboard design](https://uxplanet.org/10-rules-for-better-dashboard-design-ef68189d734c)** · Taras Bakusevych, UX Planet — o artigo companheiro, citado por ele no item 1.
- **[ColorBrewer](https://colorbrewer2.org/)** — a ferramenta de paletas que ele recomenda no item 15, com filtro de segurança para daltonismo e para impressão.
- **[Truncating the Y-Axis: Threat or Menace?](https://arxiv.org/abs/1907.02035)** · Correll, Bertini e Franconeri, CHI 2020 — a complicação dos itens 3 e 4.
- **[Graphical Perception](https://www.tandfonline.com/doi/abs/10.1080/01621459.1984.10478080)** · Cleveland e McGill, 1984 — a base do item 1 e a razão dos itens 8, 10, 11 e 13.
- **[What to consider when visualizing data for colorblind readers](https://www.datawrapper.de/blog/colorblindness-part2)** · Lisa Charlotte Muth, Datawrapper — o item 16 aprofundado.
- **[About Colour Blindness](https://www.colourblindawareness.org/colour-blindness/)** · Colour Blind Awareness — a fonte da correção sobre prevalência: 1 em 12 homens, 1 em 200 mulheres.
- **[Chartability](https://chartability.fizz.studio/)** · Frank Elavsky — a acessibilidade que falta no item 16.
