from rest_framework import serializers

from apps.problems.models import PracticeHint, InterviewHint


class BaseHintSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "content",
            "order",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )


class PracticeHintSerializer(BaseHintSerializer):
    class Meta(BaseHintSerializer.Meta):
        model = PracticeHint


class InterviewHintSerializer(BaseHintSerializer):
    class Meta(BaseHintSerializer.Meta):
        model = InterviewHint