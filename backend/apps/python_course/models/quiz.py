from django.db import models

from .lesson import Lesson


class Quiz(models.Model):
    lesson = models.OneToOneField(
        Lesson,
        on_delete=models.CASCADE,
        related_name="quiz",
    )

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    passing_score = models.PositiveSmallIntegerField(default=70)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "lesson_quizzes"

    def __str__(self):
        return self.title