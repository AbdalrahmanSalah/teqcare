from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from core.models import User


class UserAdmin(admin.ModelAdmin):
    ordring = ('email',)
    list_display = ['email', 'name']

admin.site.register(User, UserAdmin)
