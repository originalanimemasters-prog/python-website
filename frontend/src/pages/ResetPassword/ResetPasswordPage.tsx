import { useEffect, useState } from "react";
import { Link, useNavigate, useSearchParams } from "react-router-dom";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { Loader2, Lock } from "lucide-react";

import { resetPassword } from "@/services/api/auth.service";
import { Button } from "@/components/ui/Button";
import { Card, CardContent } from "@/components/ui/Card";
import { Input } from "@/components/ui/Input";
import { Label } from "@/components/ui/Label";

const schema = z
  .object({
    password: z
      .string()
      .min(8, "Password must be at least 8 characters"),
    confirmPassword: z.string(),
  })
  .refine((data) => data.password === data.confirmPassword, {
    path: ["confirmPassword"],
    message: "Passwords do not match",
  });

type ResetPasswordForm = z.infer<typeof schema>;

export default function ResetPasswordPage() {
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();

  const uid = searchParams.get("uid");
  const token = searchParams.get("token");

  const [loading, setLoading] = useState(false);
  const [successMessage, setSuccessMessage] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<ResetPasswordForm>({
    resolver: zodResolver(schema),
  });

  useEffect(() => {
    if (!successMessage) return;

    const timer = setTimeout(() => {
      navigate("/login");
    }, 3000);

    return () => clearTimeout(timer);
  }, [successMessage, navigate]);

  if (!uid || !token) {
    return (
      <Card className="w-full max-w-md">
        <CardContent className="p-8 text-center">
          <h1 className="mb-4 text-2xl font-bold">
            Invalid Reset Link
          </h1>

          <p className="mb-6 text-sm text-gray-600">
            This password reset link is invalid or has expired.
          </p>

          <Button asChild className="w-full">
            <Link to="/forgot-password">
              Request New Reset Link
            </Link>
          </Button>
        </CardContent>
      </Card>
    );
  }

  const onSubmit = async (data: ResetPasswordForm) => {
    setErrorMessage("");

    try {
      setLoading(true);

      await resetPassword({
        uid,
        token,
        new_password: data.password,
      });

      setSuccessMessage(
        "Password reset successfully! Redirecting to login..."
      );
    } catch (error: any) {
      console.error(error);

      setErrorMessage(
        error?.response?.data?.detail ||
          "Failed to reset password. The link may be invalid or expired."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <Card className="w-full max-w-md">
      <CardContent className="p-8">
        <h1 className="mb-6 text-center text-2xl font-bold">
          Reset Password
        </h1>

        {successMessage && (
          <div className="mb-4 space-y-4">
            <div className="rounded-md border border-green-200 bg-green-50 p-3 text-sm text-green-700">
              {successMessage}
            </div>

            <Button asChild className="w-full">
              <Link to="/login">Go to Login</Link>
            </Button>
          </div>
        )}

        {errorMessage && (
          <div className="mb-4 rounded-md border border-red-200 bg-red-50 p-3 text-sm text-red-700">
            {errorMessage}
          </div>
        )}

        {!successMessage && (
          <form
            onSubmit={handleSubmit(onSubmit)}
            className="space-y-4"
          >
            <div>
              <Label htmlFor="password">
                New Password
              </Label>

              <Input
                id="password"
                type="password"
                disabled={loading}
                {...register("password")}
              />

              {errors.password && (
                <p className="mt-1 text-sm text-red-500">
                  {errors.password.message}
                </p>
              )}
            </div>

            <div>
              <Label htmlFor="confirmPassword">
                Confirm Password
              </Label>

              <Input
                id="confirmPassword"
                type="password"
                disabled={loading}
                {...register("confirmPassword")}
              />

              {errors.confirmPassword && (
                <p className="mt-1 text-sm text-red-500">
                  {errors.confirmPassword.message}
                </p>
              )}
            </div>

            <Button
              type="submit"
              disabled={loading}
              className="w-full"
            >
              {loading ? (
                <>
                  <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                  Resetting...
                </>
              ) : (
                <>
                  <Lock className="mr-2 h-4 w-4" />
                  Reset Password
                </>
              )}
            </Button>
          </form>
        )}
      </CardContent>
    </Card>
  );
}