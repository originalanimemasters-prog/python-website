from django.contrib import admin

from apps.python_course.models.topic import Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "module",
        "status",
        "order",
        "created_at",
    )
    search_fields = (
        "title",
        "slug",
    )
    list_filter = (
        "module",
        "status",
    )
    ordering = (
        "module",
        "order",
    )
    prepopulated_fields = {
        "slug": ("title",)
    }
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    list_per_page = 50