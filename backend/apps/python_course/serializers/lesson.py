from rest_framework import serializers

from apps.python_course.models import (
    ContentBlock,
    Lesson,
)

class ContentBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentBlock

        fields = (
            "id",
            "block_type",
            "title",
            "order",
            "markdown",
            "image",
        )

        read_only_fields = (
            "id",
        )
        
class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson

        fields = (
            "id",
            "title",
            "slug",
            "short_description",
            "order",
            "is_free",
        )

        read_only_fields = (
            "id",
        )
        
class LessonDetailSerializer(serializers.ModelSerializer):
    content_blocks = ContentBlockSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Lesson

        fields = (
            "id",
            "title",
            "slug",
            "short_description",
            "order",
            "is_free",
            "content_blocks",
        )

        read_only_fields = (
            "id",
        )