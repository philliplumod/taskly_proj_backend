from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("profile_id", "user", "image")
    readonly_fields = ["profile_id"]


admin.site.register(Profile, ProfileAdmin)
