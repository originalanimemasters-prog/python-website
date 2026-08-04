from django.db.models import Prefetch
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied

from apps.python_course.models import (
    Quiz,
    QuizQuestion,
)
from apps.python_course.services.lesson import LessonService


class QuizService:
    """
    Handles all quiz-related operations.
    """

    @classmethod
    def get_quiz(
        cls,
        user,
        lesson,
    ) -> Quiz:
        """
        Returns the active quiz for a lesson.
        """

        if not LessonService.can_access_lesson(
            user,
            lesson,
        ):
            raise PermissionDenied(
                "Subscription required to access this quiz."
            )

        return get_object_or_404(
            Quiz.objects.prefetch_related(
                Prefetch(
                    "questions",
                    queryset=QuizQuestion.objects.prefetch_related(
                        "options",
                    ).order_by("order"),
                )
            ),
            lesson=lesson,
            is_active=True,
        )

    @classmethod
    def calculate_score(
        cls,
        quiz: Quiz,
        answers: dict[int, int],
    ) -> int:
        """
        Calculates the user's quiz score.

        answers format:

        {
            question_id: option_id
        }
        """

        questions = list(
            quiz.questions.all()
        )

        total_questions = len(
            questions
        )

        if total_questions == 0:
            return 0

        correct_answers = 0

        for question in questions:

            selected_option = answers.get(
                question.id
            )

            if selected_option is None:
                continue

            # Make sure the selected option
            # belongs to this question.
            if selected_option not in {
                option.id
                for option in question.options.all()
            }:
                continue

            # Check if the selected option
            # is the correct answer.
            if any(
                option.id == selected_option
                and option.is_correct
                for option in question.options.all()
            ):
                correct_answers += 1

        return round(
            (
                correct_answers
                / total_questions
            )
            * 100
        )

    @classmethod
    def passed(
        cls,
        quiz: Quiz,
        score: int,
    ) -> bool:
        """
        Returns whether the user
        passed the quiz.
        """

        return (
            score
            >= quiz.passing_score
        )