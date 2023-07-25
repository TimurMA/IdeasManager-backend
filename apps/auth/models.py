from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class RoleType(models.TextChoices):
        expert = 'expert'
        admin = 'admin'
        initializer = 'initializer'
        projectOffice = 'projectOffice'

    role = models.CharField(max_length=13, choices=RoleType.choices, default = 'initializer', verbose_name='Роль')

    groups = None
    user_permissions = None


