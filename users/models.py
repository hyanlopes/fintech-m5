import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from cpf_field.models import CPFField


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # created_at = models.DateTimeField(auto_now_create=True)
    cpf = CPFField("cpf")
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ["birth_date", "first_name", "last_name", "email"]


# Create your models here.
