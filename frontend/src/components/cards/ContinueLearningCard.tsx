import { Link } from "react-router-dom";
import { ArrowRight, BookOpen } from "lucide-react";
import { Card, CardContent } from "@/components/ui/Card";
import { Progress } from "@/components/ui/Progress";
import { Button } from "@/components/ui/Button";
import { EmptyState } from "@/components/common/EmptyState";
import type { DashboardData } from "@/types";
import { ROUTES } from "@/utils/constants";

export function ContinueLearningCard({ data }: { data: DashboardData["continueLearning"] }) {
  if (!data) {
    return (
      <Card>
        <CardContent className="p-5">
          <EmptyState
            icon={BookOpen}
            title="Nothing in progress"
            description="Start a module to see it here."
          />
        </CardContent>
      </Card>
    );
  }

  return (
    <Card className="overflow-hidden border-primary/30 bg-brand-gradient-soft">
      <CardContent className="flex flex-col gap-4 p-6">
        <span className="text-xs font-semibold uppercase tracking-wider text-primary">Continue learning</span>
        <h3 className="font-display text-xl font-bold">{data.lessonTitle}</h3>
        <div>
          <div className="mb-1.5 flex justify-between text-xs text-muted-foreground">
            <span>Lesson progress</span>
            <span>{data.progressPercent}%</span>
          </div>
          <Progress value={data.progressPercent} />
        </div>
        <Button asChild className="w-fit">
          <Link to={ROUTES.pythonRoadmap}>
            Resume lesson <ArrowRight className="h-4 w-4" />
          </Link>
        </Button>
      </CardContent>
    </Card>
  );
}
