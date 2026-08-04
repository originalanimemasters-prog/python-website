from django.urls import path

from apps.python_course.views import (
    ChallengeDetailView,
    CourseDetailView,
    CourseListView,
    LessonDetailView,
    QuizDetailView,
)

urlpatterns = [
    path(
        "courses/",
        CourseListView.as_view(),
        name="course-list",
    ),
    path(
        "courses/<slug:slug>/",
        CourseDetailView.as_view(),
        name="course-detail",
    ),
    path(
        "lessons/<slug:slug>/",
        LessonDetailView.as_view(),
        name="lesson-detail",
    ),
    path(
        "lessons/<slug:slug>/quiz/",
        QuizDetailView.as_view(),
        name="quiz-detail",
    ),
    path(
        "lessons/<slug:slug>/challenge/",
        ChallengeDetailView.as_view(),
        name="challenge-detail",
    ),
]