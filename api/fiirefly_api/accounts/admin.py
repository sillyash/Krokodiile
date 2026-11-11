from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import Profile

User = get_user_model()


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


admin.site.unregister(User)


@admin.register(User)
class AriseUserAdmin(UserAdmin):
    inlines = [ProfileInline]
    list_display = ['username', 'profile__nickname', 'is_staff']
    search_fields = ['username', 'profile__nickname']
