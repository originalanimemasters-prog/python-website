import type { LearningModule } from "@/types";

export const APP_NAME = "DevForge";

export const ROUTES = {
  home: "/",
  login: "/login",
  signup: "/signup",
  verifyEmail: "/verify-email",
  forgotPassword: "/forgot-password",
  resetPassword: "/reset-password",
  dashboard: "/dashboard",
  pythonRoadmap: "/learn/python",
  lesson: (moduleSlug: string, lessonSlug: string) => `/learn/${moduleSlug}/lesson/${lessonSlug}`,
  practice: (moduleSlug: string, questionId: string) => `/learn/${moduleSlug}/practice/${questionId}`,
  quiz: (moduleSlug: string, quizId: string) => `/learn/${moduleSlug}/quiz/${quizId}`,
  profile: "/profile",
} as const;

/**
 * Central registry of learning modules. Adding "java", "git", "sql", "docker", "django", "aws"
 * later is a one-line addition here plus a matching mock/service file — no architectural change.
 */
export const LEARNING_MODULES: LearningModule[] = [
  {
    slug: "python",
    name: "Python",
    description: "Variables to OOP — build a real foundation, one concept at a time.",
    icon: "FileCode2",
    color: "from-violet-500 to-blue-500",
    totalLessons: 14,
    isAvailable: true,
  },
  {
    slug: "java",
    name: "Java",
    description: "Strongly-typed, enterprise-grade fundamentals.",
    icon: "Coffee",
    color: "from-orange-500 to-red-500",
    totalLessons: 0,
    isAvailable: false,
  },
  {
    slug: "git",
    name: "Git",
    description: "Version control that every team relies on.",
    icon: "GitBranch",
    color: "from-red-500 to-pink-500",
    totalLessons: 0,
    isAvailable: false,
  },
  {
    slug: "sql",
    name: "SQL",
    description: "Query, join, and model relational data.",
    icon: "Database",
    color: "from-blue-500 to-cyan-500",
    totalLessons: 0,
    isAvailable: false,
  },
  {
    slug: "docker",
    name: "Docker",
    description: "Package and ship software the modern way.",
    icon: "Container",
    color: "from-sky-500 to-blue-600",
    totalLessons: 0,
    isAvailable: false,
  },
  {
    slug: "django",
    name: "Django",
    description: "Build production backends with Python's leading framework.",
    icon: "Server",
    color: "from-emerald-500 to-green-600",
    totalLessons: 0,
    isAvailable: false,
  },
  {
    slug: "aws",
    name: "AWS",
    description: "Deploy and scale on the world's leading cloud.",
    icon: "Cloud",
    color: "from-amber-500 to-orange-600",
    totalLessons: 0,
    isAvailable: false,
  },
];

export const MOCK_API_DELAY_MS = 450;
