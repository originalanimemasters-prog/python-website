from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.subscriptions.serializers import SubscriptionSerializer
from apps.subscriptions.services import SubscriptionService


class MySubscriptionAPIView(APIView):
    """
    Returns the authenticated user's subscription details.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Refresh subscription status if expired.
        SubscriptionService.has_active_subscription(
            request.user
        )

        subscription = (
            SubscriptionService.get_subscription(
                request.user
            )
        )

        if subscription is None:
            return Response(
                {
                    "subscription": None,
                    "message": "No active subscription.",
                },
                status=status.HTTP_200_OK,
            )

        serializer = SubscriptionSerializer(
            subscription
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )