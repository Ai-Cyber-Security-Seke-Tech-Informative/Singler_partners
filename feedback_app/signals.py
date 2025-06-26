from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Feedback
from django.core.mail import send_mail

@receiver(post_save, sender=Feedback)
def send_feedback_notification(sender, instance, created, **kwargs):
    if created:
        # Example: notify internal email
        send_mail(
            subject=f'New Feedback: {instance.feedback_type}',
            message=f'From: {instance.full_name} ({instance.email})\n\n{instance.message}',
            from_email='noreply@yourdomain.com',
            recipient_list=['support@yourdomain.com'],
            fail_silently=True,
        )
