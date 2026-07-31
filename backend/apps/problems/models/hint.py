from django.db import models

from apps.core.models.base import BaseModel
from apps.problems.models.practice_question import PracticeQuestion
from apps.problems.models.interview_question import InterviewQuestion


class BaseHint(BaseModel):
    content = models.TextField()

    order = models.PositiveIntegerField(
        default=1,
        help_text="Display order of this hint (lower numbers shown first).",
    )

    class Meta:
        abstract = True
        ordering = ["order"]

    def __str__(self):
        return f"Hint #{self.order}"


class PracticeHint(BaseHint):
    question = models.ForeignKey(
        PracticeQuestion,
        on_delete=models.CASCADE,
        related_name="hints",
    )

    class Meta(BaseHint.Meta):
        verbose_name = "Practice Hint"
        verbose_name_plural = "Practice Hints"


class InterviewHint(BaseHint):
    question = models.ForeignKey(
        InterviewQuestion,
        on_delete=models.CASCADE,
        related_name="hints",
    )

    class Meta(BaseHint.Meta):
        verbose_name = "Interview Hint"
        verbose_name_plural = "Interview Hints"