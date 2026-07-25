import { PageContainer, SectionHeading } from "@/components/common/PageContainer";
import { LessonCard } from "@/components/cards/LessonCard";
import { RoadmapNodeCard } from "@/components/cards/RoadmapNodeCard";
import { Skeleton } from "@/components/ui/Skeleton";
import { ErrorState } from "@/components/common/ErrorState";
import { Card, CardContent } from "@/components/ui/Card";
import { useRoadmap } from "@/hooks/useRoadmap";
import { useLessonSummaries } from "@/hooks/useLessons";

export default function PythonRoadmapPage() {
  const roadmap = useRoadmap("python");
  const lessons = useLessonSummaries("python");

  const isLoading = roadmap.isLoading || lessons.isLoading;
  const isError = roadmap.isError || lessons.isError;

  return (
    <PageContainer className="flex flex-col gap-10 py-12">
      <SectionHeading
        eyebrow="Module"
        title="Python Roadmap"
        description="14 lessons, four stages, one clear path from variables to exception handling."
      />

      {isLoading && (
        <div className="grid gap-8 lg:grid-cols-[1fr_1.4fr]">
          <Skeleton className="h-96 w-full" />
          <Skeleton className="h-96 w-full" />
        </div>
      )}

      {isError && <ErrorState onRetry={() => { roadmap.refetch(); lessons.refetch(); }} />}

      {!isLoading && !isError && roadmap.data && lessons.data && (
        <div className="grid gap-8 lg:grid-cols-[1fr_1.4fr]">
          <Card className="h-fit">
            <CardContent className="p-6">
              {roadmap.data.nodes.map((node, i) => (
                <RoadmapNodeCard key={node.id} node={node} index={i} />
              ))}
            </CardContent>
          </Card>

          <div className="flex flex-col gap-3">
            {lessons.data.map((lesson) => (
              <LessonCard key={lesson.id} lesson={lesson} />
            ))}
          </div>
        </div>
      )}
    </PageContainer>
  );
}
