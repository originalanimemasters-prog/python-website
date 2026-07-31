from django.db import models

from .lesson import Lesson


class ContentBlock(models.Model):
    class BlockType(models.TextChoices):
        TEXT = "text", "Text"
        CODE = "code", "Code"
        IMAGE = "image", "Image"
        NOTE = "note", "Note"
        TIP = "tip", "Tip"
        WARNING = "warning", "Warning"
        QUIZ = "quiz", "Quiz"
        CHALLENGE = "challenge", "Challenge"
        SUMMARY = "summary", "Summary"

    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="content_blocks",
    )

    block_type = models.CharField(
        max_length=20,
        choices=BlockType.choices,
    )

    title = models.CharField(
        max_length=200,
        blank=True,
    )

    markdown = models.TextField(
        blank=True,
    )

    image = models.ImageField(
        upload_to="lesson_blocks/images/",
        blank=True,
        null=True,
    )

    order = models.PositiveIntegerField(
        default=1,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        db_table = "lesson_content_blocks"
        ordering = ["order"]

    def __str__(self):
        return f"{self.lesson.title} - {self.get_block_type_display()}"