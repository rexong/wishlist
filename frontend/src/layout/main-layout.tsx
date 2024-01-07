import Navbar from "./nav-bar";
import { Outlet } from "react-router-dom";

export default function MainLayout() {
    return (
        <main className="h-screen w-screen">
            <Navbar />
            <Outlet />
        </main>
    )
}