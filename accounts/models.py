from django.db.models import UUIDField, EmailField
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


class Account(AbstractUser):
    id = UUIDField(default=uuid4, primary_key=True, editable=False)
    email = EmailField(max_length=100, unique=True)
