from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import timedelta
from apps.subscriptions.services import SubscriptionService


class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "student", "Student"
        ADMIN = "admin", "Admin"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT,
    )

    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    # ==========================
    # Subscription Helpers
    # ==========================

    def has_active_subscription(self):
        return SubscriptionService.has_active_subscription(self)

    def subscription_days_remaining(self):
        return SubscriptionService.days_remaining(self)

    def subscription_status(self):
        try:
            return self.subscription.status
        except Exception:
            return None


class UserProgress(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="progress",
    )

    xp = models.PositiveIntegerField(default=0)

    level = models.PositiveIntegerField(default=1)

    current_streak = models.PositiveIntegerField(default=0)

    longest_streak = models.PositiveIntegerField(default=0)

    last_activity_date = models.DateField(
        null=True,
        blank=True,
    )

    streak_restores_remaining = models.PositiveSmallIntegerField(default=5)

    total_xp_earned = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} Progress"

class EmailOTP(models.Model):

    class Purpose(models.TextChoices):
        SIGNUP = "signup", "Sign Up"
        LOGIN = "login", "Login"
        FORGOT_PASSWORD = "forgot_password", "Forgot Password"
        CHANGE_EMAIL = "change_email", "Change Email"

    email = models.EmailField(db_index=True)

    otp_hash = models.CharField(max_length=255)

    purpose = models.CharField(
        max_length=30,
        choices=Purpose.choices,
    )

    attempts = models.PositiveSmallIntegerField(default=0)

    is_used = models.BooleanField(default=False)

    verified_at = models.DateTimeField(
        null=True,
        blank=True,
        )

    expires_at = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["email", "purpose"]),
        ]

    def is_expired(self):
        return timezone.now() >= self.expires_at

    def __str__(self):
        return f"{self.email} ({self.purpose})"
    