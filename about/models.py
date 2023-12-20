from django.db import models

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(upload_to="about_images/", blank=True)