from uuid import uuid4
from django.db.models import (
    TextChoices,
    Model,
    UUIDField,
    CharField,
    ForeignKey,
    CASCADE,
)


class StudentCourseStatus(TextChoices):
    PENDING = "pending"
    ACCEPTED = "accepted"


class StudentCourse(Model):
    id = UUIDField(default=uuid4, primary_key=True, editable=False)
    status = CharField(
        max_length=10,
        choices=StudentCourseStatus.choices,
        default=StudentCourseStatus.PENDING,
    )

    student = ForeignKey(
        "accounts.Account",
        on_delete=CASCADE,
        related_name="students_courses",
    )

    course = ForeignKey(
        "courses.Course",
        on_delete=CASCADE,
        related_name="students_courses",
    )
