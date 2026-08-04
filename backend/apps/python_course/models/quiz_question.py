from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from .quiz import Quiz


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name="questions",
    )

    question = models.TextField(
        validators=[
            MinLengthValidator(5),
        ],
    )

    explanation = models.TextField(
        blank=True,
    )

    order = models.PositiveIntegerField(
        default=1,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )
    class Meta:
        db_table = "quiz_questions"

        ordering = ["quiz", "order"]

        verbose_name = "Quiz Question"
        verbose_name_plural = "Quiz Questions"

        constraints = [
            models.UniqueConstraint(
                fields=["quiz", "order"],
                name="unique_question_order_per_quiz",
            ),
        ]

    def __str__(self):
        return (
            f"{self.quiz.title} → "
            f"Question {self.order}"
        )

    def clean(self):
        super().clean()

        self.question = self.question.strip()

        if not self.question:
            raise ValidationError(
                {
                    "question": (
                        "Question cannot be empty."
                    )
                }
            )

    def save(self, *args, **kwargs):
        self.full_clean()

        super().save(
            *args,
            **kwargs,
        )