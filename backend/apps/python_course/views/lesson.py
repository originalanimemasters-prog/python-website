from rest_framework import generics

from apps.python_course.serializers import (
    LessonDetailSerializer,
)
from apps.python_course.services import (
    LessonService,
)


class LessonDetailView(generics.RetrieveAPIView):
    """
    Returns a published lesson with its content.
    """

    serializer_class = LessonDetailSerializer
    lookup_field = "slug"

    def get_object(self):
        user = self.request.user
        slug = self.kwargs["slug"]

        return LessonService.get_lesson_content(
            user,
            slug
        )