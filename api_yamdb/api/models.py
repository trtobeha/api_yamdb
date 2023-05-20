from rest_framework_simplejwt.tokens import RefreshToken

from django.db import models


class User(models.Model):
    username = models.CharField(
        unique=True,
        blank=False,
        null=False,
        max_length=150,
        required=True,
        # r'^[\w.@+-]+\Z'
    )
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
        max_length=254,
        required=True,
    )
    first_name = None
    last_name = None
    bio = None
    role = None  # default=user
    is_verified = models.BooleanField(default=False)
    confirmation_code = None

    class Meta:
        pass

    def __str__(self) -> str:
        pass
