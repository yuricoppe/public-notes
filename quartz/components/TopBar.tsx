import { concatenateResources } from "../util/resources"
import { classNames } from "../util/lang"
import { pathToRoot } from "../util/path"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import styles from "./styles/topbar.scss"

type TopBarConfig = {
  /** Abridor da gaveta, antes da marca. Só aparece abaixo do desktop. */
  nav: QuartzComponent[]
  /** Migalhas de pão, logo depois da marca. */
  trail: QuartzComponent[]
  /** Busca, tema e modo leitura, à direita. */
  actions: QuartzComponent[]
}

/**
 * Barra superior, de ponta a ponta.
 *
 * É `position: sticky`, não `fixed`: o `base.scss` do upstream põe
 * `overflow-x: hidden` e `width: 100vw` no `html`, e essa combinação deixa
 * `position: fixed` instável — a barra acaba deslocada do topo. Sticky vive no
 * fluxo normal, dispensa compensar altura no corpo e não sofre com isso.
 *
 * Subcomponentes vêm por opção, não por `children`: só o `header[]` recebe
 * filhos do renderizador. Mesmo padrão do `Flex`.
 */
export default ((config: TopBarConfig) => {
  const TopBar: QuartzComponent = (props: QuartzComponentProps) => {
    const baseDir = pathToRoot(props.fileData.slug!)
    return (
      <header class={classNames(props.displayClass, "topbar")} role="banner">
        <a href="#quartz-body" class="skip-link">
          Pular para o conteúdo
        </a>
        {config.nav.map((Item) => (
          <Item {...props} />
        ))}
        <a href={baseDir} class="topbar-brand">
          {props.cfg.pageTitle}
        </a>
        <div class="topbar-trail">
          {config.trail.map((Crumb) => (
            <Crumb {...props} />
          ))}
        </div>
        <div class="topbar-actions">
          {config.actions.map((Action) => (
            <Action {...props} />
          ))}
        </div>
      </header>
    )
  }

  const all = [...config.nav, ...config.trail, ...config.actions]
  TopBar.css = concatenateResources(styles, ...all.map((c) => c.css))
  TopBar.beforeDOMLoaded = concatenateResources(...all.map((c) => c.beforeDOMLoaded))
  TopBar.afterDOMLoaded = concatenateResources(...all.map((c) => c.afterDOMLoaded))
  return TopBar
}) satisfies QuartzComponentConstructor<TopBarConfig>
