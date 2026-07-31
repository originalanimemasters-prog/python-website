from django.db import models

from .quiz_question import QuizQuestion


class QuizOption(models.Model):
    question = models.ForeignKey(
        QuizQuestion,
        on_delete=models.CASCADE,
        related_name="options",
    )

    option_text = models.CharField(max_length=300)

    is_correct = models.BooleanField(default=False)

    class Meta:
        db_table = "quiz_options"

    def __str__(self):
        return self.option_text