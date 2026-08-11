import { QuartzComponent, QuartzComponentConstructor } from "./types"
import styles from "./styles/drawerscrim.scss"

/**
 * Véu por trás da gaveta de navegação, abaixo de 1200px.
 *
 * Precisa ser **irmão** da coluna esquerda, não filho: dentro dela ele ficaria
 * no mesmo contexto de empilhamento e cobriria o próprio painel da gaveta.
 * Por isso entra em `afterBody`, cujo contêiner não cria contexto.
 */
const DrawerScrim: QuartzComponent = () => <div class="drawer-scrim" aria-hidden="true" />

DrawerScrim.css = styles

export default (() => DrawerScrim) satisfies QuartzComponentConstructor
