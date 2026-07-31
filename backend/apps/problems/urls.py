from django.urls import path

from .views import (
    PracticeQuestionListAPIView,
    PracticeQuestionDetailAPIView,
    InterviewQuestionListAPIView,
    InterviewQuestionDetailAPIView,
)

app_name = "problems"

urlpatterns = [
    path("practice/", PracticeQuestionListAPIView.as_view(), name="practice-list"),
    path(
        "practice/<slug:slug>/",
        PracticeQuestionDetailAPIView.as_view(),
        name="practice-detail",
    ),
    path("interview/", InterviewQuestionListAPIView.as_view(), name="interview-list"),
    path(
        "interview/<slug:slug>/",
        InterviewQuestionDetailAPIView.as_view(),
        name="interview-detail",
    ),
]