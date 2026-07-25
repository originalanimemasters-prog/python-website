import { Flame, TrendingUp } from "lucide-react";
import { Card, CardContent } from "@/components/ui/Card";
import { Progress } from "@/components/ui/Progress";
import type { ActivityItem as ActivityItemType } from "@/types";

export function ProgressCard({ percent }: { percent: number }) {
  return (
    <Card>
      <CardContent className="flex flex-col gap-3 p-5">
        <div className="flex items-center gap-2 text-sm text-muted-foreground">
          <TrendingUp className="h-4 w-4 text-primary" /> Overall progress
        </div>
        <p className="font-display text-3xl font-bold">{percent}%</p>
        <Progress value={percent} />
      </CardContent>
    </Card>
  );
}

export function StreakCard({ days }: { days: number }) {
  return (
    <Card>
      <CardContent className="flex items-center gap-4 p-5">
        <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-warning/15 text-warning">
          <Flame className="h-6 w-6" />
        </div>
        <div>
          <p className="font-display text-2xl font-bold">{days}-day streak</p>
          <p className="text-xs text-muted-foreground">Keep it going — come back tomorrow</p>
        </div>
      </CardContent>
    </Card>
  );
}

const ACTIVITY_ICON: Record<ActivityItemType["type"], string> = {
  lesson_completed: "bg-primary/15 text-primary",
  quiz_passed: "bg-accent/15 text-accent",
  badge_earned: "bg-warning/15 text-warning",
  practice_solved: "bg-success/15 text-success",
};

export function ActivityRow({ activity }: { activity: ActivityItemType }) {
  return (
    <div className="flex items-center gap-3 py-2.5">
      <span className={`h-2 w-2 shrink-0 rounded-full ${ACTIVITY_ICON[activity.type].split(" ")[0]}`} />
      <div className="flex-1">
        <p className="text-sm">{activity.title}</p>
      </div>
      <span className="whitespace-nowrap text-xs text-muted-foreground">{activity.timestamp}</span>
    </div>
  );
}
