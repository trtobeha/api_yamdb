from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ...


class Category(models.Model):
    ...


class Genre(models.Model):
    ...


class Title(models.Model):
    ...


class Review(models.Model):
    ...


class Comment(models.Model):
    ...
