from django.db import models

class PartnerInquiry(models.Model):
    PARTNERSHIP_CHOICES = [
        ("techProvider", "Tech Provider"),
        ("brandOwner", "Brand Owner"),
        ("enforcementAgency", "Enforcement Agency"),
        ("other", "Other"),
    ]

    org_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    partnership_type = models.CharField(max_length=50, choices=PARTNERSHIP_CHOICES)
    description = models.TextField()
    attachments = models.FileField(upload_to="partner_attachments/", blank=True, null=True)
    consent = models.BooleanField()

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.org_name} - {self.contact_person}"
