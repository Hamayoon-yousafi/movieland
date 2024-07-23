from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver 

@receiver(post_save, sender=User)
def profile_updated(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, )

@receiver(post_delete, sender=User)
def delete_user(sender, instance, **kwargs):
    try:
        profile = Profile.objects.get(user=instance)
    except:
        profile = None
    if profile:
        profile.delete()