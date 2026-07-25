import { Link, useParams } from "react-router-dom";
import { ArrowRight, Clock, StickyNote } from "lucide-react";
import { LessonSidebar } from "@/components/sidebar/LessonSidebar";
import { CodeBlock } from "@/components/editor/CodeBlock";
import { Badge } from "@/components/ui/Badge";
import { Button } from "@/components/ui/Button";
import { Skeleton } from "@/components/ui/Skeleton";
import { ErrorState } from "@/components/common/ErrorState";
import { useLessonContent, useLessonSummaries } from "@/hooks/useLessons";
import { ROUTES } from "@/utils/constants";

export default function LessonPage() {
  const { moduleSlug = "python", lessonSlug = "variables" } = useParams();
  const { data: lesson, isLoading, isError, refetch } = useLessonContent(moduleSlug, lessonSlug);
  const { data: lessons } = useLessonSummaries(moduleSlug);

  return (
    <div className="grid lg:grid-cols-[260px_1fr]">
      <aside className="hidden border-r border-border/60 lg:block">
        {lessons && <LessonSidebar lessons={lessons} activeSlug={lessonSlug} moduleSlug={moduleSlug} />}
      </aside>

      <div className="mx-auto w-full max-w-3xl px-6 py-10">
        {isLoading && (
          <div className="flex flex-col gap-4">
            <Skeleton className="h-8 w-1/2" />
            <Skeleton className="h-4 w-full" />
            <Skeleton className="h-4 w-3/4" />
            <Skeleton className="h-48 w-full" />
          </div>
        )}

        {isError && <ErrorState onRetry={() => refetch()} />}

        {!isLoading && !isError && lesson && (
          <article className="flex flex-col gap-6">
            <div>
              <div className="mb-2 flex items-center gap-2">
                <Badge>{lesson.category}</Badge>
                <span className="flex items-center gap-1 text-xs text-muted-foreground">
                  <Clock className="h-3 w-3" /> {lesson.durationMinutes} min
                </span>
              </div>
              <h1 className="font-display text-3xl font-bold">{lesson.title}</h1>
            </div>

            <p className="leading-relaxed text-muted-foreground">{lesson.explanationMd}</p>

            <CodeBlock code={lesson.codeExample.code} language={lesson.codeExample.language} />

            <div className="rounded-xl border border-border bg-surface p-4">
              <p className="mb-1.5 text-xs font-semibold uppercase tracking-wider text-muted-foreground">Output</p>
              <pre className="whitespace-pre-wrap font-mono text-sm text-success">{lesson.output}</pre>
            </div>

            {lesson.notes.length > 0 && (
              <div className="rounded-xl border border-primary/30 bg-brand-gradient-soft p-4">
                <p className="mb-2 flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider text-primary">
                  <StickyNote className="h-3.5 w-3.5" /> Notes
                </p>
                <ul className="flex flex-col gap-1.5 text-sm text-muted-foreground">
                  {lesson.notes.map((note, i) => (
                    <li key={i}>• {note}</li>
                  ))}
                </ul>
              </div>
            )}

            <div className="flex justify-end border-t border-border/60 pt-6">
              {lesson.nextLessonSlug ? (
                <Button asChild>
                  <Link to={ROUTES.lesson(moduleSlug, lesson.nextLessonSlug)}>
                    Next lesson <ArrowRight className="h-4 w-4" />
                  </Link>
                </Button>
              ) : (
                <Button asChild>
                  <Link to={ROUTES.pythonRoadmap}>Back to roadmap</Link>
                </Button>
              )}
            </div>
          </article>
        )}
      </div>
    </div>
  );
}
