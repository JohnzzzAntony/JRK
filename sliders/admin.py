from django.contrib import admin
from .models import HeroSlider
from django.utils.html import format_html

@admin.register(HeroSlider)
class HeroSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview', 'order', 'is_active', 'button_text')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height:60px;" />', obj.image.url)
        elif obj.video:
            return format_html('<span style="color: blue;">[Video Background]</span>')
        return "-"
    preview.short_description = 'Background Preview'
