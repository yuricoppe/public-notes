---
title: "Anotações dos artigos"
description: "Trechos e anotações de leitura sobre barra de busca, dropdown, carregamento, resultados e filtros"
tags:
  - tema/ux
  - dominio/busca
  - tipo/nota
---

**Fonte: [Search: Visible and Simple](https://www.nngroup.com/articles/search-visible-and-simple/)** · Nielsen Norman Group

---

Um comentário típico é: "Não quero ter que navegar neste site do jeito que eles querem. Só quero encontrar o que estou procurando." É por isso que muitos usuários vão direto para a função de busca **da página inicial** .

A busca também é uma válvula de escape para os usuários quando eles ficam presos na navegação. Quando não conseguem encontrar um lugar razoável para ir em seguida, frequentemente recorrem à função de busca do site. É por isso que você deve disponibilizar a busca em todas as páginas do site; não é possível prever onde os usuários estarão quando perceberem que estão perdidos.

## A pesquisa deve ser uma caixa

Os usuários costumam se movimentar de forma rápida e intensa quando buscam algo para pesquisar. Como vimos em estudos recentes, eles costumam vasculhar a página inicial em busca da _"caixinha onde posso digitar"._ Há muito tempo sabemos que [os usuários vasculham](https://www.nngroup.com/articles/why-web-users-scan-instead-reading/), e as implicações são claras:

- Nas páginas iniciais, a pesquisa deve ser um **campo de digitação e não um link.**
- Coloque a caixa de pesquisa no **topo da página**, geralmente no canto direito (embora o esquerdo funcione quase tão bem).
- O campo de entrada da pesquisa deve ser **amplo o suficiente** para conter a consulta típica; se a caixa for muito pequena, a consulta rolará e diminuirá a usabilidade.

---

## A Obsolescência da Busca na Internet

Considerando que a busca está se tornando obsoleta na internet, poderia-se pensar que os usuários desenvolveriam habilidades avançadas de busca. No entanto, a realidade é diferente.
Usuários típicos apresentam ==dificuldades significativas na reformulação de consultas==: se não obtiverem bons resultados na primeira tentativa, as tentativas subsequentes raramente são bem-sucedidas. Na verdade, muitos usuários costumam desistir. Um estudo recente que avaliou um grande grupo de pessoas realizando compras em vários sites de e-commerce revelou dados preocupantes sobre a taxa de sucesso das buscas:

- **Sucesso na busca**
    - Primeira consulta: 51%
    - Segunda consulta: 32%
    - Terceira consulta: 18%
Esses dados indicam que, se os usuários não encontrarem o resultado desejado na primeira consulta, as chances de sucesso em buscas adicionais diminuem consideravelmente. Para piorar, muitos usuários acabam não se esforçando para reformular as consultas; quase metade dos entrevistados que falharam na primeira busca desistiu imediatamente.
- As interfaces de busca poderiam apresentar maneiras simples de ampliar as consultas.
- A ênfase deve se concentrar em aumentar as chances de sucesso na primeira tentativa.

Se a lista de resultados parecer inadequada, é provável que abandonem o site completamente, optando por buscar resultados em mecanismos de busca externos, como o Google.

---

**Enfatize a capacidade do seu mecanismo de busca de lidar com consultas de uma única palavra** e consultas muito curtas de várias palavras e ainda produzir resultados de alta qualidade.==**Não ofereça busca avançada na página inicial.**== A busca avançada pode causar problemas para os usuários, pois eles invariavelmente a utilizam de forma errada. Quando fizer sentido, ofereça a busca avançada como uma opção para a qual os usuários podem acessar links na página de resultados da busca: "Não encontrou o que procurava? Experimente a busca avançada."

---

**Fonte: [Search UX Best Practices](https://www.pencilandpaper.io/articles/search-ux)** · Pencil & Paper

---

Mesmo em nossa era de IA, as pessoas ainda precisam procurar, encontrar e descobrir informações por meio de experiências de pesquisa.

---

**Qual é o estado dos seus dados?**

O que pode ser indexado? Os dados estão em boas condições para uma pesquisa eficaz? Há um profissional de dados responsável por garantir que seus dados estejam limpos? Ou muitos deles estão em mau estado? Isso pode limitar sua capacidade de tornar a experiência incrível.

---

É importante entender que há uma diferença entre:

- **Encontrar um resultado correto:**
    os usuários desejam se concentrar em algo específico que eles sabem que existe – por exemplo, ID da amostra: 12342-22
- **Encontrar uma variedade de resultados:**
    os usuários desejam analisar um conjunto de informações para comparar e contrastar potencialmente – por exemplo, “Amostras de sangue gene 125”
- **Não encontrar resultados:**
    os usuários querem usar a pesquisa para verificar algo que sabem que não deveria ser encontrado na pesquisa – por exemplo, “amostra duplicada 3201-000”
- **Encontrar “onde” querem ir:**
    Isso pode ser localizado em uma página específica (busca de localização) ou pode estar relacionado a chegar a um lugar em um aplicativo com muitos lugares nele – por exemplo, “amostras”

---

## **Melhores práticas da barra de pesquisa**

- Incluir um ícone de pesquisa que mostre aos usuários um estado de foco muito perceptível quando o cursor passa sobre ele (certifique-se de que o atalho de teclado para iniciar a pesquisa também seja bem pensado, especialmente em casos em que a pesquisa é uma ação comum)
- Incluir o estado de foco quando a entrada foi “clicada”
- Incluir algumas sugestões predefinidas no texto do espaço reservado (nos casos em que não está claro o que você pode pesquisar em um aplicativo)
- Inclua o que está sendo pesquisado no texto do espaço reservado. Ex.: pesquisar no site inteiro vs. pesquisar itens na tabela abaixo.
![png](../attachments/Pasted%20image%2020251105231928.png)

---

## **Melhores práticas do menu suspenso de pesquisa:**

- Incluir categorias de cabeçalho no menu suspenso para facilitar a digitalização
- Foco automático no principal resultado da pesquisa
- Incluir instruções de atalho nos resultados iniciais para acesso rápido aos resultados e à funcionalidade do aplicativo
- Permitir rolagem no menu suspenso de pesquisa
- Incluir feedback de carregamento mostra que o computador está pensando em algumas coisas – confira nosso artigo detalhado sobre **padrões de carregamento de UX**.
- Mostre como os resultados correspondem usando uma técnica de destaque

---

## **Melhores práticas de carregamento de pesquisa:**

- Use feedback de carregamento específico ao contexto – o que significa que o feedback de carregamento é adaptado para diferentes durações de espera.
[![](https://cdn.prod.website-files.com/65d605a3b4417479c154329f/65e19e1312c79a10b418752d_Screen-Recording-2023-09-06-at-2.08.11-PM.gif)](https://cdn.prod.website-files.com/65d605a3b4417479c154329f/65e19e1312c79a10b418752d_Screen-Recording-2023-09-06-at-2.08.11-PM.gif)

☝️ Dica rápida
Para conjuntos de dados enormes, pode não ser viável indexar todos os locais possíveis nos seus dados com a busca, mantendo-a razoavelmente ágil. Você pode considerar a opção de permitir que as pessoas selecionem um intervalo geral antes de iniciar uma busca, se isso for apropriado para seus usuários.

---

## **Melhores práticas para resultados de pesquisa**

- Incluir guias ao representar diferentes tipos de resultados de pesquisa (em diferentes objetos de dados)
- Incluir totais de correspondências feitas a partir da consulta inserida
- Certifique-se de que os acertos estejam destacados para mostrar onde a correspondência está
- Use paginação conforme necessário
- Inclua controles de filtragem e classificação para que as pessoas possam refinar ainda mais os resultados que procuram (consulte nosso [artigo sobre filtragem](https://pencilandpaper.io/articles/ux-pattern-analysis-enterprise-filtering/)) para se aprofundar nas nuances em torno dos filtros
- Incluir o feedback do estado vazio quando os resultados da pesquisa forem iguais a 0 – revise nosso artigo de padrões sobre [estados vazios](https://pencilandpaper.io/articles/ux-pattern-analysis-enterprise-filtering/) para mais práticas recomendadas.

---

## **Pesquisa Avançada**

A busca avançada envolve inserir uma lógica específica na sua consulta para especificar onde e como o sistema indexará o(s) banco(s) de dados para encontrar o que você precisa. Esse tipo de busca exige mais planejamento prévio para executar uma consulta eficaz.
Esse tipo de pesquisa tem características únicas em comparação a outras experiências de pesquisa:

1. **Critérios de inclusão**
    – a capacidade de especificar a sequência ou lógica que será incluída nos resultados
2. **Critérios de exclusão**
    – a capacidade de especificar a sequência ou lógica que será excluída dos resultados
3. **Critérios mutuamente exclusivos**
    (“ou”) – especificando duas ou mais coisas que podem não coexistir, por exemplo, contém “vermelho” ou “azul”.
4. **Critérios aditivos**
    (“e”) – especificando que vários critérios podem ser incluídos, por exemplo, tipo = Artigos, E fonte = acadêmico

---

## Erros Comuns de UX de Pesquisa

### 1. Má Qualidade do Resultado

Usuários testam sistemas por meio de buscas. Quando encontram resultados irrelevantes, a confiança diminui. Há ferramentas e tecnologias modernas que podem ajudar a melhorar essa experiência.

### 2. Falhas de Tempo e Pouco Feedback da Interface

O tempo é crucial na experiência de busca, pois envolve muitas microinterações. A atualização deve ser instantânea, evitando atrasos confusos. Para melhorar, considere desabilitar certas funções enquanto o usuário interage com a interface.

### 3. Falta de Capacidade de Descoberta

Os usuários frequentemente não sabem que dados estão disponíveis. É essencial que eles compreendam os dados no sistema, pois muitos softwares apresentam essa lacuna.

### 4. Representação Inadequada de Resultados

Resultados de pesquisa devem comunicar claramente as correspondências. É importante destacar como as correspondências se relacionam aos dados, ajudando os usuários a focar nos resultados relevantes.

### 5. Feedback Insuficiente

Mostrar que a busca está sendo processada é fundamental. Feedback de carregamento e estados vazios são necessários para evitar que os usuários pensem que o sistema falhou.

### 6. Pesquisa vs. Navegação

Não usar a busca como uma solução para problemas de navegação ruim é crucial. Nem todos utilizam a busca como principal meio de navegação. A busca não substitui uma navegação sólida, e depender dela pode resultar em uma experiência de usuário insatisfatória.

---

**Fonte: [Search UX best practices: a complete guide](https://nulab.com/learn/design-and-ux/search-ux-best-practices/)** · Nulab

---

### Participe das pesquisas em alta

Imagine fazer login e ver imediatamente o que está em alta no momento. As buscas por tendências não só ajudam os usuários a descobrir conteúdo popular, como também criam um senso de comunidade, mostrando o que os outros estão interagindo. Quando os usuários veem uma lista de tópicos em alta, isso desperta sua curiosidade, convidando-os a aderir à onda ou explorar novas áreas de interesse.


---

### Ofereça sugestões alternativas para resultados de estado vazio

Quando os usuários digitam algo e não obtêm “nenhum resultado”, oferecer sugestões alternativas pode melhorar muito a experiência deles. Uma abordagem é ter um banco de palavras e frases com erros ortográficos comuns e sugerir de forma inteligente o que eles podem estar tentando encontrar. Você também pode usar um sistema de recomendação de conteúdo personalizado que analisa as interações, preferências e comportamentos anteriores do usuário.


Ao entender com o que os usuários se envolveram anteriormente, você pode recomendar conteúdo relacionado que reflita os interesses deles, aumentando a probabilidade de exploração contínua.
Também é uma boa ideia categorizar o conteúdo em grupos temáticos. Se a busca por "sobremesa vegana" não retornar resultados, considere sugerir uma categoria geral, como "receitas veganas" ou "sobremesas do mundo todo". Esse método amplia o escopo de conteúdo potencial, mas também incentiva os usuários a explorar categorias que talvez não tivessem considerado inicialmente.
Utilizar conteúdo gerado pelo usuário é outra estratégia eficaz. Destaque postagens populares ou contribuições de outros usuários relacionadas ao tópico de pesquisa para criar um senso de envolvimento da comunidade e despertar o interesse.

---

### Crie guias para diferentes tipos de resultados de pesquisa

Adicionar abas para representar vários objetos de dados pode tornar os resultados mais claros. Por exemplo, se uma consulta de pesquisa apresentar resultados para produtos e artigos, abas separadas permitem que os usuários filtrem rapidamente essas categorias sem precisar rolar infinitamente por uma lista mista.
Cada aba deve ser claramente identificada (por exemplo, "Produtos", "Artigos", "Contas") para simplificar a navegação. Isso ajuda os usuários a localizar as informações desejadas rapidamente, ao mesmo tempo em que oferece uma indicação visual que organiza os resultados de forma fácil de assimilar, o que reduz a carga cognitiva. Boas notícias para a paciência dos seus visitantes.

---

**Fonte: [Best practices for search results](https://uxplanet.org/best-practices-for-search-results-1bbed9d7a311)** · UX Planet

---

## **1. Não apague a consulta dos usuários depois que eles clicarem no botão Pesquisar**

_Mantenha o texto original visível no campo de entrada de pesquisa._ A reformulação da consulta é uma etapa crucial no processo de pesquisa. Se os usuários não encontrarem o que procuram na primeira tentativa, talvez queiram pesquisar novamente usando uma consulta ligeiramente diferente. Para facilitar, deixe a consulta inicial na caixa de pesquisa para que não precisem digitar a consulta inteira novamente.

## **3. Use autossugestão eficaz**

Se o seu site usa o mecanismo de sugestão automática para entrada de pesquisa, você precisa garantir que esse mecanismo seja útil para os seus usuários. A sugestão automática deve ajudar os usuários a acelerar o processo de pesquisa, mantendo-os focados na conversão.
[![](https://miro.medium.com/v2/resize:fit:600/1*AQFWWqXrznprydFeOL-axg.png)](https://miro.medium.com/v2/resize:fit:600/1*AQFWWqXrznprydFeOL-axg.png)

Créditos da imagem: ThinkWithGoogle

## **4. Corrija erros de digitação**

_A digitação é propensa a erros._ Se um usuário digitar um termo de pesquisa incorretamente e você conseguir detectar isso, tente adivinhar o que ele quer dizer e pesquise por ele. Isso evitará a frustração que seus usuários terão ao não verem uma página de resultados.
[![](https://miro.medium.com/v2/resize:fit:700/1*U3xATz5_lkAgYsjJXNlH7g.png)](https://miro.medium.com/v2/resize:fit:700/1*U3xATz5_lkAgYsjJXNlH7g.png)

_Não há suporte para reformulação de consultas na página de resultados zero da Apple Store_

[![](https://miro.medium.com/v2/resize:fit:700/1*i0oGvymAq0dl7rhLjdLvug.png)](https://miro.medium.com/v2/resize:fit:700/1*i0oGvymAq0dl7rhLjdLvug.png)

A Asos faz um bom trabalho ao exibir resultados alternativos quando ocorre um erro de digitação, sem ofender o usuário. A mensagem é sutil, como "também pesquisamos por Overcoats", com o termo de busca original "Overcoatt".

## **5. Mostrar o número de resultados da pesquisa**

Quando os usuários veem o número de itens de pesquisa, essa informação torna mais fácil para eles decidirem quanto tempo desejam gastar procurando os resultados.

[![](https://miro.medium.com/v2/resize:fit:700/1*WC83Jp1xpJtLdMbuc5hhiQ.png)](https://miro.medium.com/v2/resize:fit:700/1*WC83Jp1xpJtLdMbuc5hhiQ.png)

O número de resultados correspondentes ajuda o usuário a fazer reformulações de consulta mais informadas.

## **6. Mantenha as consultas de pesquisa recentes dos usuários**

A formulação de consultas exige algum esforço. Mesmo quando os usuários sabem o que pesquisaram na última vez que visitaram seu site, eles ainda precisam se lembrar de informações. Ao projetar uma experiência de pesquisa, você deve ter em mente uma regra básica de usabilidade:
**Dica:** Apresente menos de 10 consultas para que as informações não fiquem muito confusas. Para dispositivos móveis, é melhor mostrar de 3 a 5 consultas.

---

**Pontos:**

- Não oculte o recurso de classificação dentro do recurso de filtragem — são tarefas diferentes.
- Destaque claramente os filtros ativados. Os usuários sabem quais filtros estão ativos.

---

**Fonte: [Search results page design: UI/UX best practices](https://medium.com/@halolab/search-results-page-design-ui-ux-best-practices-f2157eea8226)** · Halo Lab

---

## **Responda às perguntas do seu cliente**

Imagine que você visita uma loja online e procura um cardigã cottagecore. Ele não está mais disponível, então, após inserir a consulta, você recebe um cardigã simples que não atende às suas necessidades. Além disso, não há uma única palavra relacionada às suas necessidades. Isso pode ser bastante desagradável, irritante e cansativo. A maneira de evitar essa situação difícil é fornecer detalhes sobre os itens faltantes e dados sobre sua disponibilidade. Permitir que os usuários enviem uma solicitação para serem notificados quando o item estiver de volta à loja também é uma boa ideia.
O objetivo do site, nesse sentido, é ser um representante de vendas informal. Tente antecipar o máximo possível de perguntas adicionais e respondê-las proativamente. Lembre-se, no entanto, de que suas sugestões são apenas uma alternativa se não atenderem às necessidades dos clientes em sua totalidade.

---

Como um mecanismo de busca que utiliza busca semântica, o DuckDuckGo exibe todos os significados das palavras-chave entre os primeiros resultados. Mais importante ainda, ele também possui um painel extra que permite visualizar alternativas, atendendo assim às necessidades dos clientes e criando seu próprio campo de informações.

---

**Fonte: [5 Proven UX Strategies For “No Results” Pages](https://baymard.com/blog/no-results-page)** · Baymard

---

## **Dicas de pesquisa por si só não são suficientes**

[![](https://baymard-assets-cdn.imgix.net/research/media_files/attachments/140071/original/research-media-file-2ff20004e421e20c3b38796f2599828e.png?auto=format&dpr=2&fit=max&q=50&w=880)](https://baymard-assets-cdn.imgix.net/research/media_files/attachments/140071/original/research-media-file-2ff20004e421e20c3b38796f2599828e.png?auto=format&dpr=2&fit=max&q=50&w=880)

Na [Marks & Spencer](https://baymard.com/ux-benchmark/case-studies/marks-spencer) , os usuários recebem o incentivo de _"Não desista!"_ e recebem conselhos que muitas vezes são ignorados. Sem migalhas relevantes para seguir, os usuários muitas vezes perdem a vontade de permanecer no site.
Mesmo quando os usuários leem as dicas, muitas vezes eles **ficam presos** — sem saber qual termo está escrito errado ou desconhecem os termos alternativos preferidos do site.

---

Primeiro, sugira **uma ou mais categorias** relacionadas à consulta de pesquisa do usuário para ajudá-lo a explorar alternativas.
Por exemplo, se uma busca por “jaquetas vermelhas de inverno” não retornar resultados, sugira um link para a categoria mais ampla “jaquetas” — ou melhor ainda, um **link para uma lista de produtos** de “jaquetas” com o filtro “inverno” aplicado.
**Sugestões de categorias** associadas a palavras na pesquisa do usuário podem levá-los a explorar o que está disponível em uma categoria ou lista de produtos e trabalhar a partir daí.

---

## **Sugira pesquisas alternativas**

[![](https://baymard-assets-cdn.imgix.net/research/media_files/attachments/140412/original/research-media-file-bf4faabda3afc50f6c5ba5c59f3be0d3.png?auto=format&dpr=2&fit=max&q=50&w=880)](https://baymard-assets-cdn.imgix.net/research/media_files/attachments/140412/original/research-media-file-bf4faabda3afc50f6c5ba5c59f3be0d3.png?auto=format&dpr=2&fit=max&q=50&w=880)

[A Crate & Barrel](https://baymard.com/ux-benchmark/case-studies/crate-barrel) exibe diversas _“Pesquisas relacionadas”_ aproveitando a palavra _“breville”_ na consulta do usuário, fornecendo um caminho para produtos daquela marca.
Para máxima eficácia, **exiba uma prévia** dos 3 a 5 principais produtos para cada consulta alternativa, dando aos usuários uma rápida visão geral do que está disponível.
Se apenas uma consulta alternativa for encontrada, ela deverá ser **aplicada automaticamente,** com um aviso explicando que não havia resultados disponíveis para a consulta original, mas o site encontrou resultados relevantes para a pesquisa revisada.

---

**Fonte: [Ecommerce Search UX Best Practices](https://baymard.com/blog/ecommerce-search-query-types)** · Baymard

---

### **Pontos Principais**

- 33% dos sites apresentam problemas em realizar "Buscas Exatas", onde os usuários devem encontrar produtos pelo nome ou número do modelo.
- 29% dos sites falham na "Busca por Tipo de Produto", dificultando que usuários acessem facilmente categorias desejadas.
- "Buscas por Características" são mal geridas em 34% dos sites, não permitindo que atributos de produtos sejam usados nas pesquisas.
- 36% dos sites têm dificuldades em lidar com "Buscas por Caso de Uso", onde os usuários pesquisam produtos de acordo com situações específicas.
- "Buscas por Abreviação e Símbolo" demonstram ser problemáticas em 50% dos sites, onde diferentes versões de termos não retornam os mesmos resultados.
- 31% dos sites não suportam "Buscas por Compatibilidade", dificultando que usuários encontrem acessórios e peças compatíveis com produtos que possuem.
- ==38% dos sites apresentam problemas com "Buscas por Sintomas", onde usuários procuram soluções para problemas sem saber exatamente quais produtos buscar.==
- "Buscas Não-Produto" falham em 50% dos sites, negligenciando a necessidade de informações como políticas de retorno e ajuda do cliente.

---

**Fonte: [Enriched Site-Search Suggestions: Rarely Used](https://www.nngroup.com/articles/enriched-site-search-suggestions/)** · Nielsen Norman Group

---

==**As pessoas raramente interagem com sugestões de pesquisa enriquecida em sites.**== Embora esses tipos de recomendações possam fornecer atalhos rápidos e validação útil para usuários que realizam pesquisas de itens conhecidos, considere se o investimento vale a pena para fazê-lo corretamente. Sugestões de pesquisa enriquecidas em excesso, lentas para carregar ou instáveis aumentam a complexidade da tarefa, contribuem para uma baixa [relação sinal-ruído](https://www.nngroup.com/articles/signal-noise-ratio/) e são amplamente ignoradas.
Ao implementar sugestões de pesquisa de site enriquecidas, siga estas diretrizes para garantir que essa funcionalidade ajude, em vez de atrapalhar, os usuários em suas tarefas de pesquisa:

- Não elimine sugestões automáticas de texto simples. Os usuários utilizam bastante essas sugestões básicas de pesquisa no site, mesmo quando sugestões de pesquisa enriquecidas estão presentes.
- Limite a quantidade de conteúdo gráfico e dinâmico, o que pode causar tempos de carregamento mais lentos e contribuir para a cegueira de banner.
- Identifique claramente os tipos de sugestões enriquecidas (por exemplo, mais vendidos, produtos recomendados, pesquisas recentes) para que os usuários não precisem adivinhar o que estão vendo ou por que aquilo está sendo exibido. (Quando deixados para adivinhar, os usuários interpretam esses resultados como conteúdo promocional.)
- Mantenha espaços dedicados para vários tipos de conteúdo (em vez de mudar a localização de tipos específicos de sugestões de pesquisa de site enriquecidas com base em consultas).
- Não presuma que usuários regulares do site aprenderão a usar sugestões de pesquisa enriquecidas com o tempo. Em nosso estudo, os usuários não notaram nem usaram sugestões de pesquisa enriquecidas, mesmo após realizar várias pesquisas ao longo do tempo em um site.
