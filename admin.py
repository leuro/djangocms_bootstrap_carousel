from django.contrib import admin
from models import MediaItem


class MediaItemAdmin(admin.ModelAdmin):
    raw_id_fields = ('image', 'video')
    fieldsets = (
        (None, {
            'fields': ('image', 'video', 'image_url', 'video_url'),
        }),
        ('More', {
            'classes': ('collapse',),
            'fields': ('width', 'height'),
        }),
    )

admin.site.register(MediaItem, MediaItemAdmin)
