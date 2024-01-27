from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


User = get_user_model()


@receiver(post_save, sender=User)
def activate_superuser(sender, instance, **kwargs):
    if instance.is_superuser and not instance.is_active:
        instance.is_active = True
        instance.save()
