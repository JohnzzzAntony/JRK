from django.contrib import admin
from .models import AboutUs, VideoCard, MissionVision, Service, Counter, WhyUsCard, GalleryItem, Partner
from django.utils.html import format_html

class VideoCardInline(admin.TabularInline):
    model = VideoCard
    extra = 1

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    inlines = [VideoCardInline]
    # singleton
    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        return super().has_add_permission(request)

@admin.register(MissionVision)
class MissionVisionAdmin(admin.ModelAdmin):
    list_display = ('section_type', 'title')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'image_tag')
    list_editable = ('order',)
    
    def image_tag(self, obj):
        if obj.icon:
            return format_html('<img src="{}" style="width: 45px; height:45px;" />', obj.icon.url)
        return "-"
    image_tag.short_description = 'Icon'

@admin.register(Counter)
class CounterAdmin(admin.ModelAdmin):
    list_display = ('title', 'value', 'order')
    list_editable = ('value', 'order')

@admin.register(WhyUsCard)
class WhyUsCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)

@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'order', 'image_tag')
    list_editable = ('order', 'category')
    
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 60px; height:45px;" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'website_url', 'order', 'image_tag')
    list_editable = ('website_url', 'order')

    def image_tag(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="height:45px; object-fit:contain; max-width: 120px;" />', obj.logo.url)
        return "-"
    image_tag.short_description = 'Logo'
