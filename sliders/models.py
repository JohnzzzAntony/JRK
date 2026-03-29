from django.db import models

class HeroSlider(models.Model):
    # Support for both image and video
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="sliders/", null=True, blank=True, help_text="Used for static slider background")
    video = models.FileField(upload_to="sliders/videos/", null=True, blank=True, help_text="Optional, for video backgrounds")
    button_text = models.CharField(max_length=100, default="Enquire Now")
    button_link = models.CharField(max_length=255, default="/contact-us/")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Hero Sliders"
