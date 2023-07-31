from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slider_images/')

class Navbar(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
