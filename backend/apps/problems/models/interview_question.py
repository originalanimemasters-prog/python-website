from django.db import models

from apps.problems.models.base_question import BaseQuestion
from apps.problems.models.company import Company
from apps.problems.models.tag import Tag


class InterviewQuestion(BaseQuestion):
    companies = models.ManyToManyField(
        Company,
        related_name="interview_questions",
    )

    tags = models.ManyToManyField(
        Tag,
        related_name="interview_questions",
        blank=True,
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Interview Question"
        verbose_name_plural = "Interview Questions"

    def __str__(self):
        return self.title