from django.db import models
from django.conf import settings
from products.models import Product

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_status = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    sku = models.ForeignKey('products.ProductSKU', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

# New Model for Image 3 Quote Enquiry
class QuoteEnquiry(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=50)
    comment = models.TextField(blank=True)
    
    status = models.CharField(max_length=20, default='New', choices=(
        ('New', 'New'),
        ('Processing', 'Processing'),
        ('Quoted', 'Quoted'),
        ('Closed', 'Closed'),
    ))
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Enquiry from {self.first_name} {self.last_name} - {self.created_at.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name = "Quote Enquiry"
        verbose_name_plural = "Quote Enquiries"

class QuoteItem(models.Model):
    enquiry = models.ForeignKey(QuoteEnquiry, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
