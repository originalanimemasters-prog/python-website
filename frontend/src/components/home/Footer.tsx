import { Link } from "react-router-dom";
import { Sparkles } from "lucide-react";
import { APP_NAME, ROUTES } from "@/utils/constants";

const FOOTER_LINKS = {
  Product: [
    { label: "Python Roadmap", href: ROUTES.pythonRoadmap },
    { label: "Dashboard", href: ROUTES.dashboard },
  ],
  Account: [
    { label: "Log in", href: ROUTES.login },
    { label: "Sign up", href: ROUTES.signup },
  ],
};

export function Footer() {
  return (
    <footer className="border-t border-border/60 bg-surface/30">
      <div className="container flex flex-col gap-10 py-12 sm:flex-row sm:justify-between">
        <div className="max-w-xs">
          <Link to={ROUTES.home} className="flex items-center gap-2">
            <span className="flex h-7 w-7 items-center justify-center rounded-lg bg-brand-gradient">
              <Sparkles className="h-3.5 w-3.5 text-white" />
            </span>
            <span className="font-display text-base font-bold">{APP_NAME}</span>
          </Link>
          <p className="mt-3 text-sm text-muted-foreground">
            A structured, hands-on path to learning to code — one module at a time.
          </p>
        </div>

        <div className="flex gap-16">
          {Object.entries(FOOTER_LINKS).map(([section, links]) => (
            <div key={section}>
              <p className="mb-3 text-xs font-semibold uppercase tracking-wider text-muted-foreground">
                {section}
              </p>
              <ul className="flex flex-col gap-2">
                {links.map((link) => (
                  <li key={link.href}>
                    <Link to={link.href} className="text-sm text-muted-foreground hover:text-foreground">
                      {link.label}
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>
      <div className="border-t border-border/60 py-4 text-center text-xs text-muted-foreground">
        © {new Date().getFullYear()} {APP_NAME}. Built for developers, by developers.
      </div>
    </footer>
  );
}
