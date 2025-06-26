# comm_app/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('info', 'Info'),
        ('alert', 'Alert'),
        ('task', 'Task'),
        ('reminder', 'Reminder'),
    ]

    sender = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='sent_notifications'
    )
    recipients = models.ManyToManyField(User, related_name='received_notifications')
    notification_type = models.CharField(
        max_length=20, choices=NOTIFICATION_TYPES, default='info'
    )
    title = models.CharField(max_length=255)
    message = models.TextField()
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} to {self.recipients.count()} users"


class NotificationReadStatus(models.Model):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    read_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('notification', 'user')

    def __str__(self):
        return f"{self.user.username} read {self.notification.title}"
