from django.db import models

from apps.problems.models.base_question import BaseQuestion
from apps.problems.models.tag import Tag


class PracticeQuestion(BaseQuestion):
    tags = models.ManyToManyField(
        Tag,
        related_name="practice_questions",
        blank=True,
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Practice Question"
        verbose_name_plural = "Practice Questions"

    def __str__(self):
        return self.title