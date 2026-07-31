import axiosClient from "./axiosClient";
import { getMockDashboardData } from "@/services/mock/user.mock";
import { withDelay } from "./delay";
import type { DashboardData, UserProfile } from "@/types";

export async function fetchUserProfile(): Promise<UserProfile> {
  const response = await axiosClient.get("/auth/me/");

  const data = response.data;

  return {
    id: data.id,
    username: data.username,
    email: data.email,

    initials: data.initials,
    avatarUrl: null,

    role: data.role,

    xp: data.xp,
    level: data.level,

    currentStreak: data.current_streak,
    longestStreak: data.longest_streak,

    totalLessonsCompleted: 0,

    badges: [],

    joinedAt: data.created_at,

    isVerified: data.is_verified,
    isPremium: false,
  };
}

export async function fetchDashboardData(): Promise<DashboardData> {
  return withDelay(getMockDashboardData());
}