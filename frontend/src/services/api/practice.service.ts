import { getMockPracticeQuestion, simulateRun } from "@/services/mock/practice.mock";
import { withDelay } from "./delay";
import type { PracticeQuestion, RunResult } from "@/types";

export async function fetchPracticeQuestion(id: string): Promise<PracticeQuestion | null> {
  // Future: return apiClient.get(`/problems/${id}`).then(r => r.data);
  return withDelay(getMockPracticeQuestion(id));
}

export async function runCode(_questionId: string, code: string): Promise<RunResult> {
  // Future: return apiClient.post(`/problems/${_questionId}/run`, { code }).then(r => r.data);
  return withDelay(simulateRun(code), 700);
}

export async function submitCode(_questionId: string, code: string): Promise<RunResult> {
  // Future: return apiClient.post(`/problems/${_questionId}/submit`, { code }).then(r => r.data);
  return withDelay(simulateRun(code), 900);
}