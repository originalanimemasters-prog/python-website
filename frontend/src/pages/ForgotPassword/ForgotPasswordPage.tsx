import { useState } from "react";
import { Link } from "react-router-dom";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { Loader2, Mail } from "lucide-react";

import { forgotPassword } from "@/services/api/auth.service";
import { Button } from "@/components/ui/Button";
import { Card, CardContent } from "@/components/ui/Card";
import { Input } from "@/components/ui/Input";
import { Label } from "@/components/ui/Label";
import { ROUTES } from "@/utils/constants";

const schema = z.object({
  email: z.string().email("Enter a valid email"),
});

type ForgotPasswordForm = z.infer<typeof schema>;

export default function ForgotPasswordPage() {
  const [loading, setLoading] = useState(false);
  const [successMessage, setSuccessMessage] = useState("");

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<ForgotPasswordForm>({
    resolver: zodResolver(schema),
  });

  const onSubmit = async (data: ForgotPasswordForm) => {
    try {
      setLoading(true);

      const response = await forgotPassword(data.email);

      setSuccessMessage(
        response.message ||
          "If an account exists, a reset link has been sent."
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
            <Mail className="mx-auto mb-3 h-10 w-10" />

            <h1 className="text-2xl font-bold">
              Forgot Password
            </h1>

            <p className="mt-2 text-sm text-muted-foreground">
              Enter your email and we'll send you a password reset link.
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
                <Label>Email</Label>

                <Input
                  type="email"
                  placeholder="you@example.com"
                  {...register("email")}
                />

                {errors.email && (
                  <p className="mt-1 text-xs text-red-500">
                    {errors.email.message}
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
                  ? "Sending..."
                  : "Send Reset Link"}
              </Button>
            </form>
          )}

        </CardContent>
      </Card>
    </div>
  );
}