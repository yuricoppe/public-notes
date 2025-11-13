# Tipografia (Typography)

## Onde é usado

A tipografia é crucial para a comunicação eficaz, legibilidade e a estética geral de uma interface. Ela é aplicada em:
- Todos os textos: títulos, parágrafos, legendas, rótulos, links, botões.
- Para estabelecer hierarquia visual clara, guiando o usuário pelo conteúdo.
- Para garantir a acessibilidade, permitindo que o texto seja facilmente lido e compreendido por todos os usuários, incluindo aqueles com deficiências visuais.
- Para reforçar a identidade da marca e o tom de voz do produto.

Define as famílias tipográficas, pesos, tamanhos, alturas de linha e espaçamento entre letras para todos os textos do sistema, assegurando legibilidade, hierarquia visual e consistência.

## Detalhes Adicionais / Tópicos

### Famílias Tipográficas (Font Families)
- Especificar as fontes primárias e secundárias (se houver).
- Incluir fontes de fallback (web safe fonts) caso a principal não carregue.
- *Exemplo:* `font-family: 'NomeDaFontePrincipal', 'NomeDaFonteSecundaria', Arial, sans-serif;`

### Escala Tipográfica
- Definir uma escala modular para tamanhos de fonte (ex: baseada em uma proporção como 1.2 ou 1.4) para criar harmonia e consistência entre os diferentes níveis de texto.
- A escala deve incluir tamanhos para H1, H2, H3, H4, H5, H6, parágrafos, texto de destaque (lead), legendas, texto pequeno (small), etc.

### Pesos e Estilos (Weights & Types)
- Documentar os pesos disponíveis da família tipográfica (Light, Regular, Medium, Semibold, Bold, Black, etc.) e quando usar cada um.
- Definir o uso de estilos como Itálico (para ênfase, citações) e Normal.

### Altura da Linha (Line Height)
- Essencial para legibilidade, especialmente em blocos de texto longos.
- Geralmente definida como um múltiplo do tamanho da fonte (ex: 1.4 a 1.8).
- Deve haver espaço suficiente entre as linhas para evitar que o texto pareça apertado.

### Comprimento da Linha (Line Length / Measure)
- O número ideal de caracteres por linha para conforto de leitura (geralmente entre 45-75 caracteres).

### Espaçamento entre Letras (Letter Spacing / Tracking)
- Ajustes sutis podem ser necessários para títulos ou textos em caixa alta para melhorar a legibilidade.

### Web Fonts
- Especificar como as fontes são carregadas (ex: `@font-face`, Google Fonts API).
- Considerar o impacto no desempenho e otimizar o carregamento (ex: `font-display: swap;`).

### Grid de Linha de Base (Baseline Grid)
- Um sistema de linhas horizontais invisíveis que ajuda a alinhar verticalmente o texto e outros elementos, criando um ritmo vertical consistente.

### Acessibilidade
- Tamanho mínimo de fonte para corpo de texto (geralmente 16px CSS).
- Contraste adequado entre texto e fundo (ver documentação de `Cor`).
- Permitir que os usuários redimensionem o texto sem quebra de layout.

## Variações de Aplicação (Exemplos)

- **Título Principal (H1):**
  - Descrição: Usado para o título mais importante da página ou seção. Deve ser único por página.
  - Família: [Nome da Fonte Principal]
  - Peso: [Ex: Bold ou Black]
  - Tamanho: [Ex: 2.5rem / 40px]
  - Altura de Linha: [Ex: 1.2]
  - Margem Inferior: [Ex: 1.5rem]
  - Outras Propriedades: [Ex: `text-transform: uppercase;` - se aplicável]
  - Status: A definir
  - Link para o Figma: [Link para H1 no Figma]

- **Corpo de Texto (Paragraph):**
  - Descrição: Usado para blocos de texto principais, como artigos e descrições detalhadas.
  - Família: [Nome da Fonte de Leitura]
  - Peso: [Ex: Regular]
  - Tamanho: [Ex: 1rem / 16px]
  - Altura de Linha: [Ex: 1.6]
  - Margem Inferior: [Ex: 1rem]
  - Status: A definir
  - Link para o Figma: [Link para Corpo de Texto no Figma]

- **Legenda (Caption):**
  - Descrição: Texto explicativo para imagens, tabelas ou outros elementos.
  - Família: [Nome da Fonte de Leitura]
  - Peso: [Ex: Regular ou Italic]
  - Tamanho: [Ex: 0.875rem / 14px]
  - Altura de Linha: [Ex: 1.4]
  - Cor: [Ex: Cor neutra mais clara que o corpo do texto]
  - Status: A definir
  - Link para o Figma: [Link para Legenda no Figma]

## Status Geral

**Status:** A definir (Crucial definir a escala e famílias antes de estilizar componentes)

## Link para o Figma (Visão Geral de Tipografia)

[Link para a seção de Tipografia no Figma] 