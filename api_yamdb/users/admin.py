from django.contrib import admin

from users.models import User

admin.site.register(User)


class UsersAdmin(admin.ModelAdmin):
    list_display = (
        'role',
        'username',
        'email',
        'first_name',
        'last_name',
    )
    empty_value_display = '-пусто-'
