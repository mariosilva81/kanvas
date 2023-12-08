from uuid import uuid4
from django.db.models import (
    Model,
    TextChoices,
    UUIDField,
    CharField,
    DateField,
    ForeignKey,
    SET_NULL,
    ManyToManyField,
)


class CourseStatus(TextChoices):
    NOT_STARTED = "not started"
    IN_PROGRESS = "in progress"
    FINISHED = "finished"


class Course(Model):
    id = UUIDField(default=uuid4, primary_key=True, editable=False)
    name = CharField(max_length=100, unique=True)
    status = CharField(
        max_length=11,
        choices=CourseStatus.choices,
        default=CourseStatus.NOT_STARTED,
    )
    start_date = DateField()
    end_date = DateField()

    instructor = ForeignKey(
        "accounts.Account", on_delete=SET_NULL, related_name="courses", null=True
    )

    students = ManyToManyField(
        "accounts.Account",
        through="students_courses.StudentCourse",
        related_name="my_courses",
    )
