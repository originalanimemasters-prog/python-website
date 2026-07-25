import { useQuery } from "@tanstack/react-query";
import { fetchQuiz } from "@/services/api/quiz.service";

export function useQuizData(id: string) {
  return useQuery({
    queryKey: ["quiz", id],
    queryFn: () => fetchQuiz(id),
    enabled: Boolean(id),
  });
}
