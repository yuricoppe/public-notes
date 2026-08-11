// Estado da gaveta de navegação.
//
// Abaixo de 1200px a coluna esquerda vira gaveta sobreposta, aberta pelo botão
// da barra do topo. É estado efêmero: começa fechada, fecha ao navegar, no
// Escape e no clique no véu — como em qualquer site de documentação.
//
// No desktop não existe estado nenhum: a coluna está sempre lá. Quem quer só o
// texto usa o modo leitura.

const OPEN = "open"
const CLOSED = "closed"

document.documentElement.setAttribute("data-drawer", CLOSED)

const isOpen = () => document.documentElement.getAttribute("data-drawer") === OPEN

function sync() {
  document.querySelectorAll<HTMLButtonElement>("button.sidebar-toggle").forEach((btn) => {
    btn.setAttribute("aria-expanded", String(isOpen()))
  })
}

function toggle() {
  document.documentElement.setAttribute("data-drawer", isOpen() ? CLOSED : OPEN)
  sync()
}

function close() {
  if (isOpen()) {
    document.documentElement.setAttribute("data-drawer", CLOSED)
    sync()
  }
}

function onKey(e: KeyboardEvent) {
  if (e.key === "Escape") close()
}

document.addEventListener("nav", () => {
  // Trocar de página fecha a gaveta: ela é sobreposta e taparia o conteúdo.
  close()

  document.querySelectorAll<HTMLButtonElement>("button.sidebar-toggle").forEach((btn) => {
    btn.removeEventListener("click", toggle)
    btn.addEventListener("click", toggle)
  })

  const scrim = document.querySelector<HTMLElement>(".drawer-scrim")
  if (scrim) {
    scrim.removeEventListener("click", close)
    scrim.addEventListener("click", close)
  }

  document.removeEventListener("keydown", onKey)
  document.addEventListener("keydown", onKey)
})

window.addEventListener("resize", close)
