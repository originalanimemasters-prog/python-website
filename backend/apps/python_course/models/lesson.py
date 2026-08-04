from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from .topic import Topic


class Lesson(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"

    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="lessons",
    )

    title = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(3),
        ],
    )
    slug = models.SlugField(max_length=220)

    short_description = models.TextField(blank=True)

    order = models.PositiveIntegerField(default=1)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    is_free = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "course_lessons"

        ordering = ["topic", "order"]

        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"

        constraints = [
            models.UniqueConstraint(
                fields=["topic", "slug"],
                name="unique_lesson_slug_per_topic",
            ),
            models.UniqueConstraint(
                fields=["topic", "order"],
                name="unique_lesson_order_per_topic",
            ),
        ]

    def __str__(self):
        return f"{self.topic.title} → {self.title}"
    
    def clean(self):
        super().clean()

        self.title = self.title.strip()

        if not self.title:
            raise ValidationError(
                {
                    "title": "Lesson title cannot be empty."
                }
            )
            
    def save(self, *args, **kwargs):
        self.full_clean()

        super().save(
            *args,
            **kwargs,
        )