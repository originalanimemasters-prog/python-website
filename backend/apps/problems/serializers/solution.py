from rest_framework import serializers

from apps.problems.models import PracticeSolution, InterviewSolution


class BaseSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "language",
            "code",
            "explanation",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )


class PracticeSolutionSerializer(BaseSolutionSerializer):
    class Meta(BaseSolutionSerializer.Meta):
        model = PracticeSolution


class InterviewSolutionSerializer(BaseSolutionSerializer):
    class Meta(BaseSolutionSerializer.Meta):
        model = InterviewSolution