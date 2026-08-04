from rest_framework import serializers

from apps.python_course.models import Challenge

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge

        fields = (
            "id",
            "title",
            "description",
            "difficulty",
            "starter_code",
            "expected_output",
            "hint",
        )

        read_only_fields = (
            "id",
        )