from django.contrib import admin
from .models import SiteSettings, NavMenuItem, Testimonial, Client, SocialPost
from contact.models import NewsletterSubscriber

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name',)
    fieldsets = (
        ('Basic Information', {
            'fields': (('site_name', 'logo'), 'favicon')
        }),
        ('Meta Details', {
            'fields': ('meta_title', 'meta_description')
        }),
        ('Contact Info', {
            'fields': ('email', 'phone', 'whatsapp')
        }),
        ('Office Addresses', {
            'fields': ('dubai_address', 'abudhabi_address')
        }),
        ('Social Links', {
            'fields': ('facebook', 'instagram', 'linkedin', 'twitter', 'instagram_handle')
        }),
    )

@admin.register(NavMenuItem)
class NavMenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'order', 'is_active')
    list_editable = ('order', 'is_active')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'position', 'rating', 'is_active', 'order')
    list_editable = ('is_active', 'order')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_active', 'order')
    list_editable = ('category', 'is_active', 'order')
    list_filter = ('category', 'is_active')

@admin.register(SocialPost)
class SocialPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'order')
    list_editable = ('order',)
