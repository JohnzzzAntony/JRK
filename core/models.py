from django.db import models

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=255, default="JKR International")
    logo = models.ImageField(upload_to="settings/", null=True, blank=True)
    favicon = models.ImageField(upload_to="settings/", null=True, blank=True)
    
    # Meta
    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)
    
    # Global Contact
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    whatsapp = models.CharField(max_length=50, blank=True, help_text="WhatsApp number with country code")
    
    # Offices
    dubai_address = models.TextField(blank=True, help_text="Dubai office full details")
    abudhabi_address = models.TextField(blank=True, help_text="Abu Dhabi office full details")
    
    # Social links
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    
    # Instagram Section
    instagram_handle = models.CharField(max_length=100, default="@jkrinternational", blank=True)

    def __str__(self):
        return "Global Site Settings"

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

class NavMenuItem(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=255, default="/")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to="testimonials/", null=True, blank=True)
    rating = models.PositiveIntegerField(default=5)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Testimonial from {self.client_name}"

    class Meta:
        ordering = ['order']

class Client(models.Model):
    CATEGORY_CHOICES = (
        ('Public', 'Public Sector'),
        ('Private', 'Private Sector'),
    )
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="clients/")
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='Public')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']

class SocialPost(models.Model):
    """Mock Instagram Feed for 'Go social with us' section."""
    image = models.ImageField(upload_to="social/")
    link = models.URLField(blank=True, help_text="Link to the actual post")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
