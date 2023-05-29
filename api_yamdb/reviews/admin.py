from django.contrib import admin

from reviews.models import Comment, Review

admin.site.register(Review)
admin.site.register(Comment)


class ReviewAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
