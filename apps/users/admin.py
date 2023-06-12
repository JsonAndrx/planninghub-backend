from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.users.models import User, Profile
# Register your models here.


class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_client')
    list_filter = ('is_client', 'is_staff', 'created', 'modified')
@admin.register(Profile)
class ProfileAdmi(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('user',)

admin.site.register(User, CustomUserAdmin)