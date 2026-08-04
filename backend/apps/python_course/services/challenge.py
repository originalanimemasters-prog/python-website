from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied

from apps.python_course.models import Challenge
from apps.python_course.services.lesson import LessonService


class ChallengeService:
    """
    Handles all challenge-related operations.
    """

    @classmethod
    def get_challenge(
        cls,
        user,
        lesson,
    ) -> Challenge:
        """
        Returns the active challenge for a lesson.
        """

        if not LessonService.can_access_lesson(
            user,
            lesson,
        ):
            raise PermissionDenied(
                "Subscription required to access this challenge."
            )

        return get_object_or_404(
            Challenge,
            lesson=lesson,
            is_active=True,
        )

    @classmethod
    def get_solution(
        cls,
        user,
        lesson,
    ) -> str:
        """
        Returns the challenge solution if the user
        has permission to view it.
        """

        challenge = cls.get_challenge(
            user,
            lesson,
        )

        if not cls.can_view_solution(
            user,
            lesson,
        ):
            raise PermissionDenied(
                "You are not allowed to view the solution."
            )

        return challenge.solution