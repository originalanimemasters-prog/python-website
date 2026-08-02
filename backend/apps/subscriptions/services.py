from __future__ import annotations

from datetime import timedelta
from typing import TYPE_CHECKING

from django.db import transaction
from django.utils import timezone

from apps.subscriptions.models import Subscription

if TYPE_CHECKING:
    from apps.accounts.models import User


MONTHLY_DURATION_DAYS = 30
YEARLY_DURATION_DAYS = 365


class SubscriptionService:
    """
    Central business logic for subscription management.

    All subscription-related operations should go through
    this service instead of being implemented inside views,
    serializers, permissions or admin.
    """

    @staticmethod
    def get_subscription(
        user: "User",
    ) -> Subscription | None:
        """
        Return the user's subscription.

        Returns None if no subscription exists.
        """

        try:
            return user.subscription

        except Subscription.DoesNotExist:
            return None

    @classmethod
    def has_active_subscription(
        cls,
        user: "User",
    ) -> bool:
        """
        Returns True only if the user has a valid
        active subscription.
        """

        subscription = cls.get_subscription(user)

        if subscription is None:
            return False

        if subscription.status != Subscription.Status.ACTIVE:
            return False

        # Lifetime subscriptions never expire.
        if subscription.plan_name == Subscription.Plan.LIFETIME:
            return True

        # Invalid state.
        if subscription.expires_at is None:
            return False

        now = timezone.now()

        if subscription.expires_at <= now:
            subscription.status = Subscription.Status.EXPIRED

            subscription.save(
                update_fields=[
                    "status",
                    "updated_at",
                ]
            )

            return False

        return True
    @staticmethod
    def subscription_days_remaining(
        subscription: Subscription,
    ) -> int:
        """
        Returns remaining subscription days from a Subscription object.

        Returns:
            -1 : Lifetime subscription
             0 : Expired / invalid subscription
            >0 : Remaining days
        """

        if subscription.plan_name == Subscription.Plan.LIFETIME:
            return -1

        if subscription.expires_at is None:
            return 0

        remaining = (
            timezone.localtime(
                subscription.expires_at
            ).date()
            - timezone.localdate()
        )

        return max(remaining.days, 0)

    @classmethod
    def days_remaining(
        cls,
        user: "User",
    ) -> int:
        """
        Returns remaining subscription days for a user.
        """

        subscription = cls.get_subscription(user)

        if subscription is None:
            return 0

        if not cls.has_active_subscription(user):
            return 0

        return cls.subscription_days_remaining(
            subscription
        )

    @classmethod
    @transaction.atomic
    def activate_subscription(
        cls,
        user: "User",
        plan: str,
    ) -> Subscription:
        """
        Creates or updates a user's subscription.
        """

        now = timezone.now()

        if plan == Subscription.Plan.MONTHLY:
            expires_at = now + timedelta(
                days=MONTHLY_DURATION_DAYS
            )

        elif plan == Subscription.Plan.YEARLY:
            expires_at = now + timedelta(
                days=YEARLY_DURATION_DAYS
            )

        elif plan == Subscription.Plan.LIFETIME:
            expires_at = None

        else:
            raise ValueError(
                f"Unsupported subscription plan: {plan}"
            )

        subscription, _ = (
            Subscription.objects.get_or_create(
                user=user,
            )
        )

        subscription = (
            Subscription.objects
            .select_for_update()
            .get(pk=subscription.pk)
        )

        subscription.plan_name = plan
        subscription.status = (
            Subscription.Status.ACTIVE
        )
        subscription.started_at = now
        subscription.expires_at = expires_at

        subscription.full_clean()

        subscription.save(
            update_fields=[
                "plan_name",
                "status",
                "started_at",
                "expires_at",
                "updated_at",
            ]
        )

        return subscription
    @classmethod
    @transaction.atomic
    def cancel_subscription(
        cls,
        user: "User",
    ) -> bool:
        """
        Cancels the user's subscription.

        Returns:
            True  -> Subscription cancelled.
            False -> No subscription found or already cancelled.
        """

        subscription = cls.get_subscription(user)

        if subscription is None:
            return False

        if subscription.status == Subscription.Status.CANCELLED:
            return False

        subscription.status = Subscription.Status.CANCELLED

        subscription.full_clean()

        subscription.save(
            update_fields=[
                "status",
                "updated_at",
            ]
        )

        return True