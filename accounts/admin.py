from django.contrib import admin
from .models import User
from django.utils.html import mark_safe


# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'get_user_avatar']

    def get_date_joined(self):
        pass

    def get_user_avatar(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" height="50" width="50">')
        return 'No Avatar'

    get_user_avatar.short_description = 'Avatar'
