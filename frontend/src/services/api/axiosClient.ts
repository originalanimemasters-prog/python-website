import axios from "axios";

/**
 * Preconfigured Axios instance. Domain services currently call the mock layer
 * (see src/services/mock) so the UI can be built and demoed without a backend.
 * Swapping a service to real data is a one-line change inside that service file —
 * point it at `apiClient.get(...)` instead of the mock function. No component changes needed.
 */
export const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL ?? "/api/v1",
  timeout: 15000,
  headers: {
    "Content-Type": "application/json",
  },
});

apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem("devforge_access_token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem("devforge_access_token");
    }
    return Promise.reject(error);
  }
);
