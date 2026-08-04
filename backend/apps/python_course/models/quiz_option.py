from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from .quiz_question import QuizQuestion


class QuizOption(models.Model):
    question = models.ForeignKey(
        QuizQuestion,
        on_delete=models.CASCADE,
        related_name="options",
    )

    option_text = models.CharField(
        max_length=300,
        validators=[
            MinLengthValidator(1),
        ],
    )

    is_correct = models.BooleanField(default=False)

    class Meta:
        db_table = "quiz_options"

        verbose_name = "Quiz Option"
        verbose_name_plural = "Quiz Options"

    def __str__(self):
        return (
            f"Q{self.question.order} → "
            f"{self.option_text}"
        )
    def clean(self):
        super().clean()

        self.option_text = self.option_text.strip()

        if not self.option_text:
            raise ValidationError(
                {
                    "option_text": (
                        "Option text cannot be empty."
                    )
                }
            )
            
    def save(self, *args, **kwargs):
        self.full_clean()

        super().save(
            *args,
            **kwargs,
        )