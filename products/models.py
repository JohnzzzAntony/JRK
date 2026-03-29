from django.db import models
from django.utils.text import slugify

from ckeditor.fields import RichTextField

class Category(models.Model):
    parent = models.ForeignKey('self', related_name='subcategories', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='categories/')
    # SEO
    meta_title = models.CharField(max_length=70, blank=True)
    meta_description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.parent.name} > {self.name}" if self.parent else self.name

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    # Detailed Content
    features = models.TextField(help_text="One feature per line", blank=True)
    overview = RichTextField(blank=True, null=True)
    technical_info = RichTextField(blank=True, null=True)
    brochure = models.FileField(upload_to='brochures/', null=True, blank=True)
    
    # Legacy/SEO
    regular_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # SEO Section
    google_seo_keywords = models.CharField(max_length=255, blank=True)
    canonical_url = models.URLField(blank=True)

    def get_discount_amount(self):
        return self.regular_price - self.sale_price if self.regular_price > self.sale_price else 0

    def get_discount_percentage(self):
        if self.regular_price > 0 and self.sale_price < self.regular_price:
            return int(round(((self.regular_price - self.sale_price) / self.regular_price) * 100))
        return 0

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/gallery/')


class ProductSKU(models.Model):
    product = models.ForeignKey(Product, related_name='skus', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, help_text="e.g. Size L / Blue")
    sku_id = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=20, choices=[('pcs', 'Pieces'), ('box', 'Box'), ('set', 'Set')])
    
    # Physical Specs
    weight = models.FloatField(help_text="in kg")
    length = models.FloatField(help_text="in cm")
    width = models.FloatField(help_text="in cm")
    height = models.FloatField(help_text="in cm")
    
    # Logistics
    shipping_charge = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_time = models.CharField(max_length=100, help_text="e.g. 3-5 days")
    shipping_status = models.CharField(max_length=50, choices=[
        ('available', 'In Stock'),
        ('out_of_stock', 'Out of Stock'),
        ('pre_order', 'Pre-Order')
    ])
