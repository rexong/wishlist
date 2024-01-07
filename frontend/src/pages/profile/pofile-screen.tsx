import ProfileForm from "./profile-form";

export default function ProfileScreen() {
  return (
    <>
      <div className="flex justify-center items-center h-full">
        <div className="w-1/5">
          <ProfileForm />
        </div>
      </div>
    </>
  )
}