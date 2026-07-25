import type { LucideIcon } from "lucide-react";
import { Card, CardContent } from "@/components/ui/Card";

export function FeatureCard({ icon: Icon, title, description }: { icon: LucideIcon; title: string; description: string }) {
  return (
    <Card className="group h-full transition-all hover:-translate-y-1 hover:border-primary/50 hover:shadow-glow-primary">
      <CardContent className="flex h-full flex-col gap-3 p-6">
        <div className="flex h-11 w-11 items-center justify-center rounded-xl bg-brand-gradient-soft text-primary transition-colors group-hover:bg-brand-gradient group-hover:text-white">
          <Icon className="h-5 w-5" />
        </div>
        <h3 className="font-display text-lg font-semibold">{title}</h3>
        <p className="text-sm text-muted-foreground">{description}</p>
      </CardContent>
    </Card>
  );
}
