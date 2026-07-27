from django.urls import path

from .views import (
    ProblemDetailAPIView,
    ProblemListAPIView,
)

urlpatterns = [
    path(
        "",
        ProblemListAPIView.as_view(),
        name="problem-list",
    ),
    path(
        "<slug:slug>/",
        ProblemDetailAPIView.as_view(),
        name="problem-detail",
    ),
]