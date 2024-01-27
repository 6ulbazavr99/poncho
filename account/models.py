from uuid import uuid4

from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.db import models


from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(_('Электронная почта'), unique=True)
    first_name = models.CharField(_('Имя'), max_length=255, null=True, blank=True)
    last_name = models.CharField(_('Фамилия'), max_length=255, null=True, blank=True)
    birthdate = models.DateField(_('Дата рождения'), null=True, blank=True)
    avatar = models.ImageField(_('Аватар'), upload_to='avatars', blank=True, null=True)
    nickname = models.CharField(_('Псевдоним'), max_length=255, null=True, blank=True, unique=True)

    # phone =

    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Дата обновления'), auto_now=True)

    is_active = models.BooleanField(
        _("active"),
        default=False,  # "False" for confirmation by email
        help_text=_(
            "Указывает, следует ли считать этого пользователя активным."
            "Снимите этот флажок вместо удаления учетных записей"
        ),
    )
    activation_code = models.CharField(max_length=255, default=_('waiting for confirmation'), null=True, blank=True)

    def __str__(self):
        return f'{self.username}'

    def save(self, *args, **kwargs):
        if not self.nickname:
            self.nickname = self.get_username()
        self.create_activation_code()
        super().save(*args, **kwargs)

    def create_activation_code(self):
        code = str(uuid4())
        self.activation_code = code


class Vendor(models.Model):
    name = models.CharField(_('Имя'), max_length=255, unique=True)
    description = models.TextField(_('Описание'), null=True, blank=True)
    avatar = models.ImageField(_('Аватар'), upload_to='avatars', blank=True, null=True)
    specifications = RichTextField(_('Характеристики'), blank=True, null=True)
    members = models.ManyToManyField(CustomUser, related_name='vendors_members', blank=True, verbose_name=_('Участники'))
    head = models.ForeignKey(CustomUser, related_name='vendors_head', blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('Руководитель'))
    email = models.EmailField(_('Электронная почта'), unique=True, blank=True, null=True)

    # phone =
    # address =

    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Дата обновления'), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Продавец')
        verbose_name_plural = _('Продавцы')
