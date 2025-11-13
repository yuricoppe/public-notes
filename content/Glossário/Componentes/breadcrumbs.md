# Breadcrumbs (Migalhas de Pão)

Breadcrumbs são um sistema de navegação secundário que mostra a localização do usuário em um site ou aplicativo. Eles ajudam o usuário a entender a hierarquia da informação e a navegar de volta para níveis anteriores.

## Casos de Uso

-   Sites com estrutura hierárquica profunda (mais de dois níveis).
-   Aplicações web complexas com múltiplas seções e subseções.
-   Documentação e bases de conhecimento.

## Tipos de Breadcrumbs

1.  **Baseados em Localização (Location-based):**
    *   Mostram onde o usuário está na hierarquia do site. São os mais comuns.
    *   Exemplo: `Home > Produtos > Eletrônicos > Smartphones`

2.  **Baseados em Caminho/Histórico (Path-based/History-based):**
    *   Mostram o caminho que o usuário percorreu para chegar à página atual. São dinâmicos.
    *   Exemplo: `Página Anterior > Página Anterior > Página Atual` (Menos comum para navegação principal, mais para processos lineares).

3.  **Baseados em Atributo (Attribute-based):**
    *   Mostram atributos ou [[Glossário/Componentes/filters|filtros]] selecionados para chegar a um conjunto de resultados (comum em e-commerce).
    *   Exemplo: `Home > Roupas > Camisetas > Tamanho: M > Cor: Azul`

## Melhores Práticas

-   **Posicionamento:** Geralmente no topo da área de conteúdo principal, abaixo do [[Glossário/Elementos/cabecalhos|cabeçalho]] principal e acima do título da página.
-   **Separador:** Usar um separador visual claro entre os links (ex: `>`, `/`, `»`). O `>` é o mais comum e reconhecido.
-   **[[Glossário/Elementos/links|Link]] para Home:** O primeiro item deve ser quase sempre um [[Glossário/Elementos/links|link]] para a página inicial.
-   **Página Atual:** O último item representa a página atual. Geralmente não é um [[Glossário/Elementos/links|link]], mas texto simples em destaque (ex: negrito) para indicar a localização ativa.
-   **Clareza:** Usar títulos de página concisos e descritivos.
-   **Não Substituir Navegação Primária:** Breadcrumbs são um auxílio, não devem substituir a navegação principal do site.
-   **Responsividade:** Em telas pequenas, podem ser truncados, roláveis horizontalmente, ou o primeiro/último item pode ser priorizado.
-   **Acessibilidade (a11y):**
    *   Envolver os breadcrumbs em um elemento `<nav>` com um `aria-label="Breadcrumb"` (ou o equivalente em português, como "Trilha de navegação").
    *   Usar uma [[Glossário/Elementos/listas|lista]] ordenada (`<ol>`) ou não ordenada (`<ul>`) para os itens, pois representam uma sequência ou conjunto de [[Glossário/Elementos/links|links]] de navegação.
    *   Para o item da página atual que não é um link, usar `aria-current="page"`.

## Variações de Estilo

-   Tamanho da fonte.
-   [[Glossário/Linguagem Visual/cor|Cor]] dos [[Glossário/Elementos/links|links]] e do texto da página atual.
-   Estilo do separador.

## Exemplos

```html
<nav aria-label="Trilha de navegação">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="/">Home</a></li>
    <li class="breadcrumb-item"><a href="/produtos/">Produtos</a></li>
    <li class="breadcrumb-item active" aria-current="page">Smartphones</li>
  </ol>
</nav>
```

## O Que Evitar

-   Usar breadcrumbs para navegação em um único nível ou em sites muito rasos.
-   Usar breadcrumbs baseados em histórico para navegação primária, pois pode ser confuso.
-   Tornar o item da página atual um [[Glossário/Elementos/links|link]] para si mesmo. 