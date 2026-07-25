import { getMockDashboardData, getMockUserProfile } from "@/services/mock/user.mock";
import { withDelay } from "./delay";
import type { DashboardData, UserProfile } from "@/types";

export async function fetchUserProfile(): Promise<UserProfile> {
  // Future: return apiClient.get(`/users/me/profile`).then(r => r.data);
  return withDelay(getMockUserProfile());
}

export async function fetchDashboardData(): Promise<DashboardData> {
  // Future: return apiClient.get(`/users/me/dashboard`).then(r => r.data);
  return withDelay(getMockDashboardData());
}
