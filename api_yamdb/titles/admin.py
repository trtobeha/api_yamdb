from django.contrib import admin

from titles.models import Category, Genre, Title

admin.site.register(Title)
admin.site.register(Category)
admin.site.register(Genre)


class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'year',
        'category',
        'genre',
    )
    list_editable = (
        'category',
        'genre',
    )
    empty_value_display = '-пусто-'


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    list_editable = (
        'name',
        'slug',
    )
    empty_value_display = '-пусто-'


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    list_editable = (
        'name',
        'slug',
    )
    empty_value_display = '-пусто-'
