// Estado da coluna esquerda.
//
// São dois comportamentos diferentes, e por isso dois estados:
//
//  - `data-sidebar` (persistido): no desktop, a coluna recolhe e a grade fecha
//    o espaço dela. É preferência do leitor, então sobrevive à navegação.
//  - `data-drawer` (efêmero): abaixo de 1200px a coluna vira gaveta sobreposta.
//    Gaveta começa fechada e fecha ao navegar, como em qualquer site de docs.
//
// O primeiro é lido antes do DOM montar para não piscar, no mesmo padrão do
// darkmode.

const COLLAPSED = "collapsed"
const EXPANDED = "expanded"
const KEY = "sidebar-state"
const DESKTOP = "(min-width: 1200px)"

const saved = localStorage.getItem(KEY)
document.documentElement.setAttribute(
  "data-sidebar",
  saved === COLLAPSED ? COLLAPSED : EXPANDED,
)
document.documentElement.setAttribute("data-drawer", "closed")

const isDesktop = () => window.matchMedia(DESKTOP).matches

function syncButtons() {
  const expanded = isDesktop()
    ? document.documentElement.getAttribute("data-sidebar") !== COLLAPSED
    : document.documentElement.getAttribute("data-drawer") === "open"
  document.querySelectorAll<HTMLButtonElement>("button.sidebar-toggle").forEach((btn) => {
    btn.setAttribute("aria-expanded", String(expanded))
  })
}

function toggle() {
  if (isDesktop()) {
    const next =
      document.documentElement.getAttribute("data-sidebar") === COLLAPSED ? EXPANDED : COLLAPSED
    document.documentElement.setAttribute("data-sidebar", next)
    localStorage.setItem(KEY, next)
  } else {
    const next =
      document.documentElement.getAttribute("data-drawer") === "open" ? "closed" : "open"
    document.documentElement.setAttribute("data-drawer", next)
  }
  syncButtons()
}

function closeDrawer() {
  if (document.documentElement.getAttribute("data-drawer") === "open") {
    document.documentElement.setAttribute("data-drawer", "closed")
    syncButtons()
  }
}

function onKey(e: KeyboardEvent) {
  if (e.key === "Escape") closeDrawer()
}

document.addEventListener("nav", () => {
  // Trocar de página fecha a gaveta: ela é sobreposta e taparia o conteúdo.
  closeDrawer()
  syncButtons()

  document.querySelectorAll<HTMLButtonElement>("button.sidebar-toggle").forEach((btn) => {
    btn.removeEventListener("click", toggle)
    btn.addEventListener("click", toggle)
  })

  const scrim = document.querySelector<HTMLElement>(".drawer-scrim")
  if (scrim) {
    scrim.removeEventListener("click", closeDrawer)
    scrim.addEventListener("click", closeDrawer)
  }

  document.removeEventListener("keydown", onKey)
  document.addEventListener("keydown", onKey)
})

window.addEventListener("resize", syncButtons)
