from rest_framework import serializers

from apps.subscriptions.models import Subscription
from apps.subscriptions.services import SubscriptionService


class SubscriptionSerializer(serializers.ModelSerializer):
    days_remaining = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = (
            "plan_name",
            "status",
            "started_at",
            "expires_at",
            "days_remaining",
        )
        read_only_fields = fields

    def get_days_remaining(self, obj):
        return SubscriptionService.subscription_days_remaining(obj)