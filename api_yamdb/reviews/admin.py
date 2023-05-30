from django.contrib import admin

from reviews.models import Comment, Review

admin.site.register(Review)
admin.site.register(Comment)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'pub_date',
        'text',
        'author',
        'score',
    )
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'pub_date',
        'text',
        'author',
    )
    empty_value_display = '-пусто-'
