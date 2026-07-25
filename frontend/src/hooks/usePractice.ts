import { useMutation, useQuery } from "@tanstack/react-query";
import { fetchPracticeQuestion, runCode, submitCode } from "@/services/api/practice.service";

export function usePracticeQuestion(id: string) {
  return useQuery({
    queryKey: ["practice", id],
    queryFn: () => fetchPracticeQuestion(id),
    enabled: Boolean(id),
  });
}

export function useRunCode(questionId: string) {
  return useMutation({
    mutationFn: (code: string) => runCode(questionId, code),
  });
}

export function useSubmitCode(questionId: string) {
  return useMutation({
    mutationFn: (code: string) => submitCode(questionId, code),
  });
}
