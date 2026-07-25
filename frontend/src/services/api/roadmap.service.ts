import { getMockRoadmap } from "@/services/mock/roadmap.mock";
import { withDelay } from "./delay";
import type { RoadmapTrack } from "@/types";

export async function fetchRoadmap(moduleSlug: string): Promise<RoadmapTrack | null> {
  // Future: return apiClient.get(`/modules/${moduleSlug}/roadmap`).then(r => r.data);
  return withDelay(getMockRoadmap(moduleSlug));
}
