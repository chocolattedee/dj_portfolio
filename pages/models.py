from django.db import models

# Create your models here.


class Home(models.Model):
    title = models.CharField(max_length=100)
    text_content = models.TextField()
    image = models.FileField(upload_to='home_images/', blank=True)
