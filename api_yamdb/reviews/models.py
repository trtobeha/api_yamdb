from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

ROLES_LIST = (('SR', 'user'), ('MD', 'moderator'), ('AD', 'admin'))


class User(AbstractUser):
    username = models.CharField(
        max_length=150, unique=True, blank=False, null=False
    )
    email = models.EmailField(
        max_length=254, unique=True, blank=False, null=False
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
        choices=ROLES_LIST,
        default='SR',
        max_length=10,
    )
    confirmation_code = models.CharField(
        unique=True,
        blank=False,
        null=False,
        max_length=255,
    )

    class Meta:
        ordering = ['username']
        default_related_name = 'user'
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self) -> str:
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, db_index=True)

    class Meta:
        verbose_name = 'категория'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} {self.name}'


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, db_index=True)

    class Meta:
        verbose_name = 'жанр'

    def __str__(self):
        return f'{self.name} {self.name}'


class Title(models.Model):
    name = models.CharField(verbose_name='название', max_length=200)
    year = models.IntegerField(verbose_name='дата выхода')
    description = models.TextField(
        verbose_name='описание',
        max_length=200,
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        verbose_name='категория',
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True,
        blank=True,
    )
    genre = models.ManyToManyField(Genre, related_name='titles')

    class Meta:
        verbose_name = 'произведение'

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    title = models.ForeignKey(
        Title,
        verbose_name='произведение',
        on_delete=models.CASCADE,
    )
    genre = models.ForeignKey(
        Genre,
        verbose_name='жанр',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.title}, жанр - {self.genre}'

    class Meta:
        verbose_name = 'произведение и жанр'


class Review(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='автор',
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    text = models.CharField(
        max_length=200,
    )
    score = models.IntegerField(
        'оценка',
        validators=(
            MinValueValidator(1),
            MaxValueValidator(10),
        ),
    )
    pub_date = models.DateTimeField(
        'дата публикации',
        auto_now_add=True,
        db_index=True,
    )

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

    def __str__(self):
        return self.text


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.CharField(
        'текст комментария',
        max_length=200,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='автор',
    )
    pub_date = models.DateTimeField(
        'дата публикации',
        auto_now_add=True,
        db_index=True,
    )

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self):
        return self.text
