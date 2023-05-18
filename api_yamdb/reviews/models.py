from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ...


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        ordering = ['name']


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        ordering = ['name']


class Title(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    year = models.IntegerField(verbose_name='Дата выхода')
    description = models.TextField(
        verbose_name='Описание',
        max_length=200,
        null=True,
        blank=True
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр'
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Произведение'


class GenreTitle(models.Model):
    title = models.ForeignKey(
        Title,
        verbose_name='Произведение',
        on_delete=models.CASCADE)
    genre = models.ForeignKey(
        Genre,
        verbose_name='Жанр',
        on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, жанр - {self.genre}'

    class Meta:
        verbose_name = 'Произведение и жанр'


class Review(models.Model):
    ...


class Comment(models.Model):
    ...
