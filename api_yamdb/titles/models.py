from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, db_index=True)

    class Meta:
        verbose_name = 'категория'
        ordering = ('name',)

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
        ordering = ('name',)

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

    class Meta:
        verbose_name = 'произведение и жанр'

    def __str__(self):
        return f'{self.title}, жанр - {self.genre}'
