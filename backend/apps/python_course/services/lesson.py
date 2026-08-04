from django.db.models import Prefetch, QuerySet
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from apps.python_course.models import Lesson
from apps.subscriptions.services import SubscriptionService

class LessonService:
    """
    Handles all public lesson-related operations.
    """

    @classmethod
    def get_lesson_by_id(cls, lesson_id: int) -> Lesson:
        """
        Returns a published lesson by ID.
        Raises 404 if the lesson does not exist.
        """

        return get_object_or_404(
            Lesson,
            id=lesson_id,
            status=Lesson.Status.PUBLISHED,
        )
    @classmethod
    def get_lessons_by_topic(cls, topic) -> QuerySet[Lesson]:
        """
        Returns all published lessons for a topic.
        """
    
        return (
            Lesson.objects.filter(
                topic=topic,
                status=Lesson.Status.PUBLISHED,
            )
            .order_by("order")
        )
    @classmethod
    def get_lesson_by_slug(cls, slug: str) -> Lesson:
        """
        Returns a published lesson by slug.
        """
    
        return get_object_or_404(
            Lesson,
            slug=slug,
            status=Lesson.Status.PUBLISHED,
        )
    @classmethod
    def can_access_lesson(
        cls,
        user,
        lesson: Lesson,
    ) -> bool:
        """
        Checks whether the user can access a lesson.
        """
    
        if lesson.is_free:
            return True
    
        if not user.is_authenticated:
            return False
    
        return SubscriptionService.has_active_subscription(
            user
        )
    @classmethod
    def get_lesson_content(
        cls,
        user,
        slug: str,
    ) -> Lesson:
        lesson = get_object_or_404(
            Lesson.objects.prefetch_related(
                "content_blocks",
                "quiz__questions__options",
                "challenge",
            ),
            slug=slug,
            status=Lesson.Status.PUBLISHED,
        )
    
        if not cls.can_access_lesson(user, lesson):
            raise PermissionDenied(
                "Subscription required to access this lesson."
            )
    
        return lesson