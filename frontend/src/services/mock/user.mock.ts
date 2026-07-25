import type { DashboardData, UserProfile } from "@/types";
import { getMockLessonSummaries } from "./lessons.mock";

export function getMockUserProfile(): UserProfile {
  return {
    id: "u1",
    name: "Parshant Rana",
    email: "parshant@devforge.dev",
    avatarUrl: "",
    joinedAt: "2026-02-14",
    currentStreak: 12,
    longestStreak: 21,
    totalLessonsCompleted: 4,
    totalXp: 1280,
    badges: [
      { id: "b1", name: "First Steps", description: "Completed your first lesson", icon: "Footprints", earnedAt: "2026-02-15" },
      { id: "b2", name: "Streak Keeper", description: "7-day learning streak", icon: "Flame", earnedAt: "2026-03-01" },
      { id: "b3", name: "Loop Master", description: "Solved 5 loop-based practice problems", icon: "Repeat", earnedAt: "2026-03-10" },
      { id: "b4", name: "Quiz Whiz", description: "Scored 100% on a quiz", icon: "Brain", earnedAt: null },
    ],
  };
}

export function getMockDashboardData(): DashboardData {
  const lessons = getMockLessonSummaries("python");
  const nextLesson = lessons.find((l) => !l.isCompleted && !l.isLocked);

  return {
    continueLearning: nextLesson
      ? {
          lessonId: nextLesson.id,
          lessonTitle: nextLesson.title,
          moduleSlug: "python",
          progressPercent: 62,
        }
      : null,
    overallProgressPercent: 29,
    currentStreak: 12,
    recentActivity: [
      { id: "a1", type: "lesson_completed", title: "Completed \u201CStrings\u201D", timestamp: "2 hours ago" },
      { id: "a2", type: "practice_solved", title: "Solved \u201CReverse a String\u201D", timestamp: "Yesterday" },
      { id: "a3", type: "badge_earned", title: "Earned \u201CStreak Keeper\u201D badge", timestamp: "3 days ago" },
      { id: "a4", type: "quiz_passed", title: "Passed Python Fundamentals Quiz", timestamp: "5 days ago" },
    ],
    recommendedLessons: lessons.filter((l) => !l.isCompleted).slice(0, 3),
  };
}
