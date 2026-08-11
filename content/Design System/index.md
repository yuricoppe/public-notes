---
title: "Design System"
description: "Índice das anotações sobre design systems: os cinco artigos, as fontes que os sustentam, e as ferramentas e templates de referência"
tags:
  - tema/design-system
  - tipo/indice
aliases:
  - "Design System"
---

Esta pasta reúne o que estudei sobre **design systems** — não a parte de como desenhar um botão, e sim a parte que determina se o sistema é usado: o que ele é, o que entra nele, quem decide, como se comunica mudança e como se mede se aquilo está funcionando.

O fio que atravessa os cinco artigos é que o problema quase nunca está no acervo. Os dados disponíveis apontam sempre para a mesma direção: sistemas fracassam por falta de suporte, de processo conhecido e de manutenção, não por falta de componentes.

## Comece por aqui

**[[O que é e quando não vale a pena]]** — as quatro palavras que os times confundem (design system, guia de estilo, biblioteca de componentes, biblioteca de padrões), o que o sistema custa de verdade, e as quatro situações em que construir um é a decisão errada.

**[[A anatomia em camadas]]** — onde cada coisa mora: o ecossistema em camadas de Brad Frost, a diferença entre componente, receita e floco de neve, uma ressalva sobre atomic design e a proposta de um Global Design System.

**[[Governança e contribuição]]** — os três modelos de time de Nathan Curtis, o fluxo de decisão de um padrão novo, os quatro níveis de contribuição, e por que revisão lenta destrói mais adesão do que regra rígida.

**[[Adoção e maturidade]]** — as seis dimensões de maturidade da NN/g, o que os sistemas bem-sucedidos fazem de diferente segundo a pesquisa da Sparkbox, e como medir sem se enganar.

**[[Versionar, depreciar, documentar]]** — versionamento semântico aplicado a design, janelas de depreciação, o que uma página de componente precisa ter, e por que reduzir também é manutenção.

## Fontes

Todas verificadas em 11 ago 2026.

### Fundamentos e arquitetura

- **[The Design System Ecosystem](https://bradfrost.com/blog/post/the-design-system-ecosystem/)** · Brad Frost, set 2023
  As camadas do ecossistema, os quatro ativos do núcleo (tokens, ícones, componentes, site de referência) e a Lei de Gall como justificativa para manter tudo simples enquanto der. Termina com a frase que resume o ofício: design systems são menos sobre ativos e mais sobre pessoas.

- **[Design System Components, Recipes, and Snowflakes](https://bradfrost.com/blog/post/design-system-components-recipes-and-snowflakes/)** · Brad Frost, fev 2021
  O vocabulário mais útil que existe para decidir o que entra no sistema. Curto e resolve uma discussão que se repete toda semana.

- **[A Global Design System](https://bradfrost.com/blog/post/a-global-design-system/)** · Brad Frost, jan 2024
  A proposta de uma biblioteca comum para toda a web, com o argumento de acessibilidade — nenhum dos cem sites mais acessados usa HTML válido, e o WebAIM Million encontrou cerca de 50 erros por página no primeiro milhão de sites. Ver também [What's Next for a Global Design System](https://bradfrost.com/blog/post/whats-next-for-a-global-design-system/), de mar 2024.

- **[Atomic Design](https://atomicdesign.bradfrost.com/)** · Brad Frost, livro completo online
  A metodologia original. Vale como modelo mental; ver a ressalva sobre usá-la como estrutura de pastas em [[A anatomia em camadas]].

- **[Design Systems 101](https://www.nngroup.com/articles/design-systems-101/)** · Therese Fessenden, Nielsen Norman Group, abr 2021
  As definições que separam design system de guia de estilo, biblioteca de componentes e biblioteca de padrões — e a recomendação explícita sobre quando um design system **não** compensa.

### Governança, times e contribuição

- **[Team Models for Scaling a Design System](https://medium.com/eightshapes-llc/team-models-for-scaling-a-design-system-2cf9d03be6a0)** · Nathan Curtis, EightShapes, set 2015
  Solitário, centralizado e federado, com a fraqueza característica de cada um e cinco recomendações para montar um time federado que funcione. É o texto que criou o vocabulário que todo mundo usa desde então.

- **[Defining Design System Contributions](https://medium.com/eightshapes-llc/defining-design-system-contributions-eb48e00e8898)** · Nathan Curtis, EightShapes, jan 2020
  Os quatro níveis de contribuição — correção, melhoria pequena, melhoria grande, recurso novo — e a fricção que nenhum processo resolve: o contribuidor é designer **ou** desenvolvedor, quase nunca os dois.

- **[A Design System Governance Process](https://bradfrost.com/blog/post/a-design-system-governance-process/)** · Brad Frost, nov 2019
  O fluxo de dez passos, do "use o que já existe" até a adoção, com a bifurcação entre floco de neve e padrão do sistema.

- **[Handling new patterns](https://primer.style/product/contribute/handling-new-patterns/)** · Primer (GitHub)
  A mesma decisão, escrita como critério operacional de uma organização real. Notável pelo que não tem: nenhuma regra de "três usos" — a promoção depende de alinhamento e de capacidade de quem mantém.

- **[Your Design System Needs an Enforcer](https://www.nngroup.com/articles/design-system-enforcer/)** · Laura Klein, Nielsen Norman Group, fev 2026
  O argumento a favor de alguém com autoridade para fazer o sistema valer — e o contraexemplo mais importante: o time que protegia o sistema ferozmente e tinha adoção baixíssima até acelerar as revisões. Baseado em experiência profissional, sem pesquisa formal.

- **[Keeping design system contributions in check](https://www.designsystems.com/keeping-design-system-contributions-in-check/)** · designsystems.com
  Como um time montou um modelo de contribuição autogovernado para resolver falta de adesão.

- **[Zalando's design system contribution model](https://medium.com/zalando-design/zalandos-design-system-contribution-model-73ab36f8591e)** · Zalando Design

- **[The paradox of design systems](https://spotify.design/article/the-paradox-of-design-systems)** · Spotify Design — ⚠️ **fora do ar**: o domínio `spotify.design` foi desativado e redireciona para o `open.spotify.com` (verificado em 11 ago 2026). O texto continua legível no [snapshot de set 2025 no Internet Archive](https://web.archive.org/web/20250917091617/https://spotify.design/article/the-paradox-of-design-systems).

### Maturidade, adoção e métricas

- **[Design-System Maturity: A 6-Dimension Framework](https://www.nngroup.com/articles/design-system-maturity/)** · Huei-Hsin Wang, Nielsen Norman Group, jul 2026
  As seis dimensões avaliadas separadamente, e o argumento contra modelos lineares de maturidade — inclusive o de que adoção não é uma fase que termina. O artigo não informa quantos times foram estudados nem o método; é instrumento de conversa, não resultado de pesquisa validado.

- **[The 2022 Design Systems Survey](https://designsystemssurvey.sparkbox.com/2022/)** · Sparkbox
  A melhor evidência quantitativa desta lista: 219 respostas, mais de vinte setores. É de onde vêm os números que sustentam o argumento central — 30% de todos os sistemas oferecem onboarding contra 84% dos bem-sucedidos, e só 16% medem qualquer coisa. As edições anteriores ([2021](https://designsystemsurvey.sparkbox.com/2021/), [2020](https://designsystemssurvey.seesparkbox.com/2020/), [2019](https://designsystemsurvey.seesparkbox.com/2019/), [2018](https://designsystemssurvey.seesparkbox.com/2018/)) permitem ver a série.

- **[Design systems 104: Making metrics matter](https://www.figma.com/blog/design-systems-104-making-metrics-matter/)** · Carly Ayres, Figma, fev 2025
  As três categorias de métrica (uso de biblioteca, eficácia da documentação, consistência) e a ressalva mais útil: taxa alta de destacamento nem sempre é ruim. Os números de produtividade citados são de fornecedores e de estudos de caso próprios — servem para orçamento, não como evidência.

### Versionamento e manutenção

- **[Versioning Design Systems](https://medium.com/eightshapes-llc/versioning-design-systems-48cceb5ace4d)** · Nathan Curtis, EightShapes, set 2018
  SemVer aplicado a design system: o que conta como maior, menor e correção; desacoplar a versão da documentação; versionar os arquivos de design; e as janelas de depreciação reais — 18 meses no Lightning da Salesforce, 3 a 6 meses no Origami do Financial Times.

- **[Design documentation](https://medium.com/design-bridges/design-documentation-2-b03e270c2d5b)** · Design Bridges

- **[How to bring structure and clarity to design system components](https://www.buttonevents.com/blog/how-to-bring-structure-and-clarity-to-design-system-components?ref=sidebar)** · Button
  Nota: o domínio mudou de `buttonconf.com` para `buttonevents.com`; o link acima já é o novo.

### Começar do zero

- **[Design System In 90 Days](https://www.smashingmagazine.com/2025/05/design-system-in-90-days/)** · Vitaly Friedman, Smashing Magazine, mai 2025
  Não é um plano de 90 dias — é uma coletânea de instrumentos para a conversa inicial: o canvas de Dan Mall, as *Design System Tactics* de Ness Grixti e um checklist de duas páginas de Nathan Curtis para uma atividade de time de 60 minutos.

- **[Design Systems (categoria)](https://www.smashingmagazine.com/category/design-systems/)** · Smashing Magazine
  O acervo da revista no assunto, útil para acompanhar o que vai saindo.

- **[Redesigning Design Systems](https://redesigningdesign.systems/)** · redesigningdesign.systems

- **[Design System Knowledge Base](https://thedesignsystem.guide/knowledge-base)** · The Design System Guide
  Base de consulta organizada por pergunta, boa para tirar dúvida pontual. Ver também a [coleção de métricas](https://thedesignsystem.guide/design-system-metrics).

- **[Embracing Design Dialects](https://alistapart.com/article/design-dialects-breaking-the-rules-not-the-system/)** · A List Apart
  Defende tratar o design system como língua viva, com dialetos, em vez de regra rígida. Conversa direto com a discussão sobre flocos de neve.

## Vídeos

- **[Deep Dive into Uber's Design Systems](https://www.youtube.com/watch?v=-z9JX8Lz5lI)** · Figma, mai 2025 · 49 min
  Jayneil Dalal entrevista Ian Guisard, que lidera design systems na Uber, dentro do arquivo real. Os capítulos valem como pauta de trabalho: variáveis por componente, mudar densidade de tela com variáveis, **benefícios de reduzir a quantidade de componentes**, depreciação, especificação para engenharia, documentação para quem desenvolve, registro de mudanças, quando quebrar as regras do sistema e anotações no Dev Mode.

- **[Sneak Peek](https://www.youtube.com/@sneakpeekdesign)** · Jayneil Dalal · canal
  Série de entrevistas que abre os arquivos do Figma de designers de empresas como Slack, Figma, Wealthfront, Plaid e Lattice, com tela compartilhada o tempo todo. O valor está nas restrições reais que tutorial nenhum mostra. Também em [sneakpeek.design](https://www.sneakpeek.design/).

- **[Deep Dive into Southwest Airlines' Design Systems](https://www.youtube.com/watch?v=1YpX4OgITkY)** · Figma
- **[Tokens, variables, and styles — Introduction to design systems](https://www.youtube.com/watch?v=JyCmacSyDY4)** · Figma
- **[Design System na vida real: o que realmente importa](https://www.youtube.com/watch?v=LYIKaIeDK9k)** · Design Circuit · em português
- **[Design Systems (playlist)](https://www.youtube.com/playlist?list=PLkmvmF0zhgT_8FirlLcTQI01ayjYB-46_)** · UI Collective
- **[Build a Design System — Full Course](https://www.youtube.com/watch?v=opTANvl9G1g)** · UI Collective
- **[Design System & Figma Variable Set Up — Full Tutorial](https://www.youtube.com/watch?v=L-tpK7Eeuow)** · UI Collective
- **[Design to Developer Handoff in Figma — Full Tutorial](https://www.youtube.com/watch?v=ALkqhXv0GPk)** · UI Collective

## Figma

- **[Components, styles, and shared libraries best practices](https://www.figma.com/best-practices/components-styles-and-shared-libraries/)** · Figma
- **[Team, folder, and file organization](https://www.figma.com/best-practices/team-file-organization/)** · Figma
- **[Creating Figma components in a Design System file](https://thedesignsystem.guide/knowledge-base/creating-figma-components-in-a-design-system-file)** · The Design System Guide
- **[How to organize your Figma files for your design system](https://help.zeroheight.com/hc/en-us/articles/36473914948379)** · zeroheight
  Nota: a URL antiga em `zeroheight.com/help/guides/` foi movida para a central de ajuda; o link acima já é o destino atual.
- **[11 uses for variables beyond light and dark mode](https://www.alicepackarddesign.com/blog/uses-for-variables-beyond-light-and-dark-mode?ref=sidebar)** · Alice Packard
- **[3 reasons to use variables for validation styling (instead of variants)](https://www.alicepackarddesign.com/blog/reasons-to-use-variables-for-validation-styling)** · Alice Packard

## Ferramentas

- **[Figlint](https://www.figma.com/community/plugin/1323794044088972088/figlint)** · plugin do Figma
  Verifica a consistência do arquivo e gera relatório apontando o que destoa do sistema.
- **[Variable Visualizer](https://www.figma.com/community/plugin/1457362132545070106/variable-visualizer)** · plugin do Figma
  Transforma o conjunto de tokens em um mapa interativo navegável.

## Templates

- **[Romina Kavcic](https://www.figma.com/@rominadesigner)** · perfil no Figma Community
  Templates de design system e estratégia.

## Relacionados

[[Tokens]] · [[Figma]] · [[Glossário/Entregáveis/design_system|Design System (Glossário)]] · [[Glossário/Entregáveis/style_guide|Style Guide]] · [[Acessibilidade/index|Acessibilidade]]

---
