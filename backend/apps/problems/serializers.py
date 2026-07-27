from rest_framework import serializers

from .models import (
    Company,
    Problem,
    ProblemExample,
    StarterCode,
    Tag,
)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "slug"]


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "slug"]


class ProblemExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemExample
        fields = [
            "id",
            "input",
            "output",
            "explanation",
            "order",
        ]


class StarterCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarterCode
        fields = [
            "id",
            "language",
            "code",
        ]


class ProblemListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Problem
        fields = [
            "id",
            "title",
            "slug",
            "difficulty",
            "is_premium",
            "tags",
        ]


class ProblemDetailSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    companies = CompanySerializer(many=True, read_only=True)
    examples = ProblemExampleSerializer(many=True, read_only=True)
    starter_codes = StarterCodeSerializer(many=True, read_only=True)

    class Meta:
        model = Problem
        fields = [
            "id",
            "title",
            "slug",
            "difficulty",
            "description",
            "input_format",
            "output_format",
            "constraints",
            "hints",
            "editorial",
            "is_premium",
            "is_published",
            "tags",
            "companies",
            "examples",
            "starter_codes",
            "created_at",
            "updated_at",
        ]