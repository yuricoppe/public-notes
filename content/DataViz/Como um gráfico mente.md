---
title: "Como um gráfico mente"
description: "Eixo truncado, eixo invertido, dois eixos verticais e área enganosa — com o que a pesquisa mediu sobre cada um, incluindo o achado de que avisar não resolve"
tags:
  - tema/dataviz
  - tipo/artigo
---

Gráfico engana sem precisar de dado falso. Todos os exemplos aqui usam números corretos — a distorção está inteiramente na forma, e é por isso que ela passa despercebida por quem produz e por quem revisa.

## O eixo truncado

O caso clássico: começar o eixo vertical num valor diferente de zero.

![Os mesmos quatro números com o eixo em zero e com o eixo truncado, e a observação de que marcar a quebra não desfaz o efeito](attachments/dataviz-eixo-truncado.svg)

Sharon Pandey e colegas mediram isso com 330 participantes, testando duas famílias de distorção: **exagero da mensagem** e **reversão da mensagem**. O resultado confirma o que se suspeitava e mede o tamanho: as técnicas levam a interpretações erradas, e o efeito é grande.

Mas o trabalho mais útil sobre truncamento é o de Michael Correll, Enrico Bertini e Steven Franconeri, e ele complica a regra em vez de reforçá-la.

Primeiro, o achado incômodo: **marcar a quebra do eixo não desfaz o exagero.** Eles testaram os remédios habituais — o símbolo de corte no eixo, barras visivelmente interrompidas — e a percepção de magnitude praticamente não mudou. A explicação: julgamento de tamanho de efeito é **visual, não aritmético**. Quem lê corretamente os números do eixo continua achando a diferença maior do que ela é.

Segundo, e por isso o artigo se chama *Ameaça ou incômodo?*: os autores **recusam** a conclusão de que todo gráfico precisa incluir o zero. Não existe verdade absoluta e independente de domínio sobre quão importante é uma diferença. Uma variação de meio grau na temperatura média global é enorme; meio ponto percentual numa pesquisa de intenção de voto é ruído. Um eixo em zero, nos dois casos, esconderia a informação.

A recomendação que sobra é mais difícil e mais honesta: **escolha a escala a partir de qual diferença de fato importa naquele domínio** — e assuma que essa escolha é sua responsabilidade, não uma consequência automática de uma regra.

Na prática:

- **Barras precisam de zero.** A barra codifica quantidade por comprimento; cortar o comprimento quebra a codificação.
- **Linhas não precisam.** A linha codifica variação, e o zero frequentemente é irrelevante e desperdiça a área do gráfico.
- **Se a escala for apertada, diga o tamanho da variação** em texto, ao lado — porque a marcação visual sozinha não conserta a percepção.

## O eixo invertido

Menos discutido e mais grave, porque não exagera a mensagem: **inverte** a conclusão. É a mesma família de distorção que Pandey e colegas classificaram como "reversão de mensagem".

O exemplo célebre é um gráfico de mortes por arma de fogo com o eixo vertical de cabeça para baixo, em que uma alta parece uma queda. Quem lê rápido — que é como quase todo mundo lê gráfico — sai com o oposto do que os dados dizem.

A regra é simples e não tem exceção defensável: **valor maior fica mais alto.** Se a grandeza é ruim, isso se resolve com cor, com rótulo ou com a frase acima do gráfico, nunca invertendo a geometria.

## Dois eixos verticais

O erro mais frequente em painel corporativo: duas séries de escalas diferentes sobrepostas, cada uma lida num eixo.

![Catálogo de seis erros frequentes, começando por dois eixos verticais no mesmo gráfico](attachments/dataviz-antipadroes.svg)

O problema é que **o alinhamento entre as duas escalas é arbitrário.** Quem monta o gráfico escolhe, deliberadamente ou não, onde as duas linhas se cruzam e o quanto elas parecem andar juntas. O gráfico passa a afirmar uma correlação que não está nos dados — e o mais desconfortável é que a afirmação muda se alguém mexer no máximo de um dos eixos.

As saídas são três: dois gráficos empilhados com o mesmo eixo horizontal; pequenos múltiplos; ou **indexar as duas séries a uma base comum** (as duas valendo 100 no início) e desenhar em um eixo só. A terceira é a que preserva a comparação de crescimento relativo, que geralmente era o que se queria.

## Área e volume

Quando a grandeza é codificada em área, há dois enganos possíveis, e um deles é honesto por engano.

**Dobrar o raio quadruplica a área.** Se um círculo representa o dobro do outro, ele precisa ter raiz de dois vezes o raio, não o dobro. Ferramenta boa faz isso sozinha; código feito à mão, quase nunca.

**Área é imprecisa mesmo quando correta.** Está no quinto degrau da hierarquia perceptual — as pessoas subestimam sistematicamente diferenças de área. Bolha e treemap servem para dar noção de ordem de grandeza, não para comparar valores próximos.

E, de novo: **nada de 3D**. Perspectiva torna a comparação impossível de forma não uniforme — a distorção varia conforme a posição do elemento no gráfico.

## Chartjunk, e o limite da ideia

Edward Tufte cunhou *chartjunk* para tudo que ocupa tinta sem carregar informação: grades pesadas, molduras, texturas, sombras, efeitos. A ideia por trás — maximizar a proporção de tinta que representa dado — continua sendo o melhor conselho de primeira passada que existe. Na prática: grade fina e discreta, sem moldura, sem sombra, sem gradiente decorativo, sem fundo colorido.

Vale conhecer também a ressalva, que surgiu depois. Estudos posteriores sugerem que certa quantidade de elementos memoráveis ajuda na retenção e no engajamento, e que gráfico completamente despido nem sempre é o mais eficaz para comunicar a públicos amplos. A leitura razoável: **rigor por padrão, ornamento como decisão consciente com objetivo declarado** — e nunca em cima da codificação do dado.

## Um checklist de honestidade

- [ ] O eixo vertical começa em zero, ou a escala está justificada por qual diferença importa
- [ ] Nenhum eixo está invertido
- [ ] Não há dois eixos verticais
- [ ] A área é proporcional ao valor, não ao raio
- [ ] O intervalo de tempo mostrado não foi escolhido para favorecer uma conclusão
- [ ] A escala é a mesma entre painéis que serão comparados
- [ ] Nenhuma dimensão falsa: 3D, sombra, perspectiva
- [ ] O título afirma o que os dados sustentam, e não mais do que isso

O penúltimo e o antepenúltimo são os mais esquecidos. Recorte de tempo é a forma de manipulação mais fácil de cometer sem má-fé: começar a série no ponto mais baixo é uma escolha que qualquer um faz sem perceber. E pequenos múltiplos com escalas diferentes por painel são um convite a comparar coisas incomparáveis.

---

**Antes:** [[Cor em gráfico]] · **Continua em:** [[Acessibilidade em dataviz]] · [[Tabelas e painéis]]
