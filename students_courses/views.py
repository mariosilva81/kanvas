from .models import StudentCourse
from courses.models import Course
from accounts.permissions import IsSuperUser
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from drf_spectacular.utils import extend_schema
from accounts.models import Account
from rest_framework.exceptions import ValidationError
from courses.serializers import CourseStudentSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.request import Request


class StudentDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUser]
    queryset = Course.objects.all()
    serializer_class = CourseStudentSerializer
    lookup_url_kwarg = "course_id"

    def perform_update(self, serializer: CourseStudentSerializer) -> Course:
        emails = []
        students_courses = serializer.validated_data.get("students_courses")

        if students_courses:
            student_email = students_courses[0]["student"]["email"]

            try:
                course = Course.objects.get(pk=self.kwargs["course_id"])
                student = Account.objects.get(email=student_email)
                StudentCourse.objects.create(course=course, student=student)
                course.students.add(student)
            except Account.DoesNotExist:
                emails.append(student_email)

        if emails:
            emails = ",".join(emails)
            raise ValidationError(
                {"detail": f"No active accounts was found: {emails}."}
            )

    @extend_schema(
        description="Rota para listagem dos estudantes do curso",
        tags=["Listagem e inclusão de estudante em um curso"],
    )
    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        description="Rota para adição de alunos ao curso",
        tags=["Listagem e inclusão de estudante em um curso"],
        parameters=[CourseStudentSerializer],
    )
    def put(self, request: Request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def patch(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def delete(self, request: Request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
