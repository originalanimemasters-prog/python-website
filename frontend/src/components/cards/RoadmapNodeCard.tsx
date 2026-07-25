import { Check, Lock, Sparkles } from "lucide-react";
import type { RoadmapNode } from "@/types";
import { cn } from "@/utils/cn";

const STATUS_STYLES: Record<RoadmapNode["status"], string> = {
  completed: "bg-success/15 border-success/40 text-success",
  "in-progress": "bg-brand-gradient-soft border-primary/50 text-foreground",
  locked: "bg-surface border-border text-muted-foreground",
};

export function RoadmapNodeCard({ node, index }: { node: RoadmapNode; index: number }) {
  return (
    <div className="relative flex gap-4 pb-8 last:pb-0">
      {/* connecting line */}
      <div className="flex flex-col items-center">
        <div
          className={cn(
            "flex h-10 w-10 shrink-0 items-center justify-center rounded-full border-2 font-display text-sm font-semibold",
            STATUS_STYLES[node.status]
          )}
        >
          {node.status === "completed" ? (
            <Check className="h-4 w-4" />
          ) : node.status === "locked" ? (
            <Lock className="h-4 w-4" />
          ) : (
            <Sparkles className="h-4 w-4" />
          )}
        </div>
        <div className="mt-1 w-px flex-1 bg-border last:hidden" aria-hidden />
      </div>

      <div className={cn("flex-1 rounded-2xl border p-4", STATUS_STYLES[node.status], "bg-opacity-5")}>
        <div className="flex items-center justify-between gap-2">
          <h4 className="font-display font-semibold text-foreground">
            {index + 1}. {node.title}
          </h4>
          <span className="whitespace-nowrap text-xs text-muted-foreground">{node.lessonCount} lessons</span>
        </div>
        <p className="mt-1 text-sm text-muted-foreground">{node.category}</p>
      </div>
    </div>
  );
}
