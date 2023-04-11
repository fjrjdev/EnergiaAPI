from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.core.validators import MinLengthValidator


class Partner(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField(max_length=200, unique=True, error_messages={"unique": "A user with that name already exists."})
    cnpj = models.CharField(validators=[MinLengthValidator(8)], unique=True, error_messages={"unique": "A user with that cpnj already exists."})
    email = models.EmailField(
        max_length=254,
        unique=True,
        error_messages={"unique": "A user with this email already exists."},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

