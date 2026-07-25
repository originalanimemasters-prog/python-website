import { Outlet } from "react-router-dom";
import { Menu } from "lucide-react";
import { Navbar } from "@/components/navbar/Navbar";
import { DashboardSidebar } from "@/components/sidebar/DashboardSidebar";
import { useUI } from "@/context/UIContext";

export function DashboardLayout() {
  const { toggleSidebar } = useUI();

  return (
    <div className="flex min-h-screen flex-col">
      <Navbar />
      <div className="flex flex-1">
        <DashboardSidebar />
        <div className="flex-1">
          <button
            onClick={toggleSidebar}
            className="focus-ring m-4 flex items-center gap-2 rounded-lg border border-border px-3 py-1.5 text-sm text-muted-foreground lg:hidden"
          >
            <Menu className="h-4 w-4" /> Menu
          </button>
          <main className="p-4 pt-0 sm:p-6 sm:pt-0 lg:p-8 lg:pt-8">
            <Outlet />
          </main>
        </div>
      </div>
    </div>
  );
}
