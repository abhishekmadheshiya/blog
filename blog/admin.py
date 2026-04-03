from django.contrib import admin
from django.utils.html import format_html

from .models import Post, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_image')

    def profile_image(self, obj):
        if obj.image:
            return format_html("<img src='{}' width='50' style='border-radius:50%%;' />", obj.image.url)
        return "-"
    profile_image.short_description = 'Image'


admin.site.register(Post)