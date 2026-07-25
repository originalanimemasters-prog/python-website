import * as Icons from "lucide-react";
import type { LucideIcon } from "lucide-react";
import { Card, CardContent } from "@/components/ui/Card";
import { cn } from "@/utils/cn";
import type { Badge as BadgeType } from "@/types";

export function BadgeCard({ badge }: { badge: BadgeType }) {
  const Icon = (Icons[badge.icon as keyof typeof Icons] as LucideIcon) ?? Icons.Award;
  const isEarned = Boolean(badge.earnedAt);

  return (
    <Card className={cn("text-center transition-opacity", !isEarned && "opacity-40 grayscale")}>
      <CardContent className="flex flex-col items-center gap-2 p-5">
        <div className="flex h-12 w-12 items-center justify-center rounded-full bg-brand-gradient text-white">
          <Icon className="h-5 w-5" />
        </div>
        <p className="font-display text-sm font-semibold">{badge.name}</p>
        <p className="text-xs text-muted-foreground">{badge.description}</p>
      </CardContent>
    </Card>
  );
}
