from django.db import models
from PIL import Image



CATEGORY_CHOICES = (
    ('Hırdavat,yapı, ve Nalburiye'),
    ('Deniz Malzemeleri'),
    ('Bahçe'),
    ('otomotiv'),
    ('Ambalaj Malzemeleri'),
    ('Kimyasallar'),


)


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.CharField(max_length=200)
    imagel_1 = models.ImageField(upload_to='product_images', default='default.jpg')
    imagel_2 = models.ImageField(upload_to='product_images', default='default.jpg')
    imagel_3 = models.ImageField(upload_to='product_images', default='default.jpg')

    def __str__(self):
        return self.name