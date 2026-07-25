import type { PracticeQuestion, RunResult } from "@/types";

const PRACTICE_QUESTIONS: PracticeQuestion[] = [
  {
    id: "reverse-string",
    moduleSlug: "python",
    title: "Reverse a String",
    difficulty: "beginner",
    promptMd:
      "Write a function `reverse_string(s)` that returns the input string reversed, without using the built-in `reversed()` or slicing shortcuts.",
    starterCode: `def reverse_string(s):\n    # your code here\n    pass\n`,
    language: "python",
    testCases: [
      { id: "t1", input: '"hello"', expectedOutput: '"olleh"', isSample: true },
      { id: "t2", input: '"python"', expectedOutput: '"nohtyp"', isSample: true },
      { id: "t3", input: '""', expectedOutput: '""', isSample: false },
    ],
  },
  {
    id: "fizzbuzz",
    moduleSlug: "python",
    title: "FizzBuzz",
    difficulty: "beginner",
    promptMd:
      "Write a function `fizzbuzz(n)` that returns a list of strings for numbers 1..n: 'Fizz' for multiples of 3, 'Buzz' for multiples of 5, 'FizzBuzz' for both, and the number as a string otherwise.",
    starterCode: `def fizzbuzz(n):\n    # your code here\n    pass\n`,
    language: "python",
    testCases: [
      { id: "t1", input: "5", expectedOutput: '["1","2","Fizz","4","Buzz"]', isSample: true },
      { id: "t2", input: "15", expectedOutput: "...FizzBuzz at index 15", isSample: false },
    ],
  },
];

export function getMockPracticeQuestion(id: string): PracticeQuestion | null {
  return PRACTICE_QUESTIONS.find((q) => q.id === id) ?? PRACTICE_QUESTIONS[0];
}

export function getMockPracticeList(): PracticeQuestion[] {
  return PRACTICE_QUESTIONS;
}

/**
 * Simulates a judge run. In production this call is replaced by a POST to
 * `/api/v1/problems/{slug}/run` — no component code changes, only the service layer.
 */
export function simulateRun(code: string): RunResult {
  const hasReturn = /return/.test(code);
  return {
    status: hasReturn ? "success" : "error",
    stdout: hasReturn ? "Sample tests passed." : "",
    stderr: hasReturn ? "" : "No return statement found — did you finish the function?",
    runtimeMs: hasReturn ? Math.floor(40 + Math.random() * 60) : 0,
    passedTestCases: hasReturn ? 2 : 0,
    totalTestCases: 2,
  };
}
