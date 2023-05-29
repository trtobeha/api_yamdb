from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    ROLES = [
        [ADMIN, 'Administrator'],
        [MODERATOR, 'Moderator'],
        [USER, 'User'],
    ]
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        null=False,
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        blank=False,
        null=False,
    )
    first_name = models.CharField(
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
    )
    bio = models.CharField(
        max_length=300,
        blank=True,
    )
    role = models.CharField(
        choices=ROLES,
        default=USER,
        max_length=10,
    )

    class Meta:
        ordering = ('username',)
        default_related_name = 'user'
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    @property
    def is_user(self):
        return self.role == self.USER

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser

    def __str__(self) -> str:
        return self.username
