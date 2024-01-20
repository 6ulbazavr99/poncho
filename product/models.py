from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    preview = models.ImageField(upload_to='previews', blank=True, null=True, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS_CHOICES = (
        ('in_stock', 'В наличии'),
        ('out_of_stock', 'Нет в наличии')
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    specifications = RichTextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    preview = models.ImageField(upload_to='previews', blank=True)
    discount = models.PositiveSmallIntegerField(default=0)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='in_stock')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    # owner = models.ForeignKey()