from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ContactInquiry

@receiver(post_save, sender=ContactInquiry)
def notify_admin_on_contact(sender, instance, created, **kwargs):
    if created:
        print(f"🔔 New contact from {instance.full_name} — Subject: {instance.subject}")
