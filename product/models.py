from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    preview = models.ImageField(upload_to='previews', blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

