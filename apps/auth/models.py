from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class RoleType(models.TextChoices):
        expert = "expert"
        admin = "admin"
        initializer = "initializer"
        projectOffice = "projectOffice"

    token = models.UUIDField(
        unique=True,
        db_index=True,
        null=True,
        max_length=100,
        verbose_name="Токен",
    )
    role = models.CharField(
        max_length=13,
        choices=RoleType.choices,
        default="initializer",
        verbose_name="Роль",
    )

    groups = None
    user_permissions = None
