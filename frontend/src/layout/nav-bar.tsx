import { ModeToggle } from "@/components/mode-toggle"
import { Button } from "@/components/ui/button"
import UserAvatar from "@/components/user-avatar"

export default function Navbar() {
  const isAuthenticated = true

  return (
    <>
      <nav className="border-b-2">
        <div className="flex item-center justify-between mx-36 my-4">
          <h2 className="basis-3/4 text-2xl">Wishlist</h2>
          <div className="basis-1/6 flex justify-evenly">
            {isAuthenticated ? (
              <>
                <UserAvatar />
              </>
            ) :
            (
              <>
                <Button>Login</Button>
                <Button>Sign Up</Button> 
              </>
            )}
            <div>
              <ModeToggle />
            </div>
          </div>
        </div>
      </nav>
    </>
  ) 
}