---
title: "UX Busca"
description: "Índice das anotações sobre experiência de busca: o artigo principal, as ferramentas e as fontes que sustentam tudo"
tags:
  - tema/ux
  - dominio/busca
  - tipo/indice
aliases:
  - "Busca/📌 Resumo dos Artigos Analisados"
---

Esta pasta reúne o que estudei sobre experiência de busca — barra, sugestões, página de resultados, filtros e o que fazer quando não há resultado nenhum.

## Comece por aqui

**[[A busca não é um campo de texto]]** — o artigo que consolida tudo. O argumento é que o esforço de UX em busca costuma ir para o lugar errado: a caixa está resolvida desde 2001, e o que quebra é o que acontece depois do Enter. Cobre os tipos de consulta que os sites não respondem, os limites de tempo de resposta, zero resultados e por que busca não conserta navegação.

**[[Ferramentas de busca]]** — plataformas e serviços de busca para produto.

## Fontes

Todas verificadas em 10 ago 2026. As anotações de leitura estão dentro do artigo acima; aqui fica só o que cada fonte é e para que serve.

- **[Search UX Best Practices](https://www.pencilandpaper.io/articles/search-ux)** · Fanny Vassilatos e Ceara Crawshaw, Pencil & Paper, 2023
  A mais completa e a mais prática. Divide a experiência em barra, dropdown, carregamento e resultados, define quatro intenções de busca e lista os erros comuns. É a única que trata carregamento como assunto de primeira classe.

- **[Ecommerce Search UX Best Practices](https://baymard.com/blog/ecommerce-search-query-types)** · Baymard, atualizado abr 2026
  Levantamento em mais de 170 sites sobre **que tipo de consulta** falha. É o dado mais acionável de toda a lista: mostra que os casos que os times testam não são os que quebram.

- **[5 Proven UX Strategies for "No Results" Pages](https://baymard.com/blog/no-results-page)** · Baymard
  Cinco estratégias para zero resultados, com o achado de que dicas de busca sozinhas não funcionam.

- **[Search: Visible and Simple](https://www.nngroup.com/articles/search-visible-and-simple/)** · Jakob Nielsen, NN/g, 2001
  A origem das taxas de sucesso por tentativa (51%, 32%, 18%) e da recomendação de não oferecer busca avançada na página inicial. Antigo, mas o argumento estrutural não envelheceu.

- **[Response Times: The 3 Important Limits](https://www.nngroup.com/articles/response-times-3-important-limits/)** · Jakob Nielsen, NN/g, 1993
  Não é sobre busca, mas define os limites (0,1s / 1s / 10s) que determinam quando a autossugestão parece rápida ou quebrada.

- **[Enriched Site-Search Suggestions: Rarely Used](https://www.nngroup.com/articles/enriched-site-search-suggestions/)** · Kate Kaplan, NN/g, 2022
  O caso contra sugestões enriquecidas: usadas 7 vezes em 60 oportunidades, sem melhora com o hábito.

- **[Best Practices for Search Results](https://uxplanet.org/best-practices-for-search-results-1bbed9d7a311)** · Nick Babich, UX Planet
  Dez itens sobre a página de resultados — não apagar a consulta, corrigir erros de digitação, mostrar o total, guardar buscas recentes, mostrar progresso e nunca devolver "nenhum resultado" sem saída.

- **[Search Results Page Design: UI/UX Best Practices](https://medium.com/@halolab/search-results-page-design-ui-ux-best-practices-f2157eea8226)** · Halo Lab
  Layouts de página de resultados, resultados mesclados, zero resultados e busca semântica. É de onde vem o exemplo do cardigã cottagecore que não existe mais no estoque.

- **[Search UX best practices: a complete guide](https://nulab.com/learn/design-and-ux/search-ux-best-practices/)** · Nulab
  Panorama introdutório: caixa, facetas, autocomplete, buscas em alta, abas por tipo de resultado. Abre com a estatística de conversão de quem usa busca — ver a ressalva na nota abaixo.

- **[Search Box UX Examples](https://www.coveo.com/blog/search-box-ux-examples/)** · Coveo
  Seis práticas ilustradas com casos reais (Dell, United, Best Buy, Fleetpride): índice unificado, posicionamento, autocomplete preditivo, busca generativa, facetas e analytics de busca.

## Relacionados

[[Artigos Nielsen Norman Group]] · [[Artigos UX Design.cc]]

---

## Nota de método

Esta página continha um bloco de "pontos principais" resumindo cada fonte, e um "Resumo" longo sobre UX de busca em geral. Ambos foram removidos. A auditoria de 10 ago 2026 encontrou o seguinte:

**Quatro dos seis resumos não correspondiam ao artigo que diziam resumir.** O de Coveo atribuía ao texto exemplos de saúde — "Buscar exames ou vacinas", busca avançada "por tipo de exame ou faixa etária" — que não existem lá; o artigo real trata de índice unificado, busca generativa e analytics, com exemplos de Dell e United Airlines. O de UX Planet listava hierarquia visual para promoções, scroll infinito, filtros por localização e performance: nenhum desses termos aparece no artigo, que é a lista de dez itens de Nick Babich. O de Nulab prometia "mobile-first", assunto que o guia não aborda. O de NN/g trazia quatro genéricos — acessibilidade, minimalismo, testes de usabilidade — que não são o que aquele artigo diz. O de Halo Lab acertava três pontos e inventava um botão "Agendar agora".

O padrão é reconhecível: especificidades com sabor de saúde inseridas em artigos que não falam de saúde, e recheio genérico no lugar do argumento real de cada texto.

**A estatística de conversão estava errada, e o erro era meu.** Eu havia anotado "quem usa a busca tem 1,8% mais chance de converter". A frase é fiel à Nulab, que escreve "1.8% more likely" — mas a Nulab distorceu a fonte que ela mesma cita. O dado original da Econsultancy é **1,8×**: conversão de 2,77% no geral contra 4,63% entre quem usa a busca. Copiei o erro de uma fonte secundária sem conferir a primária.

**O "Resumo" final** eram cerca de 60 linhas sobre fundamentos, comportamento, tendências e e-commerce, sem nenhuma fonte, e hoje redundante com [[A busca não é um campo de texto]].

**De quebra, um mistério resolvido.** A antiga página de anotações pulava do item 1 para o 3 na lista do UX Planet. O artigo original tem dez itens; o que sumiu foi o número 2, "Provide accurate and relevant results", perdido no recorta e cola.

Links: das dez URLs, oito respondem 200. As duas de 403 são bloqueio do Medium a robôs — confirmei ambas por snapshot do Internet Archive, e é de lá que vêm os títulos e a autoria acima.
