import { useQuery } from "@tanstack/react-query";
import { fetchLessonContent, fetchLessonSummaries } from "@/services/api/lessons.service";

export function useLessonSummaries(moduleSlug: string) {
  return useQuery({
    queryKey: ["lessons", moduleSlug],
    queryFn: () => fetchLessonSummaries(moduleSlug),
  });
}

export function useLessonContent(moduleSlug: string, lessonSlug: string) {
  return useQuery({
    queryKey: ["lesson", moduleSlug, lessonSlug],
    queryFn: () => fetchLessonContent(moduleSlug, lessonSlug),
    enabled: Boolean(moduleSlug && lessonSlug),
  });
}
