from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models

from django.utils.translation import gettext_lazy as _

from product.models import Product


User = get_user_model()


class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Стоимость'), blank=True,
                                 null=True, editable=False)

    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Дата обновления'), auto_now=True)

    def save(self, *args, **kwargs):
        if self.amount is None:
            self.calculate_amount()
        super().save(*args, **kwargs)

    def calculate_amount(self):
        amount = self.product.price * self.quantity
        self.amount = amount

    class Meta:
        verbose_name = _('Элемент заказа')
        verbose_name_plural = _('Элементы заказа')

    def __str__(self):
        return f'[{self.product.name}] {self.quantity} шт. -> {self.order}'


class Order(models.Model):

    STATUS_CHOICES = (
        ('open', _('Открыт')),
        ('in_process', _('В обработке')),
        ('closed', _('Закрыт'))
    )

    number = models.CharField(max_length=15, blank=True, null=True, verbose_name=_('Номер'))
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='open',
                              blank=True, null=True, verbose_name=_('Статус'))
    items = models.ManyToManyField(Product, through=OrderItem, related_name='orders')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Стоимость'), blank=True,
                                 null=True, editable=False)

    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Дата обновления'), auto_now=True)

    def __str__(self):
        return f'{self.number} [{str(self.owner)}]'

    def save(self, *args, **kwargs):
        self.generate_number()
        super().save(*args, **kwargs)
        self.calculate_total_amount()

    def generate_number(self):
        code = str(uuid4())[:8]
        self.number = 'order№' + code

    def calculate_total_amount(self):
        # print(self.order_items.all(), '!@#!@#!@#!@#@!#!@#!@#')
        # print(self.order_items)
        # print(self.items.all())
        # print(self)
        total_amount = sum(item.amount for item in self.order_items.all())
        self.total_amount = total_amount

    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')
