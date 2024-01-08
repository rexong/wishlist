import { Link } from "react-router-dom";
import { Button } from "./ui/button";
import { DropdownMenu, DropdownMenuContent, DropdownMenuGroup, DropdownMenuItem, DropdownMenuSeparator, DropdownMenuTrigger } from "./ui/dropdown-menu";
import UserAvatar from "./user-avatar";

export default function UserAvatarDropdown() {
    return (
      <DropdownMenu>
        <DropdownMenuTrigger asChild>
          <Button variant="ghost" className="relative h-8 w-8 rounded-full">
            <UserAvatar />
          </Button>
        </DropdownMenuTrigger>
        <DropdownMenuContent className="w-12" align="end" forceMount>
          <DropdownMenuGroup>
            <DropdownMenuItem>
              <Link to="/profile" className="w-full">
                <span>Profile</span>
              </Link>
            </DropdownMenuItem>
            <DropdownMenuSeparator />
            <DropdownMenuItem>
              Log Out
            </DropdownMenuItem>
          </DropdownMenuGroup>
        </DropdownMenuContent>
      </DropdownMenu>   
    )
    
}
