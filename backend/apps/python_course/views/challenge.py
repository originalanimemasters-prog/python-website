from rest_framework import generics

from apps.python_course.serializers import (
    ChallengeSerializer,
)
from apps.python_course.services import (
    ChallengeService,
    LessonService,
)


class ChallengeDetailView(generics.RetrieveAPIView):
    """
    Returns the active challenge for a lesson.
    """

    serializer_class = ChallengeSerializer
    lookup_field = "slug"

    def get_object(self):
        lesson = LessonService.get_lesson_by_slug(
            self.kwargs["slug"],
        )

        return ChallengeService.get_challenge(
            self.request.user,
            lesson,
        )