import { BookCheck, Flame, Settings, Star, Trophy } from "lucide-react";
import { PageContainer } from "@/components/common/PageContainer";
import { Avatar, AvatarFallback } from "@/components/ui/Avatar";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/Card";
import { Input } from "@/components/ui/Input";
import { Label } from "@/components/ui/Label";
import { Button } from "@/components/ui/Button";
import { Skeleton } from "@/components/ui/Skeleton";
import { ErrorState } from "@/components/common/ErrorState";
import { StatCard } from "@/components/common/StatCard";
import { BadgeCard } from "@/components/cards/BadgeCard";
import { LessonCard } from "@/components/cards/LessonCard";
import { useUserProfile } from "@/hooks/useUser";
import { getMockLessonSummaries } from "@/services/mock/lessons.mock";

export default function ProfilePage() {
  const { data: user, isLoading, isError, refetch } = useUserProfile();

  if (isLoading) {
    return (
      <PageContainer className="flex flex-col gap-5 py-10">
        <Skeleton className="h-32 w-full" />
        <Skeleton className="h-64 w-full" />
      </PageContainer>
    );
  }

  if (isError || !user) {
    return (
      <PageContainer className="py-10">
        <ErrorState onRetry={() => refetch()} />
      </PageContainer>
    );
  }

  const completedLessons = getMockLessonSummaries("python").filter((l) => l.isCompleted);
  const initials = user.name
    .split(" ")
    .map((n) => n[0])
    .join("");

  return (
    <PageContainer className="flex flex-col gap-8 py-10">
      <Card>
        <CardContent className="flex flex-col items-center gap-4 p-8 text-center sm:flex-row sm:text-left">
          <Avatar className="h-20 w-20">
            <AvatarFallback className="text-xl">{initials}</AvatarFallback>
          </Avatar>
          <div>
            <h1 className="font-display text-2xl font-bold">{user.name}</h1>
            <p className="text-sm text-muted-foreground">{user.email}</p>
            <p className="mt-1 text-xs text-muted-foreground">
              Joined {new Date(user.joinedAt).toLocaleDateString(undefined, { month: "long", year: "numeric" })}
            </p>
          </div>
        </CardContent>
      </Card>

      <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
        <StatCard icon={Flame} label="Current streak" value={`${user.currentStreak} days`} accent="text-warning" />
        <StatCard icon={Trophy} label="Longest streak" value={`${user.longestStreak} days`} accent="text-primary" />
        <StatCard icon={BookCheck} label="Lessons completed" value={user.totalLessonsCompleted} accent="text-success" />
        <StatCard icon={Star} label="Total XP" value={user.totalXp.toLocaleString()} accent="text-accent" />
      </div>

      <div>
        <h2 className="mb-4 font-display text-lg font-semibold">Badges</h2>
        <div className="grid grid-cols-2 gap-4 sm:grid-cols-4">
          {user.badges.map((badge) => (
            <BadgeCard key={badge.id} badge={badge} />
          ))}
        </div>
      </div>

      <div>
        <h2 className="mb-4 font-display text-lg font-semibold">Completed lessons</h2>
        <div className="flex flex-col gap-3">
          {completedLessons.map((lesson) => (
            <LessonCard key={lesson.id} lesson={lesson} />
          ))}
        </div>
      </div>

      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <Settings className="h-4 w-4" /> Settings
          </CardTitle>
        </CardHeader>
        <CardContent className="flex flex-col gap-4">
          <div className="grid gap-4 sm:grid-cols-2">
            <div className="flex flex-col gap-1.5">
              <Label htmlFor="displayName">Display name</Label>
              <Input id="displayName" defaultValue={user.name} />
            </div>
            <div className="flex flex-col gap-1.5">
              <Label htmlFor="profileEmail">Email</Label>
              <Input id="profileEmail" defaultValue={user.email} type="email" />
            </div>
          </div>
          <Button className="w-fit">Save changes</Button>
        </CardContent>
      </Card>
    </PageContainer>
  );
}
