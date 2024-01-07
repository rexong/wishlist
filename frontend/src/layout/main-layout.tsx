import Router from "@/router";
import Navbar from "./nav-bar";

export default function MainLayout() {
  return (
      <main className="flex flex-col h-screen w-screen">
        <Navbar />
          <div className="flex-grow">
            <Router />
          </div>
      </main>
  )
}