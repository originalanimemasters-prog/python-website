from django.db import models

from .quiz import Quiz


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name="questions",
    )

    question = models.TextField()

    explanation = models.TextField(blank=True)

    order = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = "quiz_questions"
        ordering = ["order"]

    def __str__(self):
        return self.question