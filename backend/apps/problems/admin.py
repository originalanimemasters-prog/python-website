from django.contrib import admin

from .models import (
    Company,
    Problem,
    ProblemExample,
    ProblemTestCase,
    StarterCode,
    Tag,
)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


class ProblemExampleInline(admin.TabularInline):
    model = ProblemExample
    extra = 1


class ProblemTestCaseInline(admin.TabularInline):
    model = ProblemTestCase
    extra = 1


class StarterCodeInline(admin.TabularInline):
    model = StarterCode
    extra = 1


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "difficulty",
        "is_premium",
        "is_published",
        "created_at",
    )

    list_filter = (
        "difficulty",
        "is_premium",
        "is_published",
    )

    search_fields = (
        "title",
        "description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    filter_horizontal = (
        "tags",
        "companies",
    )

    inlines = [
        ProblemExampleInline,
        ProblemTestCaseInline,
        StarterCodeInline,
    ]


@admin.register(ProblemExample)
class ProblemExampleAdmin(admin.ModelAdmin):
    list_display = ("id", "problem", "order")


@admin.register(ProblemTestCase)
class ProblemTestCaseAdmin(admin.ModelAdmin):
    list_display = ("id", "problem", "order", "is_hidden")
    list_filter = ("is_hidden",)


@admin.register(StarterCode)
class StarterCodeAdmin(admin.ModelAdmin):
    list_display = ("id", "problem", "language")
    list_filter = ("language",)