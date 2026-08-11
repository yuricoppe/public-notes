---
title: "A anatomia em camadas"
description: "Onde cada coisa mora: o núcleo, as receitas, os flocos de neve — e por que quase todo componente que um time quer promover não deveria subir"
tags:
  - tema/design-system
  - tipo/artigo
---

A pergunta que mais consome tempo em time de design system não é como desenhar um componente. É se aquilo ali é um componente do sistema. Ela reaparece toda semana, é decidida no improviso, e o resultado acumulado de decidi-la mal é um sistema inchado de coisas que um produto só usa — ou um sistema anêmico do qual todo mundo escapa.

Existe vocabulário para resolver isso, e ele é o assunto desta página.

## As camadas

Brad Frost descreve o ecossistema como um bolo de camadas, em que cada uma acima da primeira é opcional:

![As camadas do ecossistema de design system, da base de padrões web até o produto, com influência nos dois sentidos](attachments/design-system-camadas.svg)

Na base estão HTML, CSS e os padrões da plataforma. Acima deles, o **núcleo do design system**, que contém quatro ativos:

- **Tokens** — as definições de baixo nível: cor, tipografia, espaçamento. As variáveis da marca.
- **Ícones** — que podem viver junto dos tokens ou separados.
- **Componentes de UI** — o que todo mundo pensa quando ouve "design system".
- **Site de referência** — parte site de marketing, parte documentação. É a vitrine, e é o que faz o resto ser encontrável.

As camadas seguintes só entram quando aparece uma necessidade real: implementações específicas por tecnologia (quando há mais de uma stack a servir), receitas, componentes inteligentes — os que embrulham lógica e dados — e, no topo, o produto.

O detalhe que mais importa nesse desenho não é a ordem das camadas. É a seta: **o sistema informa os produtos e os produtos informam o sistema.** Um design system que só empurra para baixo é um sistema que vai envelhecer sozinho até virar aquilo de que todo mundo escapa.

## Componente, receita, floco de neve

Dentro dessa estrutura, Frost nomeia três categorias que resolvem a briga semanal:

![Comparação entre componente de design system, receita e floco de neve, com exemplos e onde cada um mora](attachments/design-system-componente-receita-floco.svg)

**Componente de design system** é compartilhado, agnóstico de conteúdo e de contexto, construído para reuso máximo. Botão, Card, Select, Accordion. Mora na biblioteca publicada.

**Receita** é uma composição de componentes do sistema, reutilizada de forma consistente dentro de **um** produto, mas sem generalidade suficiente para o sistema. `CartaoDeProduto`, `CampoDeNome`. Frost é explícito: são componentes valiosos e reutilizáveis, que podem se aplicar a um produto só.

**Floco de neve** é a peça de uso único, necessária para construir o produto e que não se repete fora do primeiro caso de uso. O exemplo dele é um componente `Seat`, de seleção de poltrona numa companhia aérea.

A pergunta que decide não é "isto está bem feito?" nem "isto poderia ser útil para outros?". É **quantos produtos precisam disto hoje**. E as duas respostas incômodas — "só o meu" e "só esta tela" — são respostas legítimas, não falhas de ambição.

Duas coisas quebram quando esse vocabulário não existe. A primeira é o sistema virar depósito: entra tudo que alguém achou reutilizável, e o time central passa a manter dezenas de componentes com um consumidor cada. A segunda é o oposto e mais silenciosa — se o sistema não admite que flocos existam, os times fazem flocos assim mesmo, só que escondidos, sem revisão e sem acessibilidade.

O arranjo prático que Frost descreve separa isso no próprio repositório: a biblioteca publicável fica em `src/components`, e receitas, páginas e flocos ficam num diretório de vitrine. O sinal é claro: quero mostrar isto, mas isto não é parte oficial do sistema.

## Sobre atomic design

Vale uma nota, porque é a referência mais citada e a mais mal aplicada.

O *atomic design* — átomos, moléculas, organismos, templates, páginas — é uma metodologia para pensar interfaces como hierarquia de composição, e nasceu como argumento para construir sistemas em vez de páginas. Como modelo mental, continua funcionando.

Como **arquitetura de pastas**, costuma dar errado. A discussão sobre se um campo de busca é molécula ou organismo é um debate sem prêmio: consome reunião, não muda o código e cria um imposto de classificação sobre cada componente novo. As categorias de Frost descritas acima — componente, receita, floco — são posteriores e mais úteis no dia a dia justamente porque a pergunta que fazem é sobre **alcance**, que tem consequência prática, e não sobre tamanho, que não tem.

## O sistema global

Uma ideia mais ampla, e que vale conhecer mesmo sem poder agir sobre ela.

Em janeiro de 2024, Frost publicou a proposta de um **Global Design System**: uma biblioteca comum de componentes de UI disponível para toda a web. O argumento parte de um paradoxo. Organizações criaram design systems para eliminar duplicação interna; o efeito agregado foi criar duplicação em outro nível, com um número enorme de pessoas dedicando tempo a desenhar, construir, documentar e manter exatamente o mesmo conjunto de componentes comuns — acordeão, seletor de data, abas, campos de formulário, alertas, diálogos — que assumem a mesma forma geral independentemente de servirem a um banco, a uma agência pública ou a um jornal.

O argumento seguinte é de acessibilidade, e é o mais forte. Frost cita que **nenhum** dos cem sites mais acessados usa HTML válido, e que o levantamento WebAIM Million encontrou quase 50 milhões de erros distintos de acessibilidade nas páginas iniciais do primeiro milhão de sites — em torno de 50 erros por página. A leitura dele: repetir a construção dos mesmos componentes em toda organização do planeta garante que os mesmos erros sejam recriados em toda organização do planeta, e quinze anos pedindo para que desenvolvedores priorizem acessibilidade não resolveram isso.

O que a proposta explicitamente **não** inclui é estética: seria uma base sem estilo além do padrão do navegador, cobrindo a maioria dos casos e não todos.

Ela ainda não existe. Mas a ideia é útil como critério mesmo dentro de uma organização: quanto mais um componente se parece com um controle genérico da plataforma, menos ele merece ser reinventado — e mais faz sentido embrulhar algo existente e bem testado em vez de escrever do zero.

## Um princípio para fechar

A Lei de Gall, que Frost usa para justificar as camadas opcionais: um sistema complexo que funciona invariavelmente evoluiu de um sistema simples que funcionava. Sistemas complexos projetados do zero não funcionam e não podem ser consertados até virarem simples.

Na prática isso significa resistir a três tentações comuns no começo: criar a camada de implementação por tecnologia antes de existir a segunda stack; criar a categoria de componente inteligente antes de existir o segundo caso; e escrever a documentação da estrutura antes de existir a estrutura.

---

**Continua em:** [[Governança e contribuição]] · [[Versionar, depreciar, documentar]]

**Antes:** [[O que é e quando não vale a pena]] · **Ver também:** [[Tokens]]
