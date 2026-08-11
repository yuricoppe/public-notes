---
title: "Adoção e maturidade"
description: "Por que adoção não é uma fase que termina, o que os sistemas bem-sucedidos fazem de diferente, e como medir sem cair em métrica de vaidade"
tags:
  - tema/design-system
  - tipo/artigo
---

Quase todo modelo de maturidade de design system desenha uma escada: primeiro constrói, depois documenta, depois as pessoas adotam. Huei-Hsin Wang, do Nielsen Norman Group, argumenta que essa forma esconde o problema mais do que descreve, por três razões.

**Maturidade não é unidirecional.** Muitos sistemas regridem por motivos fora do controle de quem os constrói: reestruturação, corte de orçamento, fusão que traz um sistema incompatível para dentro de casa.

**Não existe uma narrativa única.** Maturidade é contextual à escala e à cultura da organização — uma startup e uma empresa grande podem ambas chegar lá por caminhos que não se parecem.

**Adoção não é uma etapa.** Modelos lineares a colocam depois da construção; na prática, times em todos os estágios estão lutando com adesão o tempo todo.

## Seis dimensões, medidas separadamente

A alternativa proposta é avaliar seis dimensões de forma independente, cada uma numa escala de 1 a 5 — de *ausente* (esforço improvisado e dependente de indivíduos) a *excepcional* (maduro, em melhoria contínua, resiliente a mudanças grandes):

![As seis dimensões de maturidade: alinhamento organizacional, eficácia do time, robustez da infraestrutura, governança, suporte e adoção](attachments/design-system-seis-dimensoes.svg)

**Alinhamento organizacional** — como o sistema está posicionado, financiado e patrocinado. Se tem padrinho na liderança e orçamento estável.

**Eficácia do time** — se quem mantém tem capacidade, as disciplinas necessárias, práticas de colaboração e saúde para sustentar aquilo a longo prazo.

**Robustez da infraestrutura** — a qualidade e a completude do que existe: componentes, tokens, documentação, ferramentas, fundações visuais, implementações.

**Governança** — como se decide, como se lida com contribuição e com desvio, como se versiona.

**Suporte** — onboarding, canais de ajuda responsivos, comunicação, programas de advocacia, mecanismos de retorno. É o que torna o sistema descobrível e usável.

**Adoção** — quão amplamente os times usam, se usam corretamente, e se confiam que o sistema é confiável e continua evoluindo.

O valor de separar assim é diagnóstico. Um perfil muito comum é infraestrutura em 4 e suporte em 2 — um sistema tecnicamente bom que ninguém sabe usar. Nesse caso, construir mais componentes não move nada; a alavanca está em outra coluna. Uma escada única não deixaria isso aparecer.

Vale registrar a ressalva metodológica: o artigo descreve o framework a partir de conversas com times, sem informar quantos nem detalhar o método. É um instrumento de organização de conversa, não um resultado de pesquisa validado.

## O que os sistemas que funcionam fazem

Aqui há dado empírico melhor. A Sparkbox rodou pesquisas anuais sobre design systems; a de 2022 teve 219 respostas, 84% de mantenedores, com times espalhados por mais de vinte setores.

![Comparação entre o que todos os design systems têm e o que os declarados bem-sucedidos têm: onboarding, treino e suporte, processo de contribuição e critério do que entra](attachments/design-system-o-que-funciona.svg)

O contraste central: apenas **30%** de todos os respondentes ofereciam onboarding ou treino. Entre os que declararam o sistema bem-sucedido, **84%** ofereciam onboarding e **76%**, treino e suporte. A distância entre 30 e 84 é a maior de toda a pesquisa.

Outros números da mesma linha: entre os bem-sucedidos, 78% tinham processo definido para decidir o que entra e 76% tinham processo de contribuição. E, do lado de quem consome o sistema, 85% dos assinantes satisfeitos se sentiam apoiados por quem mantém.

Repare no que **não** aparece nessa lista: ter mais componentes, ter mais tokens, ter documentação mais bonita. A diferença entre os sistemas que funcionam e os que não funcionam está quase toda no que se faz **em volta** do acervo — ensinar, apoiar, responder, e ter regras conhecidas.

Do outro lado do balcão, os problemas que quem usa mais relata são coerentes com isso: documentação ruim (39%), **não saber em que estado a peça está** — se é antiga, quebrada ou ainda por vir (35%), recursos faltando (26%), organização ruim (26%).

O segundo item merece destaque porque é barato de resolver e quase nunca é resolvido: uma etiqueta de estado visível em cada componente. É o assunto de [[Versionar, depreciar, documentar]].

## Descoberta é metade da adoção

Um componente pode estar pronto, testado e documentado e ainda assim ser invisível — porque a pessoa não sabe que ele existe, não consegue encontrá-lo, ou não tem certeza de como aplicá-lo. Os três casos produzem o mesmo resultado: alguém constrói de novo.

Isso reposiciona o site de referência. Ele não é a documentação do sistema; é o produto pelo qual o sistema é consumido. Nomes de componentes previsíveis, busca que funciona, exemplos que dá para copiar, e a resposta para "quando **não** usar isto" ao lado de "como usar".

E reposiciona também o momento do onboarding. A pessoa que entra no time em março vai formar a opinião dela sobre o sistema na primeira semana. Se aprender que o caminho mais rápido é copiar a tela do lado, é isso que ela vai fazer pelos próximos dois anos.

## Medir sem enganar a si mesmo

Só **16%** dos respondentes da Sparkbox acompanhavam qualquer métrica de uso ou satisfação — o mesmo número do ano anterior. É a prática mais rara de todas, e é a que permite discutir o sistema com quem paga por ele.

As categorias que fazem sentido acompanhar:

**Uso e cobertura.** Uso é a largura da adoção — quais componentes são inseridos, com que frequência. Cobertura é a profundidade — que fatia da interface é feita de peças do sistema em vez de código próprio. São coisas diferentes e a segunda é a que importa mais.

**Destacamento (*detach*).** Com que frequência alguém descola uma instância para sobrescrevê-la. É o indicador antecedente mais útil que existe: destacamento alto costuma significar que o componente é rígido demais ou que falta alguma coisa. Mas a leitura precisa de cuidado — se o componente foi desenhado para ser customizado, destacamento alto pode ser exatamente o funcionamento previsto. O número sozinho não conclui nada; ele indica onde perguntar.

**Documentação.** Que páginas as pessoas procuram e onde elas desistem, o que revela as lacunas de orientação.

**Satisfação de quem usa.** A metade qualitativa, e a única que captura "eu uso porque sou obrigado" — que é um estado bem diferente de adoção.

Um cuidado geral: praticamente todos os números públicos de retorno de design system vêm de fornecedores de ferramenta ou de estudos de caso escritos pelo próprio time. Servem para conseguir orçamento; não servem como evidência. A comparação honesta é com a sua própria série ao longo do tempo.

E uma armadilha específica: contar componentes publicados como métrica de saúde. É a métrica mais fácil de coletar, a mais fácil de subir e a que menos diz — um sistema pode dobrar de tamanho e piorar, e frequentemente é exatamente isso que acontece.

---

**Continua em:** [[Versionar, depreciar, documentar]]

**Antes:** [[Governança e contribuição]] · [[O que é e quando não vale a pena]]
