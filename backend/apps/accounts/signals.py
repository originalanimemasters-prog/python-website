from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, UserProgress


@receiver(post_save, sender=User)
def create_user_progress(sender, instance, created, **kwargs):
    if created:
        UserProgress.objects.create(user=instance)