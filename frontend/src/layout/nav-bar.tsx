import { ModeToggle } from "@/components/mode-toggle"
import UserAvatar from "@/components/user-avatar"
import { Link } from "react-router-dom"
import isAuthenticated from "@/state"

export default function Navbar() {

  return (
    <>
      <nav className="border-b-2 h-16">
        <div className="flex mx-32 h-full items-center justify-between">
          <Link to='/'>
            <h2 className="text-2xl">Wishlist</h2>
          </Link>
          <div className="basis-1/6 flex justify-evenly items-center h-full">
            {isAuthenticated && <UserAvatar/>}
            <ModeToggle />
          </div>
        </div>
      </nav>
    </>
  ) 
}