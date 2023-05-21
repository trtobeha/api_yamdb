from django.db import models
from django.contrib.auth.models import AbstractUser

ROLES_LIST = models.TextChoices('user', 'moderator', 'admin')


class User(AbstractUser):
    username = models.CharField(
        unique=True,
        blank=False,
        null=False,
        max_length=150,
        required=True,
    )
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
        max_length=254,
        required=True,
    )
    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=150,
    )
    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=150,
    )
    bio = models.CharField(
        max_length=300,
        blank=True,
    )
    role = models.CharField(choices=ROLES_LIST.choices, default='user')
    confirmation_code = models.CharField(
        unique=True,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['username']
        default_related_name = 'users'
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self) -> str:
        pass
