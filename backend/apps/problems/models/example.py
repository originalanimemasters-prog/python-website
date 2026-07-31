from django.db import models

from apps.core.models.base import BaseModel
from apps.problems.models.interview_question import InterviewQuestion
from apps.problems.models.practice_question import PracticeQuestion


class BaseExample(BaseModel):
    input_data = models.TextField()

    output_data = models.TextField()

    explanation = models.TextField(
        blank=True,
    )

    order = models.PositiveIntegerField(
        default=1,
        help_text="Display order of this example on the question page.",
    )

    class Meta:
        abstract = True
        ordering = ["order"]

    def __str__(self):
        return f"Example {self.order}"


class PracticeExample(BaseExample):
    question = models.ForeignKey(
        PracticeQuestion,
        on_delete=models.CASCADE,
        related_name="examples",
    )

    class Meta(BaseExample.Meta):
        verbose_name = "Practice Example"
        verbose_name_plural = "Practice Examples"
        constraints = [
            models.UniqueConstraint(
                fields=["question", "order"],
                name="unique_practice_example_order",
            ),
        ]


class InterviewExample(BaseExample):
    question = models.ForeignKey(
        InterviewQuestion,
        on_delete=models.CASCADE,
        related_name="examples",
    )

    class Meta(BaseExample.Meta):
        verbose_name = "Interview Example"
        verbose_name_plural = "Interview Examples"
        constraints = [
            models.UniqueConstraint(
                fields=["question", "order"],
                name="unique_interview_example_order",
            ),
        ]