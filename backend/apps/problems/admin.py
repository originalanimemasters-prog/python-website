from django.contrib import admin

from apps.problems.models import (
    Company,
    Topic,
    InterviewExample,
    InterviewHint,
    InterviewQuestion,
    InterviewSolution,
    InterviewTestCase,
    PracticeExample,
    PracticeHint,
    PracticeQuestion,
    PracticeSolution,
    PracticeTestCase,
    Tag,
)


# ==========================================================
# Company & Tag
# ==========================================================


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "website", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("name", "website")
    ordering = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("created_at", "updated_at")
    list_per_page = 50


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    search_fields = ("name", "slug")
    ordering = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("created_at", "updated_at")
    list_per_page = 50
    
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "created_at",
    )
    search_fields = (
        "name",
        "slug",
    )
    ordering = ("name",)
    prepopulated_fields = {
        "slug": ("name",)
    }
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    list_per_page = 50


# ==========================================================
# Inlines
# ==========================================================


class BaseExampleInline(admin.TabularInline):
    extra = 0
    ordering = ("order",)


class PracticeExampleInline(BaseExampleInline):
    model = PracticeExample


class InterviewExampleInline(BaseExampleInline):
    model = InterviewExample


class BaseHintInline(admin.TabularInline):
    extra = 0
    ordering = ("order",)


class PracticeHintInline(BaseHintInline):
    model = PracticeHint


class InterviewHintInline(BaseHintInline):
    model = InterviewHint


class BaseSolutionInline(admin.TabularInline):
    extra = 0
    ordering = ("language",)


class PracticeSolutionInline(BaseSolutionInline):
    model = PracticeSolution


class InterviewSolutionInline(BaseSolutionInline):
    model = InterviewSolution


class BaseTestCaseInline(admin.TabularInline):
    extra = 0
    ordering = ("order",)


class PracticeTestCaseInline(BaseTestCaseInline):
    model = PracticeTestCase


class InterviewTestCaseInline(BaseTestCaseInline):
    model = InterviewTestCase


# ==========================================================
# Question Admins
# ==========================================================


class BaseQuestionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "topic",
        "difficulty",
        "is_active",
        "created_at",
    )
    list_filter = (
        "difficulty",
        "is_active",
        "topic",
    )
    search_fields = (
        "title",
        "slug",
        "problem_statement",
    )
    ordering = ("-created_at",)
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at")
    list_select_related = ("topic",)
    date_hierarchy = "created_at"
    list_per_page = 25


@admin.register(PracticeQuestion)
class PracticeQuestionAdmin(BaseQuestionAdmin):
    filter_horizontal = ("tags",)
    inlines = (
        PracticeExampleInline,
        PracticeTestCaseInline,
        PracticeHintInline,
        PracticeSolutionInline,
    )


@admin.register(InterviewQuestion)
class InterviewQuestionAdmin(BaseQuestionAdmin):
    list_filter = BaseQuestionAdmin.list_filter + ("companies",)
    filter_horizontal = (
        "companies",
        "tags",
    )
    inlines = (
        InterviewExampleInline,
        InterviewTestCaseInline,
        InterviewHintInline,
        InterviewSolutionInline,
    )


# ==========================================================
# Base Admins
# ==========================================================


class BaseExampleAdmin(admin.ModelAdmin):
    list_display = ("question", "order")
    search_fields = ("question__title",)
    ordering = ("question", "order")
    readonly_fields = ("created_at", "updated_at")
    autocomplete_fields = ("question",)
    list_per_page = 50


class BaseHintAdmin(admin.ModelAdmin):
    list_display = ("question", "order")
    search_fields = ("question__title",)
    ordering = ("question", "order")
    readonly_fields = ("created_at", "updated_at")
    autocomplete_fields = ("question",)
    list_per_page = 50


class BaseSolutionAdmin(admin.ModelAdmin):
    list_display = ("question", "language")
    list_filter = ("language",)
    search_fields = ("question__title",)
    ordering = ("question", "language")
    readonly_fields = ("created_at", "updated_at")
    autocomplete_fields = ("question",)
    list_per_page = 50


class BaseTestCaseAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "order",
        "is_hidden",
    )
    list_filter = ("is_hidden",)
    search_fields = ("question__title",)
    ordering = ("question", "order")
    readonly_fields = ("created_at", "updated_at")
    autocomplete_fields = ("question",)
    list_per_page = 50


# ==========================================================
# Example Admins
# ==========================================================


@admin.register(PracticeExample)
class PracticeExampleAdmin(BaseExampleAdmin):
    pass


@admin.register(InterviewExample)
class InterviewExampleAdmin(BaseExampleAdmin):
    pass


# ==========================================================
# Hint Admins
# ==========================================================


@admin.register(PracticeHint)
class PracticeHintAdmin(BaseHintAdmin):
    pass


@admin.register(InterviewHint)
class InterviewHintAdmin(BaseHintAdmin):
    pass


# ==========================================================
# Solution Admins
# ==========================================================


@admin.register(PracticeSolution)
class PracticeSolutionAdmin(BaseSolutionAdmin):
    pass


@admin.register(InterviewSolution)
class InterviewSolutionAdmin(BaseSolutionAdmin):
    pass


# ==========================================================
# Test Case Admins
# ==========================================================


@admin.register(PracticeTestCase)
class PracticeTestCaseAdmin(BaseTestCaseAdmin):
    pass


@admin.register(InterviewTestCase)
class InterviewTestCaseAdmin(BaseTestCaseAdmin):
    pass