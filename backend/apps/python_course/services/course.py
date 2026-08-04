from django.db.models import Prefetch, QuerySet
from django.shortcuts import get_object_or_404

from apps.python_course.models import (
    Course,
    Module,
    Topic,
)


class CourseService:
    """
    Handles all public course-related operations.
    """

    @classmethod
    def get_courses(cls) -> QuerySet[Course]:
        """
        Returns all published courses.
        """

        return (
            Course.objects.filter(
                status=Course.Status.PUBLISHED,
            )
            .order_by("title")
        )

    @classmethod
    def get_course_by_slug(cls, slug: str) -> Course:
        """
        Returns a published course by slug.
        Raises 404 if the course does not exist.
        """

        return get_object_or_404(
            Course,
            slug=slug,
            status=Course.Status.PUBLISHED,
        )

    @classmethod
    def get_course_hierarchy(cls, slug: str) -> Course:
        """
        Returns a published course with all
        published modules and published topics.
        """

        module_queryset = (
            Module.objects.filter(
                status=Module.Status.PUBLISHED,
            )
            .order_by("order")
            .prefetch_related(
                Prefetch(
                    "topics",
                    queryset=Topic.objects.filter(
                        status=Topic.Status.PUBLISHED,
                    ).order_by("order"),
                )
            )
        )

        return get_object_or_404(
            Course.objects.prefetch_related(
                Prefetch(
                    "modules",
                    queryset=module_queryset,
                )
            ),
            slug=slug,
            status=Course.Status.PUBLISHED,
        )