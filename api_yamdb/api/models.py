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
    )
    role = None  # default=user
    confirmation_code = None

    class Meta:
        pass

    def __str__(self) -> str:
        pass
