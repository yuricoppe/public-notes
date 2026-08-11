import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

// Barra do topo: marca · migalhas · busca, tema e leitura à direita.
// Vive no slot `chrome`, irmão da grade — ver openspec/changes/adopt-docs-style-layout.
const topBar = Component.TopBar({
  nav: [Component.SidebarToggle()],
  trail: [Component.Breadcrumbs()],
  actions: [
    Component.Search(),
    Component.Darkmode(),
    Component.DesktopOnly(Component.ReaderMode()),
  ],
})

export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  chrome: [topBar, Component.DrawerScrim()],
  header: [],
  afterBody: [],
  footer: Component.Footer(),
}

// A home é a única página sem colunas laterais. Em vez de escondê-las por CSS,
// não são renderizadas — assim os scripts do explorador e do grafo nem rodam.
const notHome = (props: { fileData: { slug?: string } }) => props.fileData.slug !== "index"
const onlyOutsideHome = (
  component: Parameters<typeof Component.ConditionalRender>[0]["component"],
) => Component.ConditionalRender({ component, condition: notHome })

// páginas de conteúdo (uma nota)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [Component.ArticleTitle(), Component.ContentMeta(), Component.TagList()],
  left: [onlyOutsideHome(Component.Explorer())],
  right: [
    onlyOutsideHome(Component.DesktopOnly(Component.TableOfContents())),
    onlyOutsideHome(Component.Graph()),
    onlyOutsideHome(Component.Backlinks()),
  ],
}

// páginas de listagem (pastas e tags)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.ArticleTitle(), Component.ContentMeta()],
  left: [Component.Explorer()],
  right: [],
}
