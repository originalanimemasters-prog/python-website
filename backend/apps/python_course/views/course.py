from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.python_course.serializers import (
    CourseSerializer,
)
from apps.python_course.services import (
    CourseService,
)


class CourseListView(generics.ListAPIView):
    """
    Returns all published courses.
    """

    permission_classes = [
        AllowAny,
    ]

    serializer_class = CourseSerializer

    def get_queryset(self):
        return CourseService.get_courses()


class CourseDetailView(generics.RetrieveAPIView):
    """
    Returns a published course with its
    published modules and topics.
    """

    permission_classes = [
        AllowAny,
    ]

    serializer_class = CourseSerializer
    lookup_field = "slug"

    def get_object(self):
        slug = self.kwargs["slug"]

        return CourseService.get_course_hierarchy(
            slug,
        )