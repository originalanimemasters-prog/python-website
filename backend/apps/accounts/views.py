from django.contrib.auth import get_user_model, update_session_auth_hash
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenRefreshView
from .email_service import EmailService
from .services import OTPService
from .models import EmailOTP
from django.utils import timezone

from .serializers import (
    ForgotPasswordSerializer,
    LoginSerializer,
    LogoutSerializer,
    PasswordChangeSerializer,
    RegisterSerializer,
    ResetPasswordSerializer,
    SendOTPSerializer,
    VerifyOTPSerializer,
    UserProfileSerializer,
)

User = get_user_model()


@api_view(["GET"])
def health_check(request):
    return Response(
        {
            "status": "success",
            "message": "DevForge Backend is running 🚀",
        }
    )


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    throttle_scope = "register"

    def perform_create(self, serializer):
        serializer.save()

class LoginView(APIView):
    permission_classes = [AllowAny]
    throttle_scope = "login"

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            serializer.validated_data,
            status=status.HTTP_200_OK,
        )


class RefreshView(TokenRefreshView):
    permission_classes = [AllowAny]


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"message": "Logged out successfully."},
            status=status.HTTP_200_OK,
        )


class MeView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class PasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PasswordChangeSerializer(
            data=request.data,
            context={"request": request},
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        update_session_auth_hash(request, request.user)

        return Response(
            {"message": "Password changed successfully."},
            status=status.HTTP_200_OK,
        )


# ---------------------------------------
# Forgot Password
# ---------------------------------------

class ForgotPasswordView(APIView):
    permission_classes = [AllowAny]
    throttle_scope = "forgot_password"

    def post(self, request):
        serializer = ForgotPasswordSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        return Response(
            serializer.save(),
            status=status.HTTP_200_OK,
        )


# ---------------------------------------
# Reset Password
# ---------------------------------------

class ResetPasswordView(APIView):
    permission_classes = [AllowAny]
    throttle_scope = "reset_password"

    def post(self, request):
        serializer = ResetPasswordSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        return Response(
            serializer.save(),
            status=status.HTTP_200_OK,
        )

class TestEmailView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):

        success = EmailService.send_email(
            to_email="originalanimemasters@gmail.com",
            subject="DevForge Email Test 🚀",
            html="""
            <h1>DevForge</h1>
            <p>If you're seeing this email, Resend is working correctly.</p>
            <h3>🎉 Congratulations!</h3>
            """,
        )

        if success:
            return Response({"message": "Email sent successfully."})

        return Response(
            {"message": "Failed to send email."},
            status=500,
        )


class SendOTPView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    throttle_scope = "send_otp"

    def post(self, request):
        serializer = SendOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]

        OTPService.create_otp(
            email=email,
            purpose=EmailOTP.Purpose.SIGNUP,
        )

        return Response(
            {
                "message": "OTP sent successfully."
            },
            status=status.HTTP_200_OK,
        )


class VerifyOTPView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    throttle_scope = "verify_otp"

    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        otp = serializer.validated_data["otp"]

        otp_object = EmailOTP.objects.filter(
            email=email,
            purpose=EmailOTP.Purpose.SIGNUP,
            is_used=False,
        ).order_by("-created_at").first()

        if not otp_object:
            return Response(
                {"message": "OTP not found."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if otp_object.expires_at < timezone.now():
            return Response(
                {"message": "OTP has expired."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not OTPService.verify_otp(
            otp_object,
            otp,
        ):
            otp_object.attempts += 1

            if otp_object.attempts >= 5:
                otp_object.delete()

                return Response(
                    {
                        "message": (
                            "Too many invalid attempts. "
                            "Please request a new OTP."
                        )
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            otp_object.save(update_fields=["attempts"])

            return Response(
                {
                    "message": "Invalid OTP."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        otp_object.is_used = True
        otp_object.verified_at = timezone.now()

        otp_object.save(
            update_fields=[
                "is_used",
                "verified_at",
            ]
        )

        return Response(
            {
                "message": "OTP verified successfully."
            },
            status=status.HTTP_200_OK,
        )