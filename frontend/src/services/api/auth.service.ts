import axiosClient from "./axiosClient";

export interface LoginRequest {
  email: string;
  password: string;
}

export interface LoginResponse {
 access: string;
  refresh: string;
}

export async function login(
  data: LoginRequest
): Promise<LoginResponse> {
  const response = await axiosClient.post(
    "/auth/login/",
    data
  );

  return response.data;
}

// =======================
// Register
// =======================

export interface RegisterRequest {
  username: string;
  email: string;
  password: string;
}

export async function register(
  data: RegisterRequest
) {
  const response = await axiosClient.post(
    "/auth/register/",
    data
  );

  return response.data;
}

export async function verifyEmail(
  uid: string,
  token: string
) {
  const response = await axiosClient.get(
    `/auth/verify-email/?uid=${uid}&token=${token}`
  );

  return response.data;
}


export async function forgotPassword(
  email: string
) {
  const response = await axiosClient.post(
    "/auth/forgot-password/",
    {
      email,
    }
  );

  return response.data;
}

export interface ResetPasswordRequest {
  uid: string;
  token: string;
  new_password: string;
}

export async function resetPassword(
  data: ResetPasswordRequest
) {
  const response = await axiosClient.post(
    "/auth/reset-password/",
    data
  );

  return response.data;
}