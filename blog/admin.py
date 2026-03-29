from django.contrib import admin
from .models import Post
from django.utils.html import format_html

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag', 'title', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content', 'excerpt')
    
    fieldsets = (
        ('Header Information', {
            'fields': (('title', 'slug'), 'featured_image', 'is_published')
        }),
        ('Content Information', {
            'fields': ('excerpt', 'content')
        }),
        ('SEO & Google Ranking', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description'),
        }),
    )

    def image_tag(self, obj):
        if obj.featured_image:
            return format_html('<img src="{}" style="width: 60px; height:45px; object-fit: cover; border-radius: 4px;" />', obj.featured_image.url)
        return "-"
    image_tag.short_description = 'Preview'
