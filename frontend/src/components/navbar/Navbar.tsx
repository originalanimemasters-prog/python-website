import { useState } from "react";
import { Link, NavLink } from "react-router-dom";
import { Menu, X, Flame, Sparkles } from "lucide-react";
import { Button } from "@/components/ui/Button";
import { Avatar, AvatarFallback } from "@/components/ui/Avatar";
import { APP_NAME, ROUTES } from "@/utils/constants";
import { useAuth } from "@/context/AuthContext";
import { cn } from "@/utils/cn";

const PUBLIC_LINKS = [
  { label: "Learn", href: ROUTES.pythonRoadmap },
  { label: "Dashboard", href: ROUTES.dashboard },
];

export function Navbar() {
  const [isOpen, setIsOpen] = useState(false);
  const { isAuthenticated } = useAuth();

  return (
    <header className="sticky top-0 z-50 w-full border-b border-border/60 bg-background/70 backdrop-blur-xl">
      <div className="container flex h-16 items-center justify-between">
        <Link to={ROUTES.home} className="flex items-center gap-2">
          <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-brand-gradient">
            <Sparkles className="h-4 w-4 text-white" />
          </span>
          <span className="font-display text-lg font-bold">{APP_NAME}</span>
        </Link>

        <nav className="hidden items-center gap-1 md:flex">
          {PUBLIC_LINKS.map((link) => (
            <NavLink
              key={link.href}
              to={link.href}
              className={({ isActive }) =>
                cn(
                  "rounded-lg px-3.5 py-2 text-sm font-medium text-muted-foreground transition-colors hover:text-foreground",
                  isActive && "text-foreground"
                )
              }
            >
              {link.label}
            </NavLink>
          ))}
        </nav>

        <div className="hidden items-center gap-3 md:flex">
          {isAuthenticated ? (
            <>
              <span className="flex items-center gap-1 text-sm text-muted-foreground">
                <Flame className="h-4 w-4 text-warning" /> 12
              </span>
              <Link to={ROUTES.profile}>
                <Avatar className="h-9 w-9">
                  <AvatarFallback>PR</AvatarFallback>
                </Avatar>
              </Link>
            </>
          ) : (
            <>
              <Button variant="ghost" size="sm" asChild>
                <Link to={ROUTES.login}>Log in</Link>
              </Button>
              <Button size="sm" asChild>
                <Link to={ROUTES.signup}>Get started</Link>
              </Button>
            </>
          )}
        </div>

        <button
          className="focus-ring rounded-lg p-2 text-foreground md:hidden"
          onClick={() => setIsOpen((prev) => !prev)}
          aria-label={isOpen ? "Close menu" : "Open menu"}
        >
          {isOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
        </button>
      </div>

      {isOpen && (
        <div className="border-t border-border/60 bg-background px-6 py-4 md:hidden">
          <nav className="flex flex-col gap-1">
            {PUBLIC_LINKS.map((link) => (
              <NavLink
                key={link.href}
                to={link.href}
                onClick={() => setIsOpen(false)}
                className="rounded-lg px-3 py-2 text-sm font-medium text-muted-foreground hover:bg-surface hover:text-foreground"
              >
                {link.label}
              </NavLink>
            ))}
            <div className="mt-3 flex flex-col gap-2">
              <Button variant="secondary" asChild>
                <Link to={ROUTES.login} onClick={() => setIsOpen(false)}>
                  Log in
                </Link>
              </Button>
              <Button asChild>
                <Link to={ROUTES.signup} onClick={() => setIsOpen(false)}>
                  Get started
                </Link>
              </Button>
            </div>
          </nav>
        </div>
      )}
    </header>
  );
}
