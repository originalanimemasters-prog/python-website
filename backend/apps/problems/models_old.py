from django.conf import settings
from django.db import models
from django.utils.text import slugify


class DifficultyChoices(models.TextChoices):
    EASY = "easy", "Easy"
    MEDIUM = "medium", "Medium"
    HARD = "hard", "Hard"


class SourceChoices(models.TextChoices):
    LEETCODE = "leetcode", "LeetCode"
    GEEKSFORGEEKS = "gfg", "GeeksForGeeks"
    CODEFORCES = "codeforces", "Codeforces"
    CODECHEF = "codechef", "CodeChef"
    INTERNAL = "internal", "Internal"


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    class Meta:
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    logo = models.URLField(blank=True)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Companies"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Problem(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=280, unique=True, blank=True)

    difficulty = models.CharField(
        max_length=10,
        choices=DifficultyChoices.choices,
    )

    source = models.CharField(
        max_length=20,
        choices=SourceChoices.choices,
        default=SourceChoices.INTERNAL,
    )

    source_url = models.URLField(blank=True)

    description = models.TextField()

    input_format = models.TextField(blank=True)
    output_format = models.TextField(blank=True)
    constraints = models.TextField(blank=True)

    hints = models.TextField(blank=True)
    editorial = models.TextField(blank=True)

    estimated_time = models.PositiveSmallIntegerField(
        default=30,
    )

    acceptance_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
    )

    frequency = models.PositiveIntegerField(default=0)

    tags = models.ManyToManyField(
        Tag,
        related_name="problems",
        blank=True,
    )

    companies = models.ManyToManyField(
        Company,
        related_name="problems",
        blank=True,
    )

    is_premium = models.BooleanField(default=False)

    ad_unlockable = models.BooleanField(default=True)

    is_published = models.BooleanField(default=False)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="created_problems",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

        indexes = [
            models.Index(fields=["difficulty"]),
            models.Index(fields=["is_published"]),
            models.Index(fields=["is_premium"]),
            models.Index(fields=["slug"]),
            models.Index(
                fields=[
                    "difficulty",
                    "is_published",
                    "is_premium",
                ]
            ),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProblemExample(models.Model):
    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
        related_name="examples",
    )

    input = models.TextField()
    output = models.TextField()
    explanation = models.TextField(blank=True)

    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.problem.title} - Example {self.order}"


class ProblemTestCase(models.Model):
    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
        related_name="test_cases",
    )

    input = models.TextField()
    output = models.TextField()

    is_hidden = models.BooleanField(default=True)

    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.problem.title} - Test {self.order}"


class StarterCode(models.Model):
    class Language(models.TextChoices):
        PYTHON = "python", "Python"
        JAVA = "java", "Java"
        CPP = "cpp", "C++"
        JAVASCRIPT = "javascript", "JavaScript"

    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
        related_name="starter_codes",
    )

    language = models.CharField(
        max_length=20,
        choices=Language.choices,
    )

    code = models.TextField()

    class Meta:
        unique_together = ("problem", "language")

    def __str__(self):
        return f"{self.problem.title} ({self.language})"
    
class UserProblem(models.Model):
    class Status(models.TextChoices):
        NOT_STARTED = "not_started", "Not Started"
        ATTEMPTED = "attempted", "Attempted"
        SOLVED = "solved", "Solved"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_problems",
    )

    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
        related_name="user_progress",
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NOT_STARTED,
    )

    attempts = models.PositiveIntegerField(default=0)

    solved_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    last_attempt_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        unique_together = ("user", "problem")

    def __str__(self):
        return f"{self.user.username} - {self.problem.title}"
    
class Bookmark(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookmarks",
    )

    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
        related_name="bookmarked_by",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "problem")

    def __str__(self):
        return f"{self.user.username} bookmarked {self.problem.title}"
    
class ProblemNote(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="problem_notes",
    )

    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
        related_name="notes",
    )

    note = models.TextField()

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user", "problem")

    def __str__(self):
        return f"{self.user.username} - {self.problem.title}"