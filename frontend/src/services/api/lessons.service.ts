import { getMockLessonContent, getMockLessonSummaries } from "@/services/mock/lessons.mock";
import { withDelay } from "./delay";
import type { LessonContent, LessonSummary } from "@/types";

export async function fetchLessonSummaries(moduleSlug: string): Promise<LessonSummary[]> {
  // Future: return apiClient.get(`/modules/${moduleSlug}/lessons`).then(r => r.data);
  return withDelay(getMockLessonSummaries(moduleSlug));
}

export async function fetchLessonContent(moduleSlug: string, lessonSlug: string): Promise<LessonContent | null> {
  // Future: return apiClient.get(`/modules/${moduleSlug}/lessons/${lessonSlug}`).then(r => r.data);
  return withDelay(getMockLessonContent(moduleSlug, lessonSlug));
}
