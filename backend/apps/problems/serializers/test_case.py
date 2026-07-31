from rest_framework import serializers

from apps.problems.models import PracticeTestCase, InterviewTestCase


class BaseTestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "input_data",
            "expected_output",
            "order",
        )
        read_only_fields = (
            "id",
        )


class PracticeTestCaseSerializer(BaseTestCaseSerializer):
    class Meta(BaseTestCaseSerializer.Meta):
        model = PracticeTestCase


class InterviewTestCaseSerializer(BaseTestCaseSerializer):
    class Meta(BaseTestCaseSerializer.Meta):
        model = InterviewTestCase