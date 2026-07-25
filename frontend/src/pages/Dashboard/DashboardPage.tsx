import { Link } from "react-router-dom";
import { Map, ArrowRight } from "lucide-react";
import { PageContainer } from "@/components/common/PageContainer";
import { Skeleton } from "@/components/ui/Skeleton";
import { ErrorState } from "@/components/common/ErrorState";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/Card";
import { Button } from "@/components/ui/Button";
import { ContinueLearningCard } from "@/components/cards/ContinueLearningCard";
import { ProgressCard, StreakCard, ActivityRow } from "@/components/cards/DashboardCards";
import { LessonCard } from "@/components/cards/LessonCard";
import { useDashboardData } from "@/hooks/useUser";
import { getMockLessonSummaries } from "@/services/mock/lessons.mock";
import { ROUTES } from "@/utils/constants";

export default function DashboardPage() {
  const { data, isLoading, isError, refetch } = useDashboardData();

  if (isLoading) {
    return (
      <PageContainer className="px-0">
        <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-3">
          {Array.from({ length: 6 }).map((_, i) => (
            <Skeleton key={i} className="h-40 w-full" />
          ))}
        </div>
      </PageContainer>
    );
  }

  if (isError || !data) {
    return (
      <PageContainer className="px-0">
        <ErrorState onRetry={() => refetch()} />
      </PageContainer>
    );
  }

  const allLessons = getMockLessonSummaries("python");
  const recommended = allLessons.filter((l) => data.recommendedLessons.some((r) => r.id === l.id));

  return (
    <PageContainer className="flex flex-col gap-6 px-0">
      <div>
        <h1 className="font-display text-2xl font-bold sm:text-3xl">Welcome back, Parshant</h1>
        <p className="text-sm text-muted-foreground">Here's where you left off.</p>
      </div>

      <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-3">
        <ContinueLearningCard data={data.continueLearning} />
        <ProgressCard percent={data.overallProgressPercent} />
        <StreakCard days={data.currentStreak} />
      </div>

      <div className="grid gap-5 lg:grid-cols-[1.3fr_1fr]">
        <Card>
          <CardHeader className="flex-row items-center justify-between space-y-0">
            <CardTitle>Recommended lessons</CardTitle>
            <Button variant="ghost" size="sm" asChild>
              <Link to={ROUTES.pythonRoadmap}>
                View all <ArrowRight className="h-3.5 w-3.5" />
              </Link>
            </Button>
          </CardHeader>
          <CardContent className="flex flex-col gap-3">
            {recommended.map((lesson) => (
              <LessonCard key={lesson.id} lesson={lesson} />
            ))}
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Recent activity</CardTitle>
          </CardHeader>
          <CardContent className="divide-y divide-border/60">
            {data.recentActivity.map((activity) => (
              <ActivityRow key={activity.id} activity={activity} />
            ))}
          </CardContent>
        </Card>
      </div>

      <Card className="border-primary/30 bg-brand-gradient-soft">
        <CardContent className="flex flex-col items-center gap-3 p-8 text-center sm:flex-row sm:justify-between sm:text-left">
          <div className="flex items-center gap-3">
            <Map className="h-8 w-8 text-primary" />
            <div>
              <p className="font-display font-semibold">See your full roadmap</p>
              <p className="text-sm text-muted-foreground">Every lesson, in order, with your progress marked.</p>
            </div>
          </div>
          <Button asChild>
            <Link to={ROUTES.pythonRoadmap}>Open roadmap</Link>
          </Button>
        </CardContent>
      </Card>
    </PageContainer>
  );
}
