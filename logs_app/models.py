from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class LogEntry(models.Model):
    LEVEL_CHOICES = [
        ('INFO', 'Info'),
        ('WARN', 'Warning'),
        ('ERROR', 'Error'),
        ('CRIT', 'Critical'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='log_entries')
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    log_level = models.CharField(max_length=5, choices=LEVEL_CHOICES, default='INFO')
    category = models.CharField(max_length=100, blank=True, null=True)  # e.g., authentication, system, network
    action = models.CharField(max_length=255)  # e.g., "User login", "File uploaded"
    description = models.TextField(blank=True, null=True)
    request_path = models.CharField(max_length=255, blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    attachment = models.FileField(upload_to='log_attachments/', blank=True, null=True)

    def __str__(self):
        return f"[{self.log_level}] {self.action} @ {self.timestamp.isoformat()}"
