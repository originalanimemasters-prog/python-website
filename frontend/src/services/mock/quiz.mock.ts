import type { Quiz } from "@/types";

const QUIZZES: Record<string, Quiz> = {
  "python-fundamentals": {
    id: "python-fundamentals",
    moduleSlug: "python",
    title: "Python Fundamentals Quiz",
    questions: [
      {
        id: "q1",
        prompt: "What does `type(3.0)` return?",
        options: [
          { id: "a", label: "int" },
          { id: "b", label: "float" },
          { id: "c", label: "double" },
          { id: "d", label: "decimal" },
        ],
        correctOptionId: "b",
        explanation: "Any number written with a decimal point is a `float` in Python.",
      },
      {
        id: "q2",
        prompt: "Which collection type does not allow duplicate values?",
        options: [
          { id: "a", label: "list" },
          { id: "b", label: "tuple" },
          { id: "c", label: "set" },
          { id: "d", label: "dict values" },
        ],
        correctOptionId: "c",
        explanation: "Sets automatically enforce uniqueness among their elements.",
      },
      {
        id: "q3",
        prompt: "What is the output of `3 // 2`?",
        options: [
          { id: "a", label: "1.5" },
          { id: "b", label: "1" },
          { id: "c", label: "2" },
          { id: "d", label: "Error" },
        ],
        correctOptionId: "b",
        explanation: "`//` is floor division, so `3 // 2` evaluates to `1`.",
      },
    ],
  },
};

export function getMockQuiz(id: string): Quiz | null {
  return QUIZZES[id] ?? QUIZZES["python-fundamentals"];
}
