import { ModeToggle } from "@/components/mode-toggle"
import UserAvatar from "@/components/user-avatar"
import { Link, Outlet } from "react-router-dom"
import isAuthenticated from "@/state"

export default function Navbar() {

  return (
    <>
      <nav className="border-b-2">
        <div className="flex item-center justify-between mx-36 my-4">
          <Link to="/">
            <h2 className="basis-3/4 text-2xl">Wishlist</h2>
          </Link>
          <div className="basis-1/6 flex justify-evenly">
            {isAuthenticated && <UserAvatar />}
            <div>
              <ModeToggle />
            </div>
          </div>
        </div>
      </nav>
      <Outlet />
    </>
  ) 
}