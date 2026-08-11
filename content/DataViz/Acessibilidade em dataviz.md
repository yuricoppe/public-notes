---
title: "Acessibilidade em dataviz"
description: "As seis camadas de um gráfico acessível, o que a auditoria dos painéis eleitorais encontrou, e o que a Apple faz que quase ninguém copia"
tags:
  - tema/dataviz
  - tema/acessibilidade
  - tipo/artigo
---

Gráfico é o componente menos acessível da web, e não por falta de técnica. A técnica existe, está documentada e é razoavelmente simples. O que falta é alguém testar.

A evidência disso é dura. Sarah Fossheim auditou os painéis de resultados da eleição americana de 2024 em nove veículos — Fox News, Washington Post, NBC, Bloomberg, CNN, Reuters, ABC, Wall Street Journal e a norueguesa NRK. Um único painel acumulou **870 problemas**, dos quais 62 eram erros de WCAG detectáveis por ferramenta automática. E a conclusão dela sobre o que isso significa é a parte que importa: quando um teste automático encontra centenas de erros numa única página, não há teste de acessibilidade acontecendo. Não é erro de execução individual — é ausência de processo.

Fossheim tinha feito a mesma auditoria em 2020. Entre uma e outra, quase nada mudou.

## As seis camadas

![As seis camadas de um gráfico acessível: independência de cor, frase que resume, tabela equivalente, teclado, leitor de tela e zoom](attachments/dataviz-camadas-acessibilidade.svg)

**1. O dado não depende só de cor.** Coberto em [[Cor em gráfico]]. Na auditoria, o mapa da Reuters virava exatamente o mesmo cinza para os dois partidos sob simulação de acromatopsia — a informação principal do gráfico, apagada.

**2. Uma frase diz o que o gráfico mostra.** Não o título do eixo: o achado. "As vendas caíram 12% no trimestre, puxadas pela região Sul." Isso não é concessão a leitor de tela — é o que a maioria das pessoas queria de qualquer forma, e é o que salva quem tem dificuldade de leitura visual, ansiedade com números ou pressa.

**3. Existe a tabela equivalente.** O gêmeo do gráfico, não um anexo escondido. Com `<caption>` e `<th scope="row">`. Resolve leitor de tela, resolve quem quer o número exato e resolve copiar para outro lugar.

Um detalhe que a auditoria pegou e que vale como aviso: a Fox News gerou uma tabela separada e sem nome por estado, o que produziu mais de cinquenta entradas indistinguíveis no menu de tabelas do VoiceOver. Tabela sem legenda em quantidade é pior que tabela nenhuma.

**4. Dá para chegar e ler pelo teclado.** Regra única: **o que aparece no hover aparece no foco.** Na CNN, o foco pulava o mapa inteiro. Na Reuters e na ABC, os tooltips só existiam no mouse. E há o excesso oposto: na Bloomberg, cada um dos 538 quadrados era um link — 538 paradas de tabulação para atravessar um gráfico.

**5. O leitor de tela recebe os valores.** Aqui está o erro mais comum e mais fácil de corrigir. As descrições encontradas na auditoria diziam o que o gráfico *é*, não o que ele *diz*: "Mapa dos EUA que mostra a quantidade de votos do colégio eleitoral por estado" — sem nenhum resultado. A Bloomberg: "gráfico de linhas múltiplas mostrando as probabilidades…" — sem um número sequer.

A técnica, para SVG:

- `role="img"` com `aria-label` ou `aria-describedby` contendo uma descrição **com os valores**
- `aria-hidden="true"` em tudo que é decorativo — grade, moldura, sombra
- ordem no DOM igual à ordem visual, porque a navegação segue o DOM
- nada de deixar cada `<rect>` ser anunciado individualmente como "imagem", que foi o que aconteceu no Wall Street Journal

Para `<canvas>` não há saída elegante: o conteúdo é opaco para tecnologia assistiva. Se o gráfico é canvas — caso da CNN, rotulado apenas como "Mapa" —, a tabela equivalente deixa de ser boa prática e passa a ser a única forma de o dado existir.

**6. Sobrevive a 400% de zoom.** O critério do WCAG que quase ninguém testa, e o inimigo é sempre o mesmo: cabeçalho fixo. No Washington Post, cabeçalho e rodapé fixos consumiam a tela inteira a 400%, sem sobrar espaço para conteúdo. A NBC tinha três barras de navegação mais cabeçalho de tabela fixo.

## O que funcionou

Vale registrar, porque a auditoria não foi só negativa. A NRK norueguesa, com três erros automáticos contra dezenas dos outros, acertou coisas transferíveis:

- **Poucos elementos fixos**, então o zoom alto continuava utilizável
- **Explicação em texto do que o gráfico significa**, em cartões e perguntas frequentes — inclusive material didático sobre como funciona o sistema eleitoral
- **Instrução explícita de interação**: "passe o mouse ou use Tab nos estados". Dizer como se usa o gráfico é acessibilidade, e é raro.

## Onde olhar quando funciona bem

Fossheim tem uma análise do aplicativo Saúde da Apple que serve de catálogo de técnicas bem executadas:

**Navegação estruturada.** O VoiceOver percorre o gráfico por unidade significativa — hora a hora, cada hora sendo uma coluna com seus valores — em vez de anunciar formas soltas.

**Rótulo que carrega o contexto do eixo.** Informação que normalmente estaria só no eixo é incorporada ao rótulo de cada elemento, para que quem não vê o eixo não perca a referência.

**Gráficos sonoros.** Em medições contínuas como eletrocardiograma e oxigenação, o dado é apresentado em som — tom e frequência variando — em vez de forma. É a demonstração mais direta de que "visualização" não precisa ser visual.

**Resumo em texto acima do gráfico.** "Na sua última caminhada, sua frequência cardíaca ficou entre 114 e 158." O achado, em uma frase, antes de qualquer forma.

**O mesmo dado em mais de um formato** — rosca, barra, detalhamento — porque pessoas processam informação de maneiras diferentes.

## Chartability

Para quem quiser um instrumento de auditoria em vez de uma lista de conselhos, existe o **Chartability**, de Frank Elavsky: cerca de cinquenta heurísticas em forma de perguntas testáveis, organizadas em sete princípios — os quatro do WCAG (perceptível, operável, compreensível, robusto) mais três extensões próprias de dado: **comprometedor**, **assistivo** e **flexível**.

O valor dele é ser aplicável a artefato de qualquer maturidade: já foi usado para avaliar Tableau, Power BI, bibliotecas de código e até desenhos em Figma. Ou seja, dá para rodar antes de existir código — que é quando corrigir é barato.

## O mínimo defensável

Se der para fazer só três coisas:

1. **A frase com o achado**, acima do gráfico.
2. **A tabela equivalente**, sempre.
3. **Simulador de daltonismo**, antes de publicar.

As três juntas levam menos de uma hora e cobrem a maior parte do que as auditorias encontram. O resto — teclado, ARIA, zoom — é mais trabalhoso e depende de teste com tecnologia assistiva de verdade, que é a etapa que nenhuma ferramenta automática substitui.

---

**Antes:** [[Cor em gráfico]] · [[Como um gráfico mente]] · **Continua em:** [[Tabelas e painéis]]

**Ver também:** [[Acessibilidade/index|Acessibilidade]] · [[Notificações/Acessibilidade de mensagens|Acessibilidade de mensagens]]
