from django.contrib import admin
from .models import Category, Product, ProductSKU, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class SKUInline(admin.TabularInline):
    model = ProductSKU
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_active')
    search_fields = ('name', 'google_seo_keywords')
    readonly_fields = ('slug',)
    inlines = [ProductImageInline, SKUInline]
    fieldsets = (
        ('Basic Information', {
            'fields': (('category', 'name'), ('image', 'slug'), 'is_active', 'brochure')
        }),
        ('Detailed Content', {
            'fields': ('features', 'overview', 'technical_info')
        }),
        ('Pricing (Legacy)', {
            'classes': ('collapse',),
            'fields': ('regular_price', 'sale_price')
        }),
        ('SEO & Google Ranking', {
            'classes': ('collapse',),
            'fields': ('google_seo_keywords', 'canonical_url'),
        }),
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug')
    list_filter = ('parent',)
