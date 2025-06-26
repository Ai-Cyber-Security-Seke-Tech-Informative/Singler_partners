from django.db import models

class ContactInquiry(models.Model):
    SUBJECT_CHOICES = [
        ("General Inquiry", "General Inquiry"),
        ("Partnership Opportunity", "Partnership Opportunity"),
        ("Request a Demo", "Request a Demo"),
        ("Report a Counterfeit Product", "Report a Counterfeit Product"),
        ("Request Support", "Request Support"),
        ("Media / Press Inquiry", "Media / Press Inquiry"),
        ("Other", "Other"),
    ]

    CONTACT_METHOD_CHOICES = [
        ("email", "Email"),
        ("phone", "Phone"),
    ]

    CONTACT_TIME_CHOICES = [
        ("Morning", "Morning"),
        ("Afternoon", "Afternoon"),
        ("Evening", "Evening"),
    ]

    COUNTRY_CHOICES = [
        ("USA", "USA"),
        ("UK", "UK"),
        ("Kenya", "Kenya"),
        ("India", "India"),
        ("Germany", "Germany"),
        ("Other", "Other"),
    ]

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)

    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    contact_method = models.CharField(max_length=10, choices=CONTACT_METHOD_CHOICES, blank=True, null=True)
    contact_time = models.CharField(max_length=20, choices=CONTACT_TIME_CHOICES, blank=True, null=True)

    message = models.TextField()
    attachment = models.FileField(upload_to="contact_attachments/", blank=True, null=True)

    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    privacy_consent = models.BooleanField(default=False)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.subject}"
