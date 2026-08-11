// Estado de recolhimento da coluna esquerda.
//
// Segue o mesmo padrão do darkmode: lê antes do DOM montar para não piscar, e
// guarda em localStorage. O estado vive num atributo do <html> para o CSS poder
// reagir sem depender de JS depois do primeiro paint.

const COLLAPSED = "collapsed"
const EXPANDED = "expanded"
const KEY = "sidebar-state"

const saved = localStorage.getItem(KEY)
if (saved === COLLAPSED || saved === EXPANDED) {
  document.documentElement.setAttribute("data-sidebar", saved)
} else {
  document.documentElement.setAttribute("data-sidebar", EXPANDED)
}

function syncButtons() {
  const collapsed = document.documentElement.getAttribute("data-sidebar") === COLLAPSED
  document.querySelectorAll<HTMLButtonElement>("button.sidebar-toggle").forEach((btn) => {
    btn.setAttribute("aria-expanded", collapsed ? "false" : "true")
  })
}

function toggleSidebar() {
  const collapsed = document.documentElement.getAttribute("data-sidebar") === COLLAPSED
  const next = collapsed ? EXPANDED : COLLAPSED
  document.documentElement.setAttribute("data-sidebar", next)
  localStorage.setItem(KEY, next)
  syncButtons()
}

document.addEventListener("nav", () => {
  syncButtons()
  document.querySelectorAll<HTMLButtonElement>("button.sidebar-toggle").forEach((btn) => {
    btn.removeEventListener("click", toggleSidebar)
    btn.addEventListener("click", toggleSidebar)
  })
})
