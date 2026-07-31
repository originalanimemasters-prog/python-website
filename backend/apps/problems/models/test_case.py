from django.db import models

from apps.core.models.base import BaseModel
from apps.problems.models.interview_question import InterviewQuestion
from apps.problems.models.practice_question import PracticeQuestion


class BaseTestCase(BaseModel):
    input_data = models.TextField()

    expected_output = models.TextField()

    is_hidden = models.BooleanField(
        default=True,
        help_text="Hidden test cases are used for grading but not shown to the user.",
    )

    order = models.PositiveIntegerField(
        default=1,
        help_text="Execution/display order of this test case.",
    )

    class Meta:
        abstract = True
        ordering = ["order"]

    def __str__(self):
        return f"Test Case {self.order}"


class PracticeTestCase(BaseTestCase):
    question = models.ForeignKey(
        PracticeQuestion,
        on_delete=models.CASCADE,
        related_name="test_cases",
    )

    class Meta(BaseTestCase.Meta):
        verbose_name = "Practice Test Case"
        verbose_name_plural = "Practice Test Cases"
        constraints = [
            models.UniqueConstraint(
                fields=["question", "order"],
                name="unique_practice_test_case_order",
            ),
        ]


class InterviewTestCase(BaseTestCase):
    question = models.ForeignKey(
        InterviewQuestion,
        on_delete=models.CASCADE,
        related_name="test_cases",
    )

    class Meta(BaseTestCase.Meta):
        verbose_name = "Interview Test Case"
        verbose_name_plural = "Interview Test Cases"
        constraints = [
            models.UniqueConstraint(
                fields=["question", "order"],
                name="unique_interview_test_case_order",
            ),
        ]