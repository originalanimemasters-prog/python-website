from rest_framework import serializers

from apps.problems.models import PracticeQuestion
from apps.problems.serializers.example import PracticeExampleSerializer
from apps.problems.serializers.hint import PracticeHintSerializer
from apps.problems.serializers.solution import PracticeSolutionSerializer
from apps.problems.serializers.tag import TagSerializer
from apps.problems.serializers.test_case import PracticeTestCaseSerializer


class PracticeQuestionSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    examples = PracticeExampleSerializer(many=True, read_only=True)
    hints = PracticeHintSerializer(many=True, read_only=True)
    solutions = PracticeSolutionSerializer(many=True, read_only=True)
    test_cases = PracticeTestCaseSerializer(many=True, read_only=True)

    class Meta:
        model = PracticeQuestion
        fields = (
            "id",
            "title",
            "slug",
            "topic",
            "problem_statement",
            "input_format",
            "output_format",
            "constraints",
            "difficulty",
            "editorial",
            "is_active",
            "tags",
            "examples",
            "hints",
            "solutions",
            "test_cases",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "slug",
            "created_at",
            "updated_at",
        )