from .course import (
    CourseDetailView,
    CourseListView,
)

from .lesson import (
    LessonDetailView,
)

from .quiz import (
    QuizDetailView,
)

from .challenge import (
    ChallengeDetailView,
)

__all__ = [
    "CourseListView",
    "CourseDetailView",
    "LessonDetailView",
    "QuizDetailView",
    "ChallengeDetailView",
]