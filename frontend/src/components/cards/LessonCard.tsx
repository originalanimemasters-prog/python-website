import { Link } from "react-router-dom";
import { Check, Clock, Lock, PlayCircle } from "lucide-react";
import { Card } from "@/components/ui/Card";
import { Badge } from "@/components/ui/Badge";
import type { LessonSummary } from "@/types";
import { ROUTES } from "@/utils/constants";
import { cn } from "@/utils/cn";

const DIFFICULTY_VARIANT = {
  beginner: "success",
  intermediate: "warning",
  advanced: "danger",
} as const;

export function LessonCard({ lesson }: { lesson: LessonSummary }) {
  const content = (
    <Card
      className={cn(
        "group flex items-center justify-between gap-4 p-4 transition-all hover:border-primary/50 hover:shadow-glow-primary",
        lesson.isLocked && "pointer-events-none opacity-50"
      )}
    >
      <div className="flex items-center gap-3">
        <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-surface-hover text-sm font-semibold text-muted-foreground">
          {lesson.isCompleted ? (
            <Check className="h-4 w-4 text-success" />
          ) : lesson.isLocked ? (
            <Lock className="h-4 w-4" />
          ) : (
            lesson.order
          )}
        </div>
        <div>
          <p className="font-medium">{lesson.title}</p>
          <p className="flex items-center gap-1 text-xs text-muted-foreground">
            <Clock className="h-3 w-3" /> {lesson.durationMinutes} min
          </p>
        </div>
      </div>
      <div className="flex items-center gap-3">
        <Badge variant={DIFFICULTY_VARIANT[lesson.difficulty]}>{lesson.difficulty}</Badge>
        <PlayCircle className="h-5 w-5 text-muted-foreground transition-colors group-hover:text-primary" />
      </div>
    </Card>
  );

  if (lesson.isLocked) return content;
  return <Link to={ROUTES.lesson(lesson.moduleSlug, lesson.slug)}>{content}</Link>;
}
