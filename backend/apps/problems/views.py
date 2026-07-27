from rest_framework import generics
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from .models import Problem
from .serializers import (
    ProblemDetailSerializer,
    ProblemListSerializer,
)

class ProblemPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class ProblemListAPIView(generics.ListAPIView):
    serializer_class = ProblemListSerializer
    permission_classes = [AllowAny]

    pagination_class = ProblemPagination

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "difficulty",
        "is_premium",
    ]

    search_fields = [
        "title",
        "description",
    ]

    ordering_fields = [
        "created_at",
        "title",
    ]

    ordering = [
        "-created_at",
    ]

    queryset = (
        Problem.objects.filter(is_published=True)
        .prefetch_related("tags")
        .order_by("-created_at")
    )


class ProblemDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProblemDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = "slug"

    queryset = (
        Problem.objects.filter(is_published=True)
        .prefetch_related(
            "tags",
            "companies",
            "examples",
            "starter_codes",
        )
    )