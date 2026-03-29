from django.contrib import admin
from .models import Order, OrderItem, QuoteEnquiry, QuoteItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    inlines = [OrderItemInline]

# New Admin Registration for Image 3 Quote Enquiry
class QuoteItemInline(admin.TabularInline):
    model = QuoteItem
    extra = 0
    readonly_fields = ('product', 'quantity')

@admin.register(QuoteEnquiry)
class QuoteEnquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'country', 'city', 'status', 'created_at')
    list_filter = ('status', 'country', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    inlines = [QuoteItemInline]
    readonly_fields = ('first_name', 'last_name', 'email', 'department', 'country', 'city', 'street', 'phone', 'comment', 'created_at')
    
    fieldsets = (
        ('Personal Information', {
            'fields': (('first_name', 'last_name'), ('email', 'phone'), 'department')
        }),
        ('Location Information', {
            'fields': ('country', 'city', 'street')
        }),
        ('Enquiry Details', {
            'fields': ('comment', 'status', 'created_at')
        }),
    )
