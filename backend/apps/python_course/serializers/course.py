from rest_framework import serializers

from apps.python_course.models import (
    Course,
    Module,
    Topic,
)


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic

        fields = (
            "id",
            "title",
            "slug",
            "description",
            "order",
        )

        read_only_fields = (
            "id",
        )


class ModuleSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Module

        fields = (
            "id",
            "title",
            "slug",
            "description",
            "order",
            "topics",
        )

        read_only_fields = (
            "id",
        )


class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Course

        fields = (
            "id",
            "title",
            "slug",
            "description",
            "thumbnail",
            "is_free",
            "modules",
        )

        read_only_fields = (
            "id",
        )