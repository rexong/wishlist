import {
  Tabs,
  TabsContent,
  TabsList,
  TabsTrigger,
} from "@/components/ui/tabs"
import AuthenticationUserDetailsForm from "./authentication-user-details-form"

export function AuthenticationUserDetailsTab() {
  return (
    <Tabs defaultValue="login" className="w-full">
      <TabsList className="grid w-full grid-cols-2">
        <TabsTrigger value="login">Login</TabsTrigger>
        <TabsTrigger value="sign-up">Sign Up</TabsTrigger>
      </TabsList>
      <TabsContent value="login">
        <AuthenticationUserDetailsForm isLogin/>
      </TabsContent>
      <TabsContent value="sign-up">
        <AuthenticationUserDetailsForm />
      </TabsContent>
    </Tabs>
  )
}

