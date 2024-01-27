from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from account.models import Vendor


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    preview = models.ImageField(upload_to='previews', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')


class Product(models.Model):
    STATUS_CHOICES = (
        ('in_stock', _('В наличии')),
        ('out_of_stock', _('Нет в наличии'))
    )

    name = models.CharField(max_length=255, unique=True, verbose_name=_('Название'))
    name_plural = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Название во множественном числе'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Описание'))
    specifications = RichTextField(blank=True, null=True, verbose_name=_('Характеристики'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Цена'))
    preview = models.ImageField(upload_to='previews', blank=True, null=True, verbose_name=_('Превью'))
    discount = models.PositiveSmallIntegerField(default=0, blank=True, null=True, verbose_name=_('Скидка'))
    bulk_discount = models.PositiveSmallIntegerField(default=0, blank=True, null=True, verbose_name=_('Массовая скидка'))
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='in_stock', blank=True, null=True, verbose_name=_('Статус'))
    category = models.ManyToManyField(Category, blank=True, related_name='products', verbose_name=_('Категория'))
    owner = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('Владелец'))
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE, verbose_name=_('Производитель'))

    # address =

    def __str__(self):
        return f'{self.name} [{self.vendor}]'

    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')

    def save(self, *args, **kwargs):
        if not self.name_plural:
            self.name_plural = f'{self.name}s\es'
