import type { LucideIcon } from "lucide-react";
import { Card, CardContent } from "@/components/ui/Card";
import { cn } from "@/utils/cn";

interface StatCardProps {
  icon: LucideIcon;
  label: string;
  value: string | number;
  accent?: string;
}

export function StatCard({ icon: Icon, label, value, accent = "text-primary" }: StatCardProps) {
  return (
    <Card>
      <CardContent className="flex items-center gap-4 p-5">
        <div className={cn("flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-surface-hover", accent)}>
          <Icon className="h-5 w-5" />
        </div>
        <div>
          <p className="text-2xl font-display font-bold leading-tight">{value}</p>
          <p className="text-xs text-muted-foreground">{label}</p>
        </div>
      </CardContent>
    </Card>
  );
}
