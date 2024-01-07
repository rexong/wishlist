import { Route, Routes } from "react-router-dom";
import HomeScreen from "./pages/home-screen";
import WishlistScreen from "./pages/wishlist/wishlist-screen";
import ProfileScreen from "./pages/pofile-screen";
import AuthenticateScreen from "./pages/authentication/authentication-screen";
import NotFoundScreen from "./pages/not-found-screen";
import isAuthenticated from "./state";

export default function Router() {
  return (
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
  )
}