import { Link } from "react-router-dom";
import { Check, Lock } from "lucide-react";
import type { LessonSummary } from "@/types";
import { ROUTES } from "@/utils/constants";
import { cn } from "@/utils/cn";

interface LessonSidebarProps {
  lessons: LessonSummary[];
  activeSlug: string;
  moduleSlug: string;
}

export function LessonSidebar({ lessons, activeSlug, moduleSlug }: LessonSidebarProps) {
  const grouped = lessons.reduce<Record<string, LessonSummary[]>>((acc, lesson) => {
    acc[lesson.category] = acc[lesson.category] ?? [];
    acc[lesson.category].push(lesson);
    return acc;
  }, {});

  return (
    <nav className="flex flex-col gap-5 p-4">
      {Object.entries(grouped).map(([category, items]) => (
        <div key={category}>
          <p className="mb-2 px-2 text-xs font-semibold uppercase tracking-wider text-muted-foreground">
            {category}
          </p>
          <div className="flex flex-col gap-0.5">
            {items.map((lesson) => {
              const isActive = lesson.slug === activeSlug;
              return (
                <Link
                  key={lesson.id}
                  to={lesson.isLocked ? "#" : ROUTES.lesson(moduleSlug, lesson.slug)}
                  aria-disabled={lesson.isLocked}
                  className={cn(
                    "flex items-center justify-between rounded-lg px-3 py-2 text-sm transition-colors",
                    isActive ? "bg-brand-gradient-soft font-medium text-foreground" : "text-muted-foreground hover:bg-surface-hover hover:text-foreground",
                    lesson.isLocked && "pointer-events-none opacity-40"
                  )}
                >
                  <span>{lesson.title}</span>
                  {lesson.isCompleted ? (
                    <Check className="h-3.5 w-3.5 text-success" />
                  ) : lesson.isLocked ? (
                    <Lock className="h-3.5 w-3.5" />
                  ) : null}
                </Link>
              );
            })}
          </div>
        </div>
      ))}
    </nav>
  );
}
