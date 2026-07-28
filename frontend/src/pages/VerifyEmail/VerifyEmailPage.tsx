import { useEffect, useState } from "react";
import { Link, useSearchParams } from "react-router-dom";
import { CheckCircle2, XCircle, Loader2 } from "lucide-react";

import { verifyEmail } from "@/services/api/auth.service";
import { Card, CardContent } from "@/components/ui/Card";
import { Button } from "@/components/ui/Button";
import { ROUTES } from "@/utils/constants";

export default function VerifyEmailPage() {
  const [searchParams] = useSearchParams();

  const [loading, setLoading] = useState(true);
  const [success, setSuccess] = useState(false);
  const [message, setMessage] = useState("Verifying your email...");

  useEffect(() => {
    const uid = searchParams.get("uid");
    const token = searchParams.get("token");

    if (!uid || !token) {
      setLoading(false);
      setSuccess(false);
      setMessage("Invalid verification link.");
      return;
    }
    const verifiedUid = uid;
    const verifiedToken = token;

    async function verify() {
      try {
        const response = await verifyEmail(
        verifiedUid,
        verifiedToken
        );

        setSuccess(true);
        setMessage(
          response.message || "Email verified successfully."
        );
      } catch (error: any) {
        setSuccess(false);

        setMessage(
          error?.response?.data?.message ||
            "Verification failed."
        );
      } finally {
        setLoading(false);
      }
    }

    verify();
  }, [searchParams]);

  return (
    <div className="flex min-h-[calc(100vh-4rem)] items-center justify-center px-4">
      <Card className="w-full max-w-md">
        <CardContent className="p-8 text-center">

          {loading ? (
            <>
              <Loader2 className="mx-auto mb-4 h-10 w-10 animate-spin" />
              <h2 className="text-xl font-bold">
                Verifying Email
              </h2>
              <p className="mt-3 text-muted-foreground">
                Please wait...
              </p>
            </>
          ) : success ? (
            <>
              <CheckCircle2 className="mx-auto mb-4 h-12 w-12 text-green-500" />

              <h2 className="text-xl font-bold">
                Email Verified
              </h2>

              <p className="mt-3 text-muted-foreground">
                {message}
              </p>

              <Button asChild className="mt-6 w-full">
                <Link to={ROUTES.login}>
                  Go to Login
                </Link>
              </Button>
            </>
          ) : (
            <>
              <XCircle className="mx-auto mb-4 h-12 w-12 text-red-500" />

              <h2 className="text-xl font-bold">
                Verification Failed
              </h2>

              <p className="mt-3 text-muted-foreground">
                {message}
              </p>

              <Button
                asChild
                variant="outline"
                className="mt-6 w-full"
              >
                <Link to={ROUTES.signup}>
                  Back to Signup
                </Link>
              </Button>
            </>
          )}
        </CardContent>
      </Card>
    </div>
  );
}