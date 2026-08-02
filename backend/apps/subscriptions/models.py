from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError

class Subscription(models.Model):
    class Plan(models.TextChoices):
        MONTHLY = "MONTHLY", "Monthly"
        YEARLY = "YEARLY", "Yearly"
        LIFETIME = "LIFETIME", "Lifetime"

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        EXPIRED = "EXPIRED", "Expired"
        CANCELLED = "CANCELLED", "Cancelled"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="subscription",
    )

    plan_name = models.CharField(
        max_length=20,
        choices=Plan.choices,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
    )

    started_at = models.DateTimeField()

    expires_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "subscriptions"
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.user.username} | "
            f"{self.get_plan_name_display()} | "
            f"{self.get_status_display()}"
        )
        
        
    def clean(self):
        if (
            self.plan_name == self.Plan.LIFETIME
            and self.expires_at is not None
        ):
            raise ValidationError(
                "Lifetime subscription cannot have an expiry date."
            )

        if (
            self.plan_name != self.Plan.LIFETIME
            and self.expires_at is None
        ):
            raise ValidationError(
                "Expiry date is required."
            )

        if (
            self.expires_at
            and self.expires_at <= self.started_at
        ):
            raise ValidationError(
                "Expiry date must be after started_at."
            )