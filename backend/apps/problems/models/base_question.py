from django.db import models

from apps.core.models.base import BaseModel
from apps.python_course.models.topic import Topic


class BaseQuestion(BaseModel):
    class Difficulty(models.TextChoices):
        EASY = "easy", "Easy"
        MEDIUM = "medium", "Medium"
        HARD = "hard", "Hard"

    title = models.CharField(
        max_length=255,
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
    )

    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="%(class)ss",
    )

    problem_statement = models.TextField()

    input_format = models.TextField(
        blank=True,
    )

    output_format = models.TextField(
        blank=True,
    )

    constraints = models.TextField(
        blank=True,
    )

    difficulty = models.CharField(
        max_length=10,
        choices=Difficulty.choices,
    )

    editorial = models.TextField(
        blank=True,
        help_text="Detailed explanation of the approach.",
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.title