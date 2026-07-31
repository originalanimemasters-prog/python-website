from django.db.models import Prefetch
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from apps.problems.models import (
    PracticeQuestion,
    PracticeTestCase,
)
from apps.problems.serializers.practice_question import PracticeQuestionSerializer


practice_queryset = (
    PracticeQuestion.objects.filter(is_active=True)
    .select_related("topic")
    .prefetch_related(
        "tags",
        "examples",
        "hints",
        "solutions",
        Prefetch(
            "test_cases",
            queryset=PracticeTestCase.objects.filter(is_hidden=False),
        ),
    )
)


class PracticeQuestionListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PracticeQuestionSerializer
    queryset = practice_queryset.order_by("id")


class PracticeQuestionDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = PracticeQuestionSerializer
    lookup_field = "slug"
    queryset = practice_queryset