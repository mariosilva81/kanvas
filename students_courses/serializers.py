from rest_framework.serializers import ModelSerializer, UUIDField, CharField, EmailField
from .models import StudentCourse


class StudentCourseSerializer(ModelSerializer):
    student_id = UUIDField(read_only=True, source="student.id")
    student_username = CharField(read_only=True, source="student.username")
    student_email = EmailField(source="student.email")

    class Meta:
        model = StudentCourse
        fields = ["id", "student_id", "student_username", "student_email", "status"]
