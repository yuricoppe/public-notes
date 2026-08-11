// @ts-ignore
import sidebarScript from "./scripts/sidebar.inline"
import { classNames } from "../util/lang"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import styles from "./styles/sidebartoggle.scss"

/**
 * Botão que recolhe a coluna esquerda. Mora dentro da própria coluna, no topo.
 */
const SidebarToggle: QuartzComponent = ({ displayClass }: QuartzComponentProps) => (
  <div class={classNames(displayClass, "sidebar-toggle-row")}>
    <button class="sidebar-toggle" type="button" aria-expanded="true" title="Esconder a navegação">
      <span class="sr-only">Esconder a navegação</span>
      <svg
        width="16"
        height="16"
        viewBox="0 0 16 16"
        fill="none"
        stroke="currentColor"
        stroke-width="1.4"
        aria-hidden="true"
      >
        <rect x="1.5" y="2.5" width="13" height="11" rx="1.5" />
        <line x1="6" y1="2.5" x2="6" y2="13.5" />
      </svg>
    </button>
  </div>
)

SidebarToggle.css = styles
SidebarToggle.beforeDOMLoaded = sidebarScript

export default (() => SidebarToggle) satisfies QuartzComponentConstructor
