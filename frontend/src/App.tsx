import { ThemeProvider } from "./components/theme-provider"
import Navbar from "./layout/nav-bar"

function App() {

  return (
    <>
      <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
        <Navbar/>
      </ThemeProvider>
    </>
  )
}

export default App
