// @ts-ignore
import sidebarScript from "./scripts/sidebar.inline"
import { concatenateResources } from "../util/resources"
import { classNames } from "../util/lang"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import styles from "./styles/contextbar.scss"

type ContextBarConfig = {
  /** Normalmente as migalhas de pão. Vazio na página inicial. */
  trail: QuartzComponent[]
}

/**
 * Faixa de contexto logo abaixo da barra superior: o botão que recolhe a coluna
 * esquerda e, ao lado, as migalhas de pão.
 *
 * Também é `position: fixed`, encostada sob a barra superior, pelo mesmo motivo
 * do TopBar — não há posição na árvore acima da grade.
 */
export default ((config: ContextBarConfig) => {
  const ContextBar: QuartzComponent = (props: QuartzComponentProps) => {
    return (
      <div class={classNames(props.displayClass, "contextbar")}>
        <button
          class="sidebar-toggle"
          type="button"
          aria-expanded="true"
          title="Mostrar ou esconder a navegação"
        >
          <span class="sr-only">Mostrar ou esconder a navegação</span>
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
        <div class="contextbar-crumbs">
          {config.trail.map((Crumb) => (
            <Crumb {...props} />
          ))}
        </div>
      </div>
    )
  }

  ContextBar.css = concatenateResources(styles, ...config.trail.map((c) => c.css))
  ContextBar.beforeDOMLoaded = concatenateResources(
    sidebarScript,
    ...config.trail.map((c) => c.beforeDOMLoaded),
  )
  ContextBar.afterDOMLoaded = concatenateResources(...config.trail.map((c) => c.afterDOMLoaded))
  return ContextBar
}) satisfies QuartzComponentConstructor<ContextBarConfig>
