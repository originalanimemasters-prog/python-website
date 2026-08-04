from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models



class Course(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"

    title = models.CharField(
        max_length=100,
        unique=True,
        validators=[
            MinLengthValidator(3),
        ],
    )
    slug = models.SlugField(max_length=120, unique=True)
    description = models.TextField(blank=True)

    thumbnail = models.ImageField(
        upload_to="courses/thumbnails/",
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    is_free = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "courses"
        ordering = ["title"]
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.title
    
    def clean(self):
        super().clean()

        self.title = self.title.strip()

        if not self.title:
            raise ValidationError(
                {"title": "Course title cannot be empty."}
            )
            
            
    def save(self, *args, **kwargs):
        self.full_clean()

        super().save(
            *args,
            **kwargs,
        )