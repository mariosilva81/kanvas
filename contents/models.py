from uuid import uuid4
from django.db.models import Model, UUIDField, CharField, TextField, ForeignKey, PROTECT


class Content(Model):
    id = UUIDField(default=uuid4, primary_key=True, editable=False)
    name = CharField(max_length=150)
    content = TextField()
    video_url = CharField(max_length=200, null=True)

    course = ForeignKey(
        "courses.Course",
        on_delete=PROTECT,
        related_name="contents",
    )
