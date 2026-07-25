import { MOCK_API_DELAY_MS } from "@/utils/constants";

export function withDelay<T>(value: T, ms: number = MOCK_API_DELAY_MS): Promise<T> {
  return new Promise((resolve) => setTimeout(() => resolve(value), ms));
}
