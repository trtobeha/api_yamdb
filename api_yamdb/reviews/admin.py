from django.contrib import admin

from reviews.models import Comment, Review


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


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
