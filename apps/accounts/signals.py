from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User

@receiver(post_save, sender=User)
def set_default_user_type(sender, instance, created, **kwargs):
    if created:
        if not instance.user_type:
            instance.user_type = 'investor'
            instance.save()