import { ThemeProvider } from "./components/theme-provider"
import { Route, Routes } from "react-router-dom"
import HomeScreen from "./pages/home-screen"
import WishlistScreen from "./pages/wishlist-screen"
import NotFoundScreen from "./pages/not-found-screen"
import AuthenticateScreen from "./pages/authentication-screen"
import isAuthenticated from "./state"
import ProfileScreen from "./pages/pofile-screen"
import MainLayout from "./layout/main-layout"

function App() {  

  return (
    <>
      <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
        <MainLayout />
        <Routes>
          {
            isAuthenticated ? (
              <>
                <Route path="/" element={<HomeScreen />} />
                <Route path="/wishlist" element={<WishlistScreen />} />
                <Route path="/profile" element={<ProfileScreen />} />
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
