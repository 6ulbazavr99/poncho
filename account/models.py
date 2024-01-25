from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.db import models


from django.utils.translation import gettext_lazy as _

# from product.models import Category


class CustomUser(AbstractUser):
    email = models.EmailField(_('Электронная почта'), unique=True)
    first_name = models.CharField(_('Имя'), max_length=255, null=True, blank=True)
    last_name = models.CharField(_('Фамилия'), max_length=255, null=True, blank=True)
    birthdate = models.DateField(_('Дата рождения'), null=True, blank=True)
    avatar = models.ImageField(_('Аватар'), upload_to='avatars', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # phone?

    def __str__(self):
        return f'{self.username}'


class Vendor(models.Model):
    name = models.CharField(_('Имя'), max_length=255, unique=True)
    description = models.TextField(_('Описание'), null=True, blank=True)
    avatar = models.ImageField(_('Аватар'), upload_to='avatars', blank=True, null=True)
    specifications = RichTextField(blank=True, null=True)
    members = models.ManyToManyField(CustomUser, related_name='vendors_members', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    head = models.ForeignKey(CustomUser, related_name='vendors_head', blank=True, null=True, on_delete=models.SET_NULL)
    # categories = models.ManyToManyField(Category, related_name='vendors', blank=True)

    def __str__(self):
        return self.name
