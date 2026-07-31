from rest_framework import serializers

from apps.problems.models import InterviewExample, PracticeExample


class BaseExampleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "input_data",
            "output_data",
            "explanation",
            "order",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )


class PracticeExampleSerializer(BaseExampleSerializer):
    class Meta(BaseExampleSerializer.Meta):
        model = PracticeExample


class InterviewExampleSerializer(BaseExampleSerializer):
    class Meta(BaseExampleSerializer.Meta):
        model = InterviewExample