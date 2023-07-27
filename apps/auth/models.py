from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):

    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _("username"),
        max_length=150,
        null=True,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    token = models.CharField(
        unique=True,
        db_index=True,
        null=True,
        blank=True,
        max_length=100,
        verbose_name="Токен",
    )

    email = models.EmailField(unique=True, blank=True, verbose_name='Почта')
    is_registered = models.BooleanField(default=False)
    roles = models.ManyToManyField('Role', related_name='roles', verbose_name='Роли')

    groups = None

    def __str__(self) -> str:
        return self.username

class Role(models.Model):
    class RoleType(models.TextChoices):
        expert = "expert"
        admin = "admin"
        initializer = "initializer"
        projectOffice = "projectOffice"

    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Пользователь')
    role = models.CharField(
        max_length=13,
        choices=RoleType.choices,
        default="admin",
        verbose_name="Роль",
    )