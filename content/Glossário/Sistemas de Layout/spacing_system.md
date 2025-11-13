# Sistema de [[Glossário/Linguagem Visual/espacamento|Espaçamento]] ([[Glossário/Linguagem Visual/espacamento|Spacing]] System)

## Descrição Geral
O sistema de [[Glossário/Linguagem Visual/espacamento|espaçamento]] define uma escala consistente e previsível para aplicar margens (`margin`), preenchimentos (`padding`) e o espaço vazio (`white space`) entre os elementos da interface do usuário. Um sistema de [[Glossário/Linguagem Visual/espacamento|espaçamento]] bem definido é crucial para criar layouts visualmente harmoniosos, melhorar a legibilidade e garantir uma hierarquia visual clara.

## Princípios Chave
- **Consistência:** Usar uma escala predefinida em vez de valores arbitrários.
- **Hierarquia Visual:** O [[Glossário/Linguagem Visual/espacamento|espaçamento]] ajuda a agrupar elementos relacionados e a separar os não relacionados, guiando o olho do usuário.
- **Ritmo Vertical e Horizontal:** Contribui para um fluxo visual agradável.
- **Manutenibilidade:** Facilita a aplicação e o ajuste de espaçamentos em todo o portal.

## Nossa Escala de [[Glossário/Linguagem Visual/espacamento|Espaçamento]]

Nossa escala é baseada em um **valor fundamental de 4px**. Múltiplos deste valor são usados para definir os diferentes níveis de [[Glossário/Linguagem Visual/espacamento|espaçamento]]. Isso proporciona flexibilidade suficiente enquanto mantém a consistência.

| Token/Variável (Exemplo) | Valor (px) | Uso Comum                                                               |
|--------------------------|------------|-------------------------------------------------------------------------|
| `space-xxs`              | 4px        | [[Glossário/Linguagem Visual/espacamento|Espaçamento]] mínimo, entre [[Glossário/Linguagem Visual/iconografia|ícones]] e texto adjacente, pequenos ajustes.   |
| `space-xs`               | 8px        | Pequeno [[Glossário/Linguagem Visual/espacamento|espaçamento]], entre itens de uma [[Glossário/Elementos/listas|lista]] compacta, paddings internos. |
| `space-sm`               | 12px       | [[Glossário/Linguagem Visual/espacamento|Espaçamento]] pequeno-médio.                                              |
| `space-md` (base)        | 16px       | [[Glossário/Linguagem Visual/espacamento|Espaçamento]] padrão, margens de [[Glossário/Elementos/paragrafo|parágrafos]], padding de [[Glossário/Componentes/cards|cards]].             |
| `space-lg`               | 24px       | [[Glossário/Linguagem Visual/espacamento|Espaçamento]] grande, entre seções de conteúdo distintas, margens de títulos. |
| `space-xl`               | 32px       | [[Glossário/Linguagem Visual/espacamento|Espaçamento]] extra grande, separação de blocos maiores de layout.          |
| `space-xxl`              | 48px       | [[Glossário/Linguagem Visual/espacamento|Espaçamento]] muito grande, para ênfase ou separação significativa.       |
| `space-xxxl`             | 64px       | [[Glossário/Linguagem Visual/espacamento|Espaçamento]] máximo, grandes áreas de respiro.                             |

**Nota:** Estes são exemplos de tokens. Os nomes exatos das variáveis (ex: em CSS/Sass) podem variar, mas devem seguir essa progressão.

## Como Implementar

**Exemplo (Conceitual em CSS com Variáveis):**

```css
:root {
  --space-xxs: 4px;
  --space-xs: 8px;
  --space-sm: 12px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
  --space-xxl: 48px;
  --space-xxxl: 64px;
}

.meu-componente {
  padding: var(--space-md);
  margin-bottom: var(--space-lg);
}

.meu-componente .titulo {
  margin-bottom: var(--space-xs);
}

.item-[[Glossário/Elementos/listas|lista]] + .item-[[Glossário/Elementos/listas|lista]] {
  margin-top: var(--space-sm); /* [[Glossário/Linguagem Visual/espacamento|Espaçamento]] entre itens de lista */
}
```

## Diretrizes de Uso
- **Use a Escala:** Sempre que possível, utilize os valores definidos na escala de [[Glossário/Linguagem Visual/espacamento|espaçamento]] em vez de valores customizados.
- **Consistência Vertical e Horizontal:** Tente manter um ritmo consistente. Se um card tem `padding: 16px` (space-md), outros [[Glossário/Componentes/cards|cards]] similares também deveriam ter.
- **Relação com o Grid:** O sistema de [[Glossário/Linguagem Visual/espacamento|espaçamento]] complementa o [[Glossário/Sistemas de Layout/grid_system|sistema de grid]]. Os gutters do grid são uma forma de [[Glossário/Linguagem Visual/espacamento|espaçamento]], mas o sistema de [[Glossário/Linguagem Visual/espacamento|espaçamento]] se aplica de forma mais granular.
- **Espaço em Branco é Importante:** Não tenha medo de usar espaçamentos maiores (ex: `space-xl`, `space-xxl`) para criar áreas de respiro e separar seções de conteúdo distintas. Isso melhora a legibilidade e o foco.
- **Ajustes Responsivos:** Em alguns casos, os valores de [[Glossário/Linguagem Visual/espacamento|espaçamento]] podem precisar ser ajustados em diferentes breakpoints (`breakpoints.md`) para otimizar o layout em telas menores. Por exemplo, `margin-bottom: var(--space-lg)` em desktop pode se tornar `margin-bottom: var(--space-md)` em mobile.

## Densidade da Informação
- A escolha do nível de [[Glossário/Linguagem Visual/espacamento|espaçamento]] afeta a densidade da informação. Interfaces mais densas podem usar valores menores da escala, enquanto interfaces que priorizam o respiro e o foco em menos elementos usarão valores maiores.
- A densidade deve ser apropriada para o contexto e o objetivo da página ou componente.

## Ferramentas
- Utilizar variáveis CSS ou tokens de design em ferramentas como Figma para garantir a aplicação consistente da escala.

## Recursos Adicionais / Figma
- [[[Glossário/Elementos/links|Link]] para a documentação da Escala de [[Glossário/Linguagem Visual/espacamento|Espaçamento]] no Figma]
- [Exemplos de componentes e layouts aplicando a escala] 