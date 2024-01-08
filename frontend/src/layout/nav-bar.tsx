import { ModeToggle } from "@/components/mode-toggle"
import { Link } from "react-router-dom"
import isAuthenticated from "@/state"
import UserAvatarDropdown from "@/components/user-avatar-dropdown"

export default function Navbar() {

  return (
    <>
      <nav className="border-b-2 h-16">
        <div className="flex mx-32 h-full items-center justify-between">
          <Link to='/'>
            <h2 className="text-2xl">Wishlist</h2>
          </Link>
          <div className="basis-1/6 flex justify-evenly items-center h-full">
            {isAuthenticated && <UserAvatarDropdown/>}
            <ModeToggle />
          </div>
        </div>
      </nav>
    </>
  ) 
}