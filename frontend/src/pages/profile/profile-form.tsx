import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Dialog, DialogClose, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import UserAvatar from "@/components/user-avatar";

export default function ProfileForm() {
  return (
    <Card>
      <CardHeader className="space-y-1 pb-3">
        <CardTitle className="text-2xl">
          Edit Account
        </CardTitle>
        <CardDescription>
          You can change your particulars here!
        </CardDescription>
      </CardHeader>
      <CardContent className="grid gap-4">
        <div className="grid gap-2">
          <Label>Email</Label>
          <Input id="email" type="email" placeholder="m@example.com" />
        </div>
        <div className="grid gap-2">
          <Label>Username</Label>
          <Input id="username"/>
        </div>
        <div className="grid gap-2">
          <Label>Picture</Label>
          <div className="flex justify-around">
            <UserAvatar />
            <Dialog>
              <DialogTrigger>Change Photo</DialogTrigger>
              <DialogContent>
                <DialogHeader>
                  <DialogTitle>Change Photo URL</DialogTitle>
                  <DialogDescription>
                    Key in the photo url that you want to change to. Make sure the photo is <b>public and accessible</b>.
                    <b> Click on Update Account</b> to save the change. 
                  </DialogDescription>
                  <div className="pt-4">
                    <Label>Photo URL</Label>
                    <Input id="photo-url" type="url" />
                  </div>
                </DialogHeader>
                <DialogFooter className="flex sm:justify-start">
                  <DialogClose asChild>
                    <Button type="button" variant='secondary'>Close</Button>
                  </DialogClose>
                </DialogFooter>
              </DialogContent>
            </Dialog>
          </div>
        </div>
      </CardContent>
      <CardFooter className="flex justify-between">
        <Button>
          Update Account
        </Button>
        <Button variant={"destructive"}>
            Delete Account
        </Button>
      </CardFooter>
    </Card>
  )
}