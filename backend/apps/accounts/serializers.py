from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import (
    urlsafe_base64_decode,
    urlsafe_base64_encode,
)
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
        ]

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Email already exists."
            )
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        verification_url = (
            f"{settings.FRONTEND_URL}"
            f"/verify-email?uid={uid}&token={token}"
        )

        send_mail(
            subject="Verify your DevForge account",
            message=(
                f"Hi {user.username},\n\n"
                f"Please verify your email by clicking the link below:\n\n"
                f"{verification_url}\n\n"
                f"If you didn't create this account, "
                f"please ignore this email."
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "role",
            "is_verified",
            "created_at",
        ]

        read_only_fields = [
            "role",
            "is_verified",
            "created_at",
        ]


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = User.objects.filter(email=email).first()

        if not user:
            raise serializers.ValidationError(
                "Invalid email or password."
            )

        user = authenticate(
            username=user.username,
            password=password,
        )

        if not user:
            raise serializers.ValidationError(
                "Invalid email or password."
            )

        if not user.is_verified:
            raise serializers.ValidationError(
                "Please verify your email before logging in."
            )

        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": UserSerializer(user).data,
        }

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def save(self):
        token = RefreshToken(
            self.validated_data["refresh"]
        )
        token.blacklist()


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(
        write_only=True
    )

    new_password = serializers.CharField(
        write_only=True,
        min_length=8,
    )

    def validate(self, attrs):
        user = self.context["request"].user

        if not user.check_password(
            attrs["old_password"]
        ):
            raise serializers.ValidationError(
                {
                    "old_password":
                    "Old password is incorrect."
                }
            )

        return attrs

    def save(self):
        user = self.context["request"].user

        user.set_password(
            self.validated_data["new_password"]
        )

        user.save()


# --------------------------
# Forgot Password
# --------------------------

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def save(self):
        email = self.validated_data["email"]

        try:
            user = User.objects.get(email=email)

            uid = urlsafe_base64_encode(
                force_bytes(user.pk)
            )

            token = default_token_generator.make_token(
                user
            )

            reset_url = (
                    f"{settings.FRONTEND_URL}"
                    f"/reset-password?uid={uid}&token={token}"
                )

            send_mail(
                subject="Reset your DevForge password",
                message=(
                    f"Hi {user.username},\n\n"
                    f"Click the link below to reset "
                    f"your password:\n\n"
                    f"{reset_url}\n\n"
                    f"If you didn't request this, "
                    f"please ignore this email."
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )

        except User.DoesNotExist:
            pass

        return {
            "message":
            (
                "If an account with this email exists, "
                "a password reset link has been sent."
            )
        }


# --------------------------
# Reset Password
# --------------------------

class ResetPasswordSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()

    new_password = serializers.CharField(
        min_length=8,
        write_only=True,
    )

    def validate(self, attrs):
        try:
            uid = force_str(
                urlsafe_base64_decode(
                    attrs["uid"]
                )
            )

            user = User.objects.get(pk=uid)

        except Exception:
            raise serializers.ValidationError(
                "Invalid password reset link."
            )

        if not default_token_generator.check_token(
            user,
            attrs["token"],
        ):
            raise serializers.ValidationError(
                "Invalid or expired password reset link."
            )

        attrs["user"] = user

        return attrs

    def save(self):
        user = self.validated_data["user"]

        user.set_password(
            self.validated_data["new_password"]
        )

        user.save()

        return {
            "message":
            "Password reset successfully."
        }