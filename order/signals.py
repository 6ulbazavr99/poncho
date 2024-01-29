# from django.contrib.auth import get_user_model
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from order.models import Order
#
# # User = get_user_model()
#
#
# @receiver(post_save, sender=Order)
# def calculate_total_amount(sender, instance, **kwargs):
#     print(instance.order_items.all(), 'POPOPOPOPOP')
#     print(instance.items.product.all())
#     # if instance.is_superuser and not instance.is_active:
#     #     instance.is_active = True
#     #     instance.save()
