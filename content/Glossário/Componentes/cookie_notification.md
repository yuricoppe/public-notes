# Cookie Notification (Notificação de Cookies)

O componente de Notificação de Cookies (também conhecido como banner de cookies ou consentimento de cookies) informa os usuários sobre o uso de cookies no site/aplicativo e, dependendo da legislação aplicável (como GDPR, LGPD), solicita o consentimento do usuário para o uso de cookies não essenciais.

## Casos de Uso

-   Praticamente todos os websites e aplicações que utilizam cookies para rastreamento, análise, personalização ou funcionalidade.
-   Obrigatório em muitas jurisdições para cumprir com as leis de privacidade.

## Funcionalidades Essenciais

-   **Mensagem Informativa:**
    *   Breve explicação de que o site usa cookies.
    *   (Opcional, mas recomendado) [[Glossário/Elementos/links|Link]] para a Política de Cookies/Privacidade para mais detalhes.
-   **Opções de Consentimento (dependendo da granularidade e da lei):
    *   **Aceitar Todos (Accept All):** [[Glossário/Elementos/botoes|Botão]] para consentir com todos os tipos de cookies.
    *   **Rejeitar Todos (Reject All - para não essenciais):** [[Glossário/Elementos/botoes|Botão]] para rejeitar cookies não essenciais.
    *   **Gerenciar Preferências/[[Glossário/Padrões/settings|Configurações]] (Manage Preferences/[[Glossário/Padrões/settings|Settings]]):** [[Glossário/Elementos/links|Link]] ou [[Glossário/Elementos/botoes|botão]] que leva a uma interface mais detalhada onde o usuário pode escolher granularmente quais categorias de cookies aceitar (ex: Essenciais, Analíticos, Marketing, Personalização).
    *   **[[Glossário/Elementos/botoes|Botão]] para Fechar (Dismiss):** Em alguns modelos de consentimento implícito (menos comum sob GDPR/LGPD estrito para cookies não essenciais), um simples "X" para fechar o banner pode ser usado, mas geralmente é acompanhado por uma aceitação ao continuar navegando.
-   **Persistência do Consentimento:** A escolha do usuário deve ser lembrada para visitas futuras (geralmente através de um cookie essencial).
-   **Acesso à Política de Cookies:** [[Glossário/Elementos/links|Link]] claro e acessível para a política de cookies completa.

## Melhores Práticas

-   **Visibilidade e Não Intrusividade:** O banner deve ser perceptível sem ser excessivamente obstrutivo ou impedir o acesso ao conteúdo principal antes da interação (especialmente para consentimento explícito).
    *   Posicionamentos comuns: [[Glossário/Componentes/footer|rodapé]] da página (banner fixo), canto inferior, ou um [[Glossário/Componentes/dialog|modal]] menos intrusivo.
-   **Linguagem Clara e Simples:** Evitar jargões legais complexos. A informação deve ser fácil de entender.
-   **Consentimento Granular (quando aplicável):** Permitir que os usuários escolham quais categorias de cookies aceitam, em vez de apenas uma opção "tudo ou nada" (além dos essenciais, que não requerem consentimento para serem ativados, mas devem ser informados).
-   **Facilidade de Alterar Preferências:** O usuário deve poder alterar suas preferências de cookies a qualquer momento (ex: através de um [[Glossário/Elementos/links|link]] no [[Glossário/Componentes/footer|rodapé]] ou nas [[Glossário/Padrões/settings|configurações]] de privacidade).
-   **Design Consistente:** O design do banner deve estar alinhado com a identidade visual do site.
-   **Acessibilidade (a11y):**
    *   O banner deve ser acessível por teclado e operável.
    *   Todos os [[Glossário/Elementos/botoes|botões]] e [[Glossário/Elementos/links|links]] devem ter rótulos claros.
    *   O conteúdo do banner deve ser legível e ter bom contraste.
    *   Se for um [[Glossário/Componentes/dialog|modal]], deve gerenciar o foco corretamente.
-   **Não usar "Dark Patterns":** Evitar designs enganosos que dificultam a rejeição ou a personalização de cookies (ex: [[Glossário/Elementos/botoes|botão]] "Aceitar" muito mais proeminente que "Rejeitar" ou "[[Glossário/Padrões/settings|Configurações]]").
-   **Cookies Essenciais:** Informar sobre cookies estritamente necessários que não requerem consentimento, mas são usados para o funcionamento do site.

## Variações

-   **Banner no [[Glossário/Componentes/footer|Rodapé]].**
-   **[[Glossário/Componentes/dialog|Modal]] Centralizado.**
-   **Notificação no Canto.**
-   **Interface de [[Glossário/Padrões/settings|Configurações]] Detalhadas:** Com [[Glossário/Elementos/interruptor|toggles]] para cada categoria de cookie e descrições.

## O Que Evitar

-   Bloquear completamente o acesso ao site antes do consentimento (a menos que seja a única interpretação legal aplicável e para todos os cookies).
-   Tornar difícil encontrar como rejeitar ou gerenciar cookies.
-   Assumir consentimento apenas pela rolagem da página ou continuação da navegação para cookies não essenciais (não conforme com GDPR/LGPD para consentimento explícito).
-   Falta de clareza sobre quais cookies são usados e para quê.
-   Não registrar a prova do consentimento (timestamp, preferências escolhidas). 