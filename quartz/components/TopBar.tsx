import { concatenateResources } from "../util/resources"
import { classNames } from "../util/lang"
import { pathToRoot } from "../util/path"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import styles from "./styles/topbar.scss"

type TopBarConfig = {
  /** Controles à direita da marca: busca, tema, modo leitura. */
  actions: QuartzComponent[]
}

/**
 * Barra superior fixa, de ponta a ponta.
 *
 * Renderiza como primeiro item da coluna esquerda, mas sai do fluxo com
 * `position: fixed` — assim cobre a largura toda sem exigir mudança na árvore
 * que o `renderPage.tsx` monta. A grade compensa com `padding-top`.
 *
 * Os subcomponentes vêm por opção, e não por `children`: componentes fora de
 * `header[]` não recebem filhos do renderizador. É o mesmo padrão do `Flex`.
 */
export default ((config: TopBarConfig) => {
  const TopBar: QuartzComponent = (props: QuartzComponentProps) => {
    const baseDir = pathToRoot(props.fileData.slug!)
    return (
      <header class={classNames(props.displayClass, "topbar")} role="banner">
        <a href="#quartz-body" class="skip-link">
          Pular para o conteúdo
        </a>
        <a href={baseDir} class="topbar-brand">
          {props.cfg.pageTitle}
        </a>
        <div class="topbar-actions">
          {config.actions.map((Action) => (
            <Action {...props} />
          ))}
        </div>
      </header>
    )
  }

  TopBar.css = concatenateResources(styles, ...config.actions.map((c) => c.css))
  TopBar.beforeDOMLoaded = concatenateResources(...config.actions.map((c) => c.beforeDOMLoaded))
  TopBar.afterDOMLoaded = concatenateResources(...config.actions.map((c) => c.afterDOMLoaded))
  return TopBar
}) satisfies QuartzComponentConstructor<TopBarConfig>
