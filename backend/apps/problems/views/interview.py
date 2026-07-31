from django.db.models import Prefetch
from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.problems.models import (
    InterviewQuestion,
    InterviewTestCase,
)
from apps.problems.serializers.interview_question import (
    InterviewQuestionSerializer,
)


interview_queryset = (
    InterviewQuestion.objects.filter(is_active=True)
    .select_related(
        "topic",
        "company",
    )
    .prefetch_related(
        "tags",
        "examples",
        "hints",
        "solutions",
        Prefetch(
            "test_cases",
            queryset=InterviewTestCase.objects.filter(is_hidden=False),
        ),
    )
)


class InterviewQuestionListAPIView(ListAPIView):
    serializer_class = InterviewQuestionSerializer
    queryset = interview_queryset.order_by("id")


class InterviewQuestionDetailAPIView(RetrieveAPIView):
    serializer_class = InterviewQuestionSerializer
    lookup_field = "slug"
    queryset = interview_queryset