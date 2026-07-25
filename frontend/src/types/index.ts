/**
 * Domain types are intentionally generic across "modules" (Python, Java, Git, SQL, Docker, ...).
 * A module is identified by its `slug`. Adding a new module means adding a new mock/service
 * file and a route entry — never touching these shared shapes.
 */

export type ModuleSlug = "python" | "java" | "git" | "sql" | "docker" | "django" | "aws";

export interface LearningModule {
  slug: ModuleSlug;
  name: string;
  description: string;
  icon: string; // lucide-react icon name
  color: string; // tailwind gradient classes
  totalLessons: number;
  isAvailable: boolean;
}

export type LessonDifficulty = "beginner" | "intermediate" | "advanced";

export interface LessonSummary {
  id: string;
  moduleSlug: ModuleSlug;
  slug: string;
  title: string;
  category: string;
  order: number;
  durationMinutes: number;
  difficulty: LessonDifficulty;
  isCompleted: boolean;
  isLocked: boolean;
}

export interface LessonContent extends LessonSummary {
  explanationMd: string;
  codeExample: {
    language: string;
    code: string;
  };
  output: string;
  notes: string[];
  nextLessonSlug: string | null;
}

export interface RoadmapNode {
  id: string;
  title: string;
  status: "completed" | "in-progress" | "locked";
  lessonCount: number;
  category: string;
}

export interface RoadmapTrack {
  moduleSlug: ModuleSlug;
  title: string;
  description: string;
  nodes: RoadmapNode[];
}

export interface TestCase {
  id: string;
  input: string;
  expectedOutput: string;
  isSample: boolean;
}

export interface PracticeQuestion {
  id: string;
  moduleSlug: ModuleSlug;
  title: string;
  difficulty: LessonDifficulty;
  promptMd: string;
  starterCode: string;
  language: string;
  testCases: TestCase[];
}

export interface QuizOption {
  id: string;
  label: string;
}

export interface QuizQuestion {
  id: string;
  prompt: string;
  options: QuizOption[];
  correctOptionId: string;
  explanation: string;
}

export interface Quiz {
  id: string;
  moduleSlug: ModuleSlug;
  title: string;
  questions: QuizQuestion[];
}

export interface Badge {
  id: string;
  name: string;
  description: string;
  icon: string;
  earnedAt: string | null;
}

export interface UserProfile {
  id: string;
  name: string;
  email: string;
  avatarUrl: string;
  joinedAt: string;
  currentStreak: number;
  longestStreak: number;
  totalLessonsCompleted: number;
  totalXp: number;
  badges: Badge[];
}

export interface ActivityItem {
  id: string;
  type: "lesson_completed" | "quiz_passed" | "badge_earned" | "practice_solved";
  title: string;
  timestamp: string;
}

export interface DashboardData {
  continueLearning: {
    lessonId: string;
    lessonTitle: string;
    moduleSlug: ModuleSlug;
    progressPercent: number;
  } | null;
  overallProgressPercent: number;
  currentStreak: number;
  recentActivity: ActivityItem[];
  recommendedLessons: LessonSummary[];
}

export type ExecutionStatus = "idle" | "running" | "success" | "error";

export interface RunResult {
  status: ExecutionStatus;
  stdout: string;
  stderr: string;
  runtimeMs: number;
  passedTestCases: number;
  totalTestCases: number;
}
