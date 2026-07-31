from rest_framework import serializers

from apps.problems.models import InterviewQuestion
from apps.problems.serializers.company import CompanySerializer
from apps.problems.serializers.example import InterviewExampleSerializer
from apps.problems.serializers.hint import InterviewHintSerializer
from apps.problems.serializers.solution import InterviewSolutionSerializer
from apps.problems.serializers.tag import TagSerializer
from apps.problems.serializers.test_case import InterviewTestCaseSerializer


class InterviewQuestionSerializer(serializers.ModelSerializer):
    companies = CompanySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    examples = InterviewExampleSerializer(many=True, read_only=True)
    hints = InterviewHintSerializer(many=True, read_only=True)
    solutions = InterviewSolutionSerializer(many=True, read_only=True)
    test_cases = InterviewTestCaseSerializer(many=True, read_only=True)

    class Meta:
        model = InterviewQuestion
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
            "companies",
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