import { useQuery } from "@tanstack/react-query";
import { fetchRoadmap } from "@/services/api/roadmap.service";

export function useRoadmap(moduleSlug: string) {
  return useQuery({
    queryKey: ["roadmap", moduleSlug],
    queryFn: () => fetchRoadmap(moduleSlug),
  });
}
