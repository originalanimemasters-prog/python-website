from django.db import models

from .lesson import Lesson


class Challenge(models.Model):
    class Difficulty(models.TextChoices):
        EASY = "easy", "Easy"
        MEDIUM = "medium", "Medium"
        HARD = "hard", "Hard"

    lesson = models.OneToOneField(
        Lesson,
        on_delete=models.CASCADE,
        related_name="challenge",
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    difficulty = models.CharField(
        max_length=10,
        choices=Difficulty.choices,
        default=Difficulty.EASY,
    )

    starter_code = models.TextField(
        blank=True,
    )

    expected_output = models.TextField(
        blank=True,
    )

    hint = models.TextField(
        blank=True,
    )

    solution = models.TextField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        db_table = "lesson_challenges"

    def __str__(self):
        return self.title