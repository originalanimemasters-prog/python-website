import { useState } from "react";
import { Link, useSearchParams } from "react-router-dom";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { Loader2, Lock } from "lucide-react";

import { resetPassword } from "@/services/api/auth.service";
import { Button } from "@/components/ui/Button";
import { Card, CardContent } from "@/components/ui/Card";
import { Input } from "@/components/ui/Input";
import { Label } from "@/components/ui/Label";
import { ROUTES } from "@/utils/constants";

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

  const uid = searchParams.get("uid");
  const token = searchParams.get("token");

  const [loading, setLoading] = useState(false);
  const [successMessage, setSuccessMessage] = useState("");

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<ResetPasswordForm>({
    resolver: zodResolver(schema),
  });

  const onSubmit = async (data: ResetPasswordForm) => {
    if (!uid || !token) {
      alert("Invalid password reset link.");
      return;
    }

    try {
      setLoading(true);

      const response = await resetPassword({
        uid,
        token,
        new_password: data.password,
      });

      setSuccessMessage(
        response.message ||
          "Your password has been reset successfully."
      );
    } catch (error: any) {
      alert(
        error?.response?.data?.message ||
          "Something went wrong."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex min-h-[calc(100vh-4rem)] items-center justify-center px-4">
      <Card className="w-full max-w-md">
        <CardContent className="p-8">

          <div className="mb-6 text-center">
            <Lock className="mx-auto mb-3 h-10 w-10" />

            <h1 className="text-2xl font-bold">
              Reset Password
            </h1>

            <p className="mt-2 text-sm text-muted-foreground">
              Enter your new password below.
            </p>
          </div>

          {successMessage ? (
            <>
              <p className="rounded bg-green-100 p-3 text-sm">
                {successMessage}
              </p>

              <Button
                asChild
                className="mt-6 w-full"
              >
                <Link to={ROUTES.login}>
                  Back to Login
                </Link>
              </Button>
            </>
          ) : (
            <form
              onSubmit={handleSubmit(onSubmit)}
              className="space-y-4"
            >
              <div>
                <Label>New Password</Label>

                <Input
                  type="password"
                  {...register("password")}
                />

                {errors.password && (
                  <p className="mt-1 text-xs text-red-500">
                    {errors.password.message}
                  </p>
                )}
              </div>

              <div>
                <Label>Confirm Password</Label>

                <Input
                  type="password"
                  {...register("confirmPassword")}
                />

                {errors.confirmPassword && (
                  <p className="mt-1 text-xs text-red-500">
                    {errors.confirmPassword.message}
                  </p>
                )}
              </div>

              <Button
                type="submit"
                disabled={loading}
                className="w-full"
              >
                {loading && (
                  <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                )}

                {loading
                  ? "Updating..."
                  : "Reset Password"}
              </Button>
            </form>
          )}

        </CardContent>
      </Card>
    </div>
  );
}
