from django.contrib import admin

from apps.python_course.models import (
    Challenge,
    ContentBlock,
    Course,
    Lesson,
    Module,
    Quiz,
    QuizOption,
    QuizQuestion,
    Topic,
)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "is_free",
        "created_at",
    )

    list_display_links = (
        "title",
    )

    search_fields = (
        "title",
        "slug",
    )

    list_filter = (
        "status",
        "is_free",
    )

    ordering = (
        "title",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
    prepopulated_fields = {
        "slug": ("title",)
    }

    save_on_top = True

    date_hierarchy = "created_at"

    list_per_page = 50


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "module",
        "status",
        "order",
        "created_at",
    )

    list_display_links = (
        "title",
    )

    list_select_related = (
        "module",
    )

    search_fields = (
        "title",
        "slug",
        "module__title",
    )

    list_filter = (
        "module",
        "status",
    )

    ordering = (
        "module",
        "order",
    )

    autocomplete_fields = (
        "module",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    save_on_top = True

    date_hierarchy = "created_at"

    list_per_page = 50

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "course",
        "status",
        "order",
        "created_at",
    )

    list_display_links = (
        "title",
    )

    list_select_related = (
        "course",
    )

    search_fields = (
        "title",
        "slug",
        "course__title",
    )

    list_filter = (
        "course",
        "status",
    )

    ordering = (
        "course",
        "order",
    )

    autocomplete_fields = (
        "course",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    save_on_top = True

    date_hierarchy = "created_at"

    list_per_page = 50
    
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "topic",
        "status",
        "is_free",
        "order",
        "created_at",
    )

    list_display_links = (
        "title",
    )

    list_select_related = (
        "topic",
    )

    search_fields = (
        "title",
        "slug",
        "topic__title",
    )

    list_filter = (
        "status",
        "is_free",
        "topic__module__course",
        "topic__module",
        "topic",
    )

    ordering = (
        "topic",
        "order",
    )

    autocomplete_fields = (
        "topic",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    save_on_top = True

    date_hierarchy = "created_at"

    list_per_page = 50

@admin.register(ContentBlock)
class ContentBlockAdmin(admin.ModelAdmin):
    list_display = (
        "lesson",
        "block_type",
        "order",
        "created_at",
    )

    list_display_links = (
        "lesson",
    )

    list_select_related = (
        "lesson",
    )

    search_fields = (
        "lesson__title",
        "title",
    )

    list_filter = (
        "block_type",
        "lesson__topic__module__course",
    )

    ordering = (
        "lesson",
        "order",
    )

    autocomplete_fields = (
        "lesson",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    save_on_top = True

    date_hierarchy = "created_at"

    list_per_page = 50
    
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "lesson",
        "passing_score",
        "is_active",
        "created_at",
    )

    list_display_links = (
        "title",
    )

    list_select_related = (
        "lesson",
    )

    search_fields = (
        "title",
        "lesson__title",
    )

    list_filter = (
        "is_active",
        "lesson__topic__module__course",
    )

    ordering = (
        "lesson",
    )

    autocomplete_fields = (
        "lesson",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    save_on_top = True

    date_hierarchy = "created_at"

    list_per_page = 50

@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = (
        "quiz",
        "order",
        "created_at",
    )

    list_display_links = (
        "quiz",
    )

    list_select_related = (
        "quiz",
    )

    search_fields = (
        "question",
        "quiz__title",
    )

    list_filter = (
        "quiz__lesson__topic__module__course",
    )

    ordering = (
        "quiz",
        "order",
    )

    autocomplete_fields = (
        "quiz",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    save_on_top = True

    date_hierarchy = "created_at"

    list_per_page = 50
    
@admin.register(QuizOption)
class QuizOptionAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "option_text",
        "is_correct",
    )

    list_display_links = (
        "option_text",
    )

    list_select_related = (
        "question",
    )

    search_fields = (
        "option_text",
        "question__question",
        "question__quiz__title",
    )

    list_filter = (
        "is_correct",
        "question__quiz__lesson__topic__module__course",
    )

    ordering = (
        "question",
        "id",
    )

    autocomplete_fields = (
        "question",
    )


    save_on_top = True

    list_per_page = 50

@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "lesson",
        "difficulty",
        "is_active",
        "created_at",
    )

    list_display_links = (
        "title",
    )

    list_select_related = (
        "lesson",
    )

    search_fields = (
        "title",
        "lesson__title",
    )

    list_filter = (
        "difficulty",
        "is_active",
        "lesson__topic__module__course",
    )

    ordering = (
        "lesson",
    )

    autocomplete_fields = (
        "lesson",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    save_on_top = True

    date_hierarchy = "created_at"

    list_per_page = 50