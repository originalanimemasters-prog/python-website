import { useQuery } from "@tanstack/react-query";
import { fetchDashboardData, fetchUserProfile } from "@/services/api/user.service";

export function useUserProfile() {
  return useQuery({
    queryKey: ["user", "profile"],
    queryFn: fetchUserProfile,
  });
}

export function useDashboardData() {
  return useQuery({
    queryKey: ["dashboard"],
    queryFn: fetchDashboardData,
  });
}
