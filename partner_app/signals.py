from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PartnerInquiry

@receiver(post_save, sender=PartnerInquiry)
def handle_partner_inquiry_submission(sender, instance, created, **kwargs):
    if created:
        print(f"[Signal] New Partner Inquiry from {instance.contact_person} ({instance.org_name})")
        # You can plug in email sending, logging, or other async tasks here
