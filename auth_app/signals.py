from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import StaffProfile
from allauth.socialaccount.models import SocialAccount

@receiver(post_save, sender=User)
def create_or_update_staff_profile(sender, instance, created, **kwargs):
    if created:
        StaffProfile.objects.create(
            user=instance,
            full_name=instance.get_full_name() or instance.username,
            email=instance.email
        )
    else:
        instance.staff_profile.save()
