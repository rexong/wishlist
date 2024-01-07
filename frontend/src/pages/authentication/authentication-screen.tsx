import { AuthenticationUserDetailsTab } from "./authentication-user-details-tab";

export default function AuthenticateScreen() {

  return (
      <>
        <div className="flex justify-center items-center h-full">
          <div className="w-1/5">
            <AuthenticationUserDetailsTab />
          </div>
        </div>
      </>
  )
}