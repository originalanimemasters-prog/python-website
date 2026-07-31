from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import EmailOTP
from django.utils import timezone
from datetime import timedelta

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
        email = validated_data["email"]

        otp = EmailOTP.objects.filter(
            email=email,
            purpose=EmailOTP.Purpose.SIGNUP,
            is_used=True,
        ).order_by("-created_at").first()

        if not otp:
            raise serializers.ValidationError(
                {
                "email": "Please verify your email first."
                }
            )

        if otp.verified_at is None:
            raise serializers.ValidationError(
                {
                "email": "Email verification is invalid."
                }
            )

        if timezone.now() > otp.verified_at + timedelta(minutes=10):
            otp.delete()

            raise serializers.ValidationError(
                {
                    "email": (
                        "Email verification has expired. "
                        "Please verify again."
                    )
                }
            )

        user = User.objects.create_user(**validated_data)

        user.is_verified = True
        user.save(update_fields=["is_verified"])
                   
        otp.delete()

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

class UserProfileSerializer(serializers.ModelSerializer):
    xp = serializers.IntegerField(source="progress.xp", read_only=True)

    level = serializers.IntegerField(source="progress.level", read_only=True)

    current_streak = serializers.IntegerField(
        source="progress.current_streak",
        read_only=True,
    )

    longest_streak = serializers.IntegerField(
        source="progress.longest_streak",
        read_only=True,
    )
    initials = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "role",
            "is_verified",
            "initials",
            "xp",
            "level",
            "current_streak",
            "longest_streak",
            "created_at",
        ]

    def get_initials(self, obj):
        if obj.username:
            return obj.username[:2].upper()
        return "DF"

class SendOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()

class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(
        min_length=6,
        max_length=6,
    )