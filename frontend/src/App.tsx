import { ThemeProvider } from "./components/theme-provider"
import Navbar from "./layout/nav-bar"
import { Route, Routes } from "react-router-dom"
import HomeScreen from "./pages/home-screen"
import WishlistScreen from "./pages/wishlist-screen"
import NotFoundScreen from "./pages/not-found-screen"
import AuthenticateScreen from "./pages/authentication-screen"
import isAuthenticated from "./state"

function App() {  

  return (
    <>
      <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
        <Navbar />
        <Routes>
          {
            isAuthenticated ? (
              <>
                <Route path="/" element={<HomeScreen />} />
                <Route path="/wishlist" element={<WishlistScreen />} />
              </>
            ) : (
              <>
                <Route path="/" element={<AuthenticateScreen />} />
              </>
            )
          }
          <Route path="*" element={<NotFoundScreen />} />
        </Routes>
      </ThemeProvider>
    </>
  )
}

export default App
