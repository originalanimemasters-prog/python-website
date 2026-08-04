from rest_framework import generics

from apps.python_course.serializers import (
    QuizSerializer,
)
from apps.python_course.services import (
    LessonService,
    QuizService,
)


class QuizDetailView(generics.RetrieveAPIView):
    """
    Returns the active quiz for a lesson.
    """

    serializer_class = QuizSerializer
    lookup_field = "slug"

    def get_object(self):
        lesson = LessonService.get_lesson_by_slug(
            self.kwargs["slug"],
        )

        return QuizService.get_quiz(
            self.request.user,
            lesson,
        )