import { Link } from "react-router-dom";
import { Compass } from "lucide-react";
import { Button } from "@/components/ui/Button";
import { ROUTES } from "@/utils/constants";

export default function NotFoundPage() {
  return (
    <div className="flex min-h-[calc(100vh-4rem)] flex-col items-center justify-center gap-4 bg-glow-radial px-4 text-center">
      <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-brand-gradient-soft text-primary">
        <Compass className="h-8 w-8" />
      </div>
      <h1 className="font-display text-6xl font-bold gradient-text">404</h1>
      <p className="max-w-sm text-muted-foreground">
        This page took a wrong turn. Let's get you back on the roadmap.
      </p>
      <Button asChild className="mt-2">
        <Link to={ROUTES.home}>Back to home</Link>
      </Button>
    </div>
  );
}
