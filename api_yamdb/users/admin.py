from django.contrib import admin

from users.models import User

admin.site.register(User)


class UsersAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
