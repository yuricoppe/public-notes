import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  // Barras fixas do topo. Vivem no slot `chrome`, irmão da grade — ver
  // openspec/changes/adopt-docs-style-layout.
  chrome: [
    Component.TopBar({
      actions: [
        Component.Search(),
        Component.Darkmode(),
        Component.DesktopOnly(Component.ReaderMode()),
      ],
    }),
    Component.ContextBar({ trail: [Component.Breadcrumbs()] }),
    Component.DrawerScrim(),
  ],
  header: [],
  afterBody: [],
  footer: Component.Footer(),
}

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [Component.ArticleTitle(), Component.ContentMeta(), Component.TagList()],
  left: [Component.Explorer()],
  right: [
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Graph(),
    Component.Backlinks(),
  ],
}

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.ArticleTitle(), Component.ContentMeta()],
  left: [Component.Explorer()],
  right: [],
}
