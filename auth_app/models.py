from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone



# -- Invite model to handle tokenized signup links --

class InviteToken(models.Model):
    email = models.EmailField(unique=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        if self.created_at is None:
            return False  # or True depending on your logic
        return (timezone.now() - self.created_at).days >= 2

    def __str__(self):
        return f"Invite for {self.email} - {'Used' if self.used else 'Pending'}"

class StaffProfile(models.Model):
    # Link to built-in Django User model
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_profile')

    # Personal Information
    full_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100, unique=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='staff_profiles/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id_number:
            self.id_number = str(uuid.uuid4())[:8]  # Example: short unique ID
        super().save(*args, **kwargs)

    # Professional Information
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    employment_type = models.CharField(
        max_length=20,
        choices=[
            ('Full-time', 'Full-time'),
            ('Part-time', 'Part-time'),
            ('Contract', 'Contract'),
            ('Intern', 'Intern'),
        ],
        default='Full-time'
    )

    # Optional Social Provider Field
    social_provider = models.CharField(max_length=30, blank=True, null=True)

    # Admin Info
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} ({self.user.email})"
    

class AdminContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    issue = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.issue[:30]}"
