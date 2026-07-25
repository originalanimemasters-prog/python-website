import { NavLink } from "react-router-dom";
import { LayoutDashboard, Map, User, X } from "lucide-react";
import { ROUTES } from "@/utils/constants";
import { useUI } from "@/context/UIContext";
import { cn } from "@/utils/cn";

const NAV_ITEMS = [
  { label: "Dashboard", href: ROUTES.dashboard, icon: LayoutDashboard },
  { label: "Python Roadmap", href: ROUTES.pythonRoadmap, icon: Map },
  { label: "Profile", href: ROUTES.profile, icon: User },
];

export function DashboardSidebar() {
  const { isSidebarOpen, closeSidebar } = useUI();

  return (
    <>
      {isSidebarOpen && (
        <div className="fixed inset-0 z-40 bg-black/60 backdrop-blur-sm lg:hidden" onClick={closeSidebar} />
      )}
      <aside
        className={cn(
          "fixed inset-y-0 left-0 z-50 w-64 shrink-0 border-r border-border/60 bg-surface/80 backdrop-blur-xl transition-transform duration-300 lg:sticky lg:top-16 lg:z-0 lg:h-[calc(100vh-4rem)] lg:translate-x-0",
          isSidebarOpen ? "translate-x-0" : "-translate-x-full"
        )}
      >
        <div className="flex items-center justify-between p-4 lg:hidden">
          <span className="font-display text-sm font-semibold">Menu</span>
          <button onClick={closeSidebar} className="focus-ring rounded-lg p-1.5" aria-label="Close menu">
            <X className="h-4 w-4" />
          </button>
        </div>
        <nav className="flex flex-col gap-1 p-4">
          {NAV_ITEMS.map((item) => (
            <NavLink
              key={item.href}
              to={item.href}
              onClick={closeSidebar}
              className={({ isActive }) =>
                cn(
                  "flex items-center gap-3 rounded-xl px-3 py-2.5 text-sm font-medium text-muted-foreground transition-colors hover:bg-surface-hover hover:text-foreground",
                  isActive && "bg-brand-gradient-soft text-foreground"
                )
              }
            >
              <item.icon className="h-4 w-4" />
              {item.label}
            </NavLink>
          ))}
        </nav>
      </aside>
    </>
  );
}
