from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from .course import Course



class Module(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="modules",
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
        db_table = "course_modules"

        ordering = ["course", "order"]

        verbose_name = "Module"
        verbose_name_plural = "Modules"

        constraints = [
            models.UniqueConstraint(
                fields=["course", "slug"],
                name="unique_module_slug_per_course",
            ),
            models.UniqueConstraint(
                fields=["course", "order"],
                name="unique_module_order_per_course",
            ),
        ]

    def __str__(self):
        return f"{self.course.title} → {self.title}"

    def clean(self):
        super().clean()

        self.title = self.title.strip()

        if not self.title:
            raise ValidationError(
                {"title": "Module title cannot be empty."}
            )


    def save(self, *args, **kwargs):
        self.full_clean()

        super().save(
            *args,
            **kwargs,
        )