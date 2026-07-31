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

    title = models.CharField(max_length=150)
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
        ordering = ["order"]
        unique_together = ("module", "slug")

    def __str__(self):
        return self.title