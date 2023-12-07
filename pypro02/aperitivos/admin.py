from django.contrib.admin import ModelAdmin, register
from pypro02.aperitivos.models import Video


@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ('titulo', 'slug', 'creation', 'vimeo_id')
    ordering = ('creation',)
    prepopulated_fields = {'slug': ('titulo',)}
