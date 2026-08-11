// @ts-ignore
import sidebarScript from "./scripts/sidebar.inline"
import { classNames } from "../util/lang"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import styles from "./styles/sidebartoggle.scss"

/**
 * Abre a gaveta de navegação.
 *
 * Só existe abaixo de 1200px, onde a coluna esquerda é sobreposta. No desktop a
 * coluna está sempre visível e quem quer o texto sozinho usa o modo leitura —
 * um botão de recolher seria um segundo caminho para o mesmo lugar.
 */
const SidebarToggle: QuartzComponent = ({ displayClass }: QuartzComponentProps) => (
  <button
    class={classNames(displayClass, "sidebar-toggle")}
    type="button"
    aria-expanded="false"
    title="Abrir a navegação"
  >
    <span class="sr-only">Abrir a navegação</span>
    <svg
      width="18"
      height="18"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      aria-hidden="true"
    >
      <line x1="4" x2="20" y1="6" y2="6" />
      <line x1="4" x2="20" y1="12" y2="12" />
      <line x1="4" x2="20" y1="18" y2="18" />
    </svg>
  </button>
)

SidebarToggle.css = styles
SidebarToggle.beforeDOMLoaded = sidebarScript

export default (() => SidebarToggle) satisfies QuartzComponentConstructor
