from rest_framework import serializers

from apps.python_course.models import (
    Quiz,
    QuizQuestion,
    QuizOption,
)

class QuizOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizOption

        fields = (
            "id",
            "option_text",
        )

        read_only_fields = (
            "id",
        )
class QuizQuestionSerializer(serializers.ModelSerializer):
    options = QuizOptionSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = QuizQuestion

        fields = (
            "id",
            "question",
            "order",
            "options",
        )

        read_only_fields = (
            "id",
        )
class QuizSerializer(serializers.ModelSerializer):
    questions = QuizQuestionSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Quiz

        fields = (
            "id",
            "title",
            "description",
            "passing_score",
            "questions",
        )

        read_only_fields = (
            "id",
        )