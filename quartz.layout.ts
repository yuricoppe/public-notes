import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

// Barra superior fixa + faixa de contexto.
// Ficam no início de `left[]` porque é a primeira posição da árvore; as duas
// saem do fluxo com `position: fixed` e cobrem a largura toda.
// Ver openspec/changes/adopt-docs-style-layout.
const chrome = (withCrumbs: boolean) => [
  Component.TopBar({
    actions: [
      Component.Search(),
      Component.Darkmode(),
      Component.DesktopOnly(Component.ReaderMode()),
    ],
  }),
  Component.ContextBar({ trail: withCrumbs ? [Component.Breadcrumbs()] : [] }),
]

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [Component.DrawerScrim()],
  footer: Component.Footer(),
}

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [Component.ArticleTitle(), Component.ContentMeta(), Component.TagList()],
  left: [...chrome(true), Component.Explorer()],
  right: [
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Graph(),
    Component.Backlinks(),
  ],
}

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.ArticleTitle(), Component.ContentMeta()],
  left: [...chrome(true), Component.Explorer()],
  right: [],
}
