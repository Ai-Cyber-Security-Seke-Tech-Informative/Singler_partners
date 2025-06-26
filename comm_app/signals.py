# comm_app/signals.py
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Notification
import logging

logger = logging.getLogger(__name__)

@receiver(m2m_changed, sender=Notification.recipients.through)
def log_notification_recipients(sender, instance, action, **kwargs):
    if action == 'post_add':
        logger.info(f"Notification '{instance.title}' sent to {instance.recipients.count()} users.")
