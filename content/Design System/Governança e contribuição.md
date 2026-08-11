---
title: "Governança e contribuição"
description: "Quem produz o sistema, quem decide o que entra nele, e por que revisão lenta destrói mais adesão do que regra rígida"
tags:
  - tema/design-system
  - tipo/artigo
---

Governança soa como a parte chata, e é a parte que determina se o sistema sobrevive. Brad Frost põe nesses termos: estabelecer um processo de governança é talvez a coisa mais importante que se pode fazer para evitar a entropia.

O problema tem duas metades independentes. A primeira é **quem produz** o sistema. A segunda é **como se decide** o que entra nele.

## Quem produz

Nathan Curtis descreveu em 2015 três arranjos que continuam sendo o vocabulário da área:

![Os três modelos de time — solitário, centralizado e federado — com quem decide o sistema em cada um e a fraqueza característica de cada arranjo](attachments/design-system-modelos-de-time.svg)

**Solitário.** Um time faz o sistema para si e o disponibiliza, mas as prioridades continuam sendo as do próprio produto. Serve bem a organizações pequenas e a times que não têm talento de design ou front-end próprio. A fraqueza é estrutural: quem adota fica sujeito às prioridades de outro time, e o sistema só evolui na direção da missão de quem o criou.

**Centralizado.** Um time dedicado produz e sustenta o sistema usado pelos outros, sem construir produto. Ganha independência de viés de produto e capacidade de espalhar a linguagem por um portfólio grande. A fraqueza é a falta de contexto: sem viver as restrições reais de um produto, o time central tem pouca visibilidade sobre os problemas do dia a dia e pouca influência sobre as decisões de compromisso que os designers de produto tomam. E a posição organizacional é sempre frágil — é o time que aparece primeiro na lista de corte.

**Federado.** Os melhores designers dos produtos mais importantes decidem juntos a direção do sistema, sem sair dos seus times. Ganha legitimidade, reduz a percepção de viés e cria vários evangelistas em vez de um só. A fraqueza é o excesso de cozinheiros: lealdade dividida entre o sistema e o produto de origem, decisões tomadas em conversas informais que ninguém consegue reconstituir depois, e a dificuldade permanente de equilibrar decisão rápida com consulta ampla.

Nenhum dos três é o certo. As correções que Curtis sugere valem mais do que a escolha em si:

- **Representar as plataformas que importam.** Um sistema decidido só por quem faz web não vai ser adotado por quem faz app nativo.
- **Distribuir disciplinas.** UX, visual, interação — e, na versão ampliada, conteúdo. Um sistema desenhado só por gente de visual vira guia de estilo com componentes.
- **Misturar quem faz e quem decide.** Contribuidores individuais para o trabalho diário, e pessoas de gestão para corrigir rota e liberar tempo de gente boa em rajadas curtas.
- **Investir em documentação e comunicação centralizadas.** Esta é a que mais falta em modelo federado: sem alguém com a responsabilidade explícita de documentar e comunicar, o sistema fica dormente mesmo com todo mundo participando.
- **Retribuir contribuição com autonomia.** À medida que o núcleo tolera mais divergência, mais gente contribui — e o ciclo se realimenta.

## Quem decide o que entra

A segunda metade é o fluxo. O de Frost tem dez passos; a espinha é esta:

![Fluxo de governança, do time de produto que começa pelo que já existe até a adoção, com a bifurcação entre floco de neve e padrão do sistema](attachments/design-system-fluxo-governanca.svg)

O passo zero, implícito, é o mais importante: o padrão é **usar o que já existe**. O fluxo só começa quando nada serve.

A bifurcação central é a pergunta de [[A anatomia em camadas]] — isto serve a quantos produtos? Se serve a um, fica no produto como receita ou floco de neve, e isso é um desfecho legítimo, não uma rejeição. Se serve a vários, entra no fluxo: protótipo barato, revisão conjunta com o time que pediu, construção e testes, documentação com versão, publicação, adoção.

O Primer, do GitHub, formaliza a mesma ideia em três estágios com critérios escritos. Um componente fica isolado no produto quando foi feito às pressas e tem problemas conhecidos, quando resolve um problema muito específico daquele time, ou quando é complexo demais para um caso que os outros produtos não têm. Sobe para "compartilhado" quando é muito provável que seja usado em mais de um produto, ou quando codifica um padrão que já existe espalhado e nunca foi destilado. E chega ao sistema quando, além disso, não depende de nada que só a aplicação de origem tem, e há acordo com quem mantém sobre prazo e capacidade.

Repare no que o Primer explicitamente **não** define: um número mágico de usos. A promoção depende de alinhamento estratégico e de capacidade de quem mantém, não de um contador. A regra de bolso que Laura Klein propõe, na NN/g, é do mesmo tipo — se a mudança ajudaria três times ou mais, provavelmente pertence ao sistema.

## Contribuição não é uma coisa só

O erro mais comum de processo é tratar toda contribuição com o mesmo rito. Nathan Curtis separa quatro níveis:

![A escala de contribuição: correção, melhoria pequena, melhoria grande e recurso novo, com custo crescente e frequência decrescente](attachments/design-system-escala-contribuicao.svg)

**Correção** de defeito em código, arquivo de design ou documentação. **Melhoria pequena**, sobre arquitetura estável — acrescentar uma cor a um alerta. **Melhoria grande**, que estende algo existente com vários atributos. **Recurso novo**, um componente que não existia.

As pequenas são frequentes e baratas e devem ser autônomas, frequentes e muito rápidas do começo ao fim. As grandes são raras e caras, exigem várias conversas para definir escopo e prioridade, e o design passa por uma ou duas rodadas.

Curtis aponta a fricção que nenhum processo resolve sozinho: um contribuidor costuma ser designer **ou** desenvolvedor, quase nunca os dois. Quanto maior a contribuição, mais isso pesa, porque metade do trabalho fica sem dono no meio do caminho. A resposta prática é emparelhar o contribuidor com alguém do núcleo da outra disciplina — e reconhecer que isso tem custo, em vez de fingir que "aceitar contribuições" é gratuito.

Os dados da Sparkbox de 2022 sugerem que essa é a área menos resolvida do ofício: 36% dos mantenedores não têm processo definido de contribuição, e — o número mais eloquente — apenas **33% estão satisfeitos** com a forma como lidam com contribuições hoje. Entre os sistemas considerados bem-sucedidos, 92% aceitavam contribuição de código e 83% de design.

## O papel de quem faz cumprir

Laura Klein defende que um sistema precisa de alguém com autoridade para fazê-lo valer, e a justificativa dela não é sobre disciplina, é sobre acúmulo. O exemplo: um carrossel de e-commerce que recebe pedidos pequenos de vários gerentes de produto, cada um razoável isoladamente, até existirem dezenas de variações — confusas para o cliente e impossíveis de manter.

O ponto é que cada time otimiza a própria métrica sem conseguir enxergar a consequência sistêmica. Quem mantém o sistema é a única pessoa em posição de ver isso. E há um benefício menos óbvio: designers precisam de respaldo quando um stakeholder empurra uma mudança ruim, e é muito mais fácil sustentar "isto contraria um princípio do sistema" do que "eu acho que não fica bom".

Mas Klein também descreve o fracasso do outro lado, e é o mais importante desta página. Um time protegia o sistema ferozmente de qualquer mudança — e a adoção era baixíssima. Depois de acelerar as revisões e passar a evoluir o sistema conforme as necessidades apareciam, a adoção disparou, porque os times passaram a confiar que o sistema cresceria junto com eles.

A conclusão que se tira daí é contraintuitiva e vale mais do que qualquer política escrita: **revisão lenta destrói mais adesão do que regra rígida.** Um "não" rápido e explicado mantém a conversa viva. Um "talvez" que leva três semanas ensina o time a nunca mais perguntar — e a partir daí a divergência não some, ela apenas deixa de ser visível.

Três práticas que decorrem disso:

- **Revisar junto, não auditar.** Sessão de trabalho, não inspeção.
- **Revisar na hora certa** — depois da exploração inicial, antes da implementação. Antes é cedo demais para haver o que discutir; depois é tarde demais para mudar sem custo.
- **Ter caminho de baixo atrito para contribuir**, para que a alternativa a pedir não seja fazer escondido.

---

**Continua em:** [[Adoção e maturidade]] · [[Versionar, depreciar, documentar]]

**Antes:** [[A anatomia em camadas]]
