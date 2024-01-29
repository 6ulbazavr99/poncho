# from django.db.models.signals import pre_save
# from django.dispatch import receiver
#
# from order.models import OrderItem, Order
# from product.models import Product
#
#
# @receiver(pre_save, sender=OrderItem)
# def update_order_item_amount(sender, instance, **kwargs):
#     instance.amount = instance.product.price * instance.quantity
#     instance.save()
#
#
# @receiver(pre_save, sender=Product)
# def update_order_item_amount_on_product_price_change(sender, instance, **kwargs):
#     order_items = OrderItem.objects.filter(product=instance)
#     for order_item in order_items:
#         order_item.amount = order_item.product.price * order_item.quantity
#         order_item.save()
