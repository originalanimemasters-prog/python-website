import { getMockQuiz } from "@/services/mock/quiz.mock";
import { withDelay } from "./delay";
import type { Quiz } from "@/types";

export async function fetchQuiz(id: string): Promise<Quiz | null> {
  // Future: return apiClient.get(`/quizzes/${id}`).then(r => r.data);
  return withDelay(getMockQuiz(id));
}
