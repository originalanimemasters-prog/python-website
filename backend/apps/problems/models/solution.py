from django.db import models

from apps.core.models.base import BaseModel
from apps.problems.models.interview_question import InterviewQuestion
from apps.problems.models.practice_question import PracticeQuestion


class BaseSolution(BaseModel):
    class Language(models.TextChoices):
        PYTHON = "python", "Python"
        JAVA = "java", "Java"
        CPP = "cpp", "C++"
        JAVASCRIPT = "javascript", "JavaScript"

    language = models.CharField(
        max_length=20,
        choices=Language.choices,
    )

    code = models.TextField()

    explanation = models.TextField(
        blank=True,
        help_text="Optional notes specific to this language's implementation.",
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.get_language_display()} Solution"


class PracticeSolution(BaseSolution):
    question = models.ForeignKey(
        PracticeQuestion,
        on_delete=models.CASCADE,
        related_name="solutions",
    )

    class Meta(BaseSolution.Meta):
        verbose_name = "Practice Solution"
        verbose_name_plural = "Practice Solutions"
        constraints = [
            models.UniqueConstraint(
                fields=["question", "language"],
                name="unique_practice_solution_per_language",
            ),
        ]


class InterviewSolution(BaseSolution):
    question = models.ForeignKey(
        InterviewQuestion,
        on_delete=models.CASCADE,
        related_name="solutions",
    )

    class Meta(BaseSolution.Meta):
        verbose_name = "Interview Solution"
        verbose_name_plural = "Interview Solutions"
        constraints = [
            models.UniqueConstraint(
                fields=["question", "language"],
                name="unique_interview_solution_per_language",
            ),
        ]