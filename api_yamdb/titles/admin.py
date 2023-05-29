from django.contrib import admin

from titles.models import Category, Genre, Title

admin.site.register(Title)
admin.site.register(Category)
admin.site.register(Genre)


class TitleAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'


class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'


class GenreAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
