from django.db import models

class Feedback(models.Model):
    FEEDBACK_TYPES = [
        ('appreciation', 'Appreciation'),
        ('complaint', 'Complaint'),
        ('counterfeit', 'Report a Counterfeit Product'),
        ('suggestion', 'Suggestion'),
        ('technical', 'Technical Issue'),
    ]

    feedback_type = models.CharField(max_length=20, choices=FEEDBACK_TYPES)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField()
    attachment = models.FileField(upload_to='feedback_attachments/', blank=True, null=True)
    privacy_consent = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.feedback_type}"
