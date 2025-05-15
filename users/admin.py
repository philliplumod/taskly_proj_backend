from django.contrib import admin
from .models import Profile, CustomUser
from django.contrib.auth.admin import UserAdmin



class ProfileAdmin(admin.ModelAdmin):
    list_display = ("profile_id", "user", "image")
    readonly_fields = ["profile_id"]


class CustomUserAdmin(UserAdmin):  # extend UserAdmin for built-in user admin features
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'last_login', 'user_id')
    ordering = ('username',)
    search_fields = ('username', 'email')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Important dates', {'fields': ('last_login',)}),
        ('UUID', {'fields': ('user_id',)}),
    )

    readonly_fields = ('user_id',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(CustomUser, CustomUserAdmin)

