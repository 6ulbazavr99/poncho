from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import gettext_lazy as _

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(_('Электронная почта'), unique=True)
    first_name = models.CharField(_('Имя'), max_length=255, null=True, blank=True)
    last_name = models.CharField(_('Фамилия'), max_length=255, null=True, blank=True)
    birthdate = models.DateField(_('Дата рождения'), null=True, blank=True)
    avatar = models.ImageField(_('Аватар'), upload_to='avatars', blank=True, default='avatars/default_avatar.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.username}'
