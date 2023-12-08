from rest_framework.serializers import ModelSerializer
from .models import Course, CourseStatus
from rest_framework import serializers
from students_courses.serializers import StudentCourseSerializer
from contents.serializers import ContentSerializer


class CourseSerializer(ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)
    students_courses = StudentCourseSerializer(many=True, read_only=True)
    status = serializers.ChoiceField(
        choices=CourseStatus.choices, required=False
    )

    class Meta:
        model = Course
        fields = [
            "id",
            "status",
            "name",
            "start_date",
            "end_date",
            "contents",
            "instructor",
            "students_courses",
        ]


class CourseStudentSerializer(ModelSerializer):
    students_courses = StudentCourseSerializer(many=True)
    name = serializers.CharField(read_only=True)

    class Meta:
        model = Course
        fields = ["id", "name", "students_courses"]
