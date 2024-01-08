import { ThemeProvider } from "./components/theme-provider"
import MainLayout from "./layout/main-layout"

function App() {  

  return (
    <>
      <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
        <MainLayout />
      </ThemeProvider>
    </>
  )
}

export default App
