from django.db import models

class JoinApplication(models.Model):
    # Personal Info
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin = models.URLField(blank=True, null=True)

    # Position Details
    POSITION_CHOICES = [
        ('brand_protection_analyst', 'Brand Protection Analyst'),
        ('counterfeit_investigation_specialist', 'Counterfeit Investigation Specialist'),
        ('cybersecurity_specialist', 'Cybersecurity Specialist'),
        ('client_relations_manager', 'Client Relations Manager'),
        ('research_development_associate', 'Research & Development Associate'),
        ('marketing_communications_specialist', 'Marketing & Communications Specialist'),
        ('other', 'Other'),
    ]
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)

    LOCATION_CHOICES = [
        ('on_site', 'On-site (Specify location later)'),
        ('remote', 'Remote'),
        ('hybrid', 'Hybrid'),
    ]
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES, blank=True, null=True)

    # Experience and Qualifications
    EXPERIENCE_CHOICES = [
        ('0_1', '0-1 years'),
        ('2_4', '2-4 years'),
        ('5_plus', '5+ years'),
    ]
    experience_years = models.CharField(max_length=10, choices=EXPERIENCE_CHOICES)
    skills = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.FileField(upload_to='cover_letters/', blank=True, null=True)

    # Availability
    start_date = models.DateField()
    WORK_SCHEDULE_CHOICES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract_freelance', 'Contract / Freelance'),
    ]
    work_schedule = models.CharField(max_length=20, choices=WORK_SCHEDULE_CHOICES, blank=True, null=True)

    # Motivation & Fit
    why_join = models.TextField()
    unique_skills = models.TextField(blank=True, null=True)

    # Consent
    data_consent = models.BooleanField()
    terms_agree = models.BooleanField()

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.position}"
