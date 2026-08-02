from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from apps.subscriptions.services import SubscriptionService


class IsPremiumUser(BasePermission):
    """
    Allows access only to users with an active subscription.
    """

    message = "Premium subscription required."

    def has_permission(
        self,
        request: Request,
        view: APIView,
    ) -> bool:

        user = request.user

        if not user.is_authenticated:
            return False

        return SubscriptionService.has_active_subscription(user)