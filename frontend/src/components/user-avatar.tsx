import { Avatar, AvatarFallback, AvatarImage } from "./ui/avatar";

export default function UserAvatar() {
    return (
      <Avatar className="h-10 w-10">
        <AvatarImage src="https://github.com/shadcn.png" />
        <AvatarFallback>SC</AvatarFallback>
      </Avatar>
    )
}