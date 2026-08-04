from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from .module import Module


class Topic(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"

    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name="topics",
    )

    title = models.CharField(
        max_length=150,
        validators=[
            MinLengthValidator(3),
        ],
    )
    
    slug = models.SlugField(max_length=170)

    description = models.TextField(blank=True)

    order = models.PositiveIntegerField(default=1)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "course_topics"

        ordering = ["module", "order"]

        verbose_name = "Topic"
        verbose_name_plural = "Topics"

        constraints = [
            models.UniqueConstraint(
                fields=["module", "slug"],
                name="unique_topic_slug_per_module",
            ),
            models.UniqueConstraint(
                fields=["module", "order"],
                name="unique_topic_order_per_module",
            ),
        ]

    def __str__(self):
        return f"{self.module.title} → {self.title}"
    
    def clean(self):
        super().clean()

        self.title = self.title.strip()

        if not self.title:
            raise ValidationError(
                {
                "title": "Topic title cannot be empty."
                }
            )
            
    def save(self, *args, **kwargs):
        self.full_clean()

        super().save(
            *args,
            **kwargs,
        )