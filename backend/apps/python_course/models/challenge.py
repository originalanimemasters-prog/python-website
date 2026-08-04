from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
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

    title = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(3),
        ],
    )
    
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

        verbose_name = "Challenge"
        verbose_name_plural = "Challenges"

    def __str__(self):
        return (
            f"{self.lesson.title} → "
            f"{self.title}"
        )
    
    def clean(self):
        super().clean()

        self.title = self.title.strip()

        if not self.title:
            raise ValidationError(
                {
                    "title": (
                        "Challenge title cannot be empty."
                    )
                }
            )
        self.description = self.description.strip()
        
        if not self.description.strip():
            raise ValidationError(
            {
            "description":
            "Description cannot be empty."
            }
        )
    def save(self, *args, **kwargs):
        self.full_clean()

        super().save(
            *args,
            **kwargs,
        )