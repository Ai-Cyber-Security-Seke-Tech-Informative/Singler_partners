from django import forms
from .models import StaffProfile, AdminContactMessage
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

# -------------------
# User Signup via Invite Token
# -------------------

class InvitedSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=100)
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    phone = forms.CharField(max_length=20)
    location = forms.CharField(max_length=100)
    address = forms.CharField(widget=forms.Textarea, required=False)
    profile_picture = forms.ImageField(required=False)
    department = forms.CharField(max_length=100)
    role = forms.CharField(max_length=50)
    employment_type = forms.ChoiceField(choices=[
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contract', 'Contract'),
        ('Intern', 'Intern')
    ])

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'full_name', 'gender',
                  'date_of_birth', 'phone', 'location', 'address', 'profile_picture',
                  'department', 'role', 'employment_type']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email

# -------------------
# Admin Contact Form
# -------------------

class AdminContactForm(forms.ModelForm):
    class Meta:
        model = AdminContactMessage
        fields = ['full_name', 'email', 'issue', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'issue': forms.TextInput(attrs={'placeholder': 'Short issue summary'}),
            'message': forms.Textarea(attrs={'placeholder': 'Describe your issue here...'}),
        }

# -------------------
# Staff Profile Update
# -------------------

class StaffProfileUpdateForm(forms.ModelForm):
    # Extra fields (not from model)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}),
        required=False,
        label="New Password",
        help_text="Leave blank if you don't want to change it."
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        required=False,
        label="Confirm Password"
    )

    class Meta:
        model = StaffProfile
        exclude = ['user', 'id_number', 'date_joined', 'last_updated', 'is_verified']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optional: Control field ordering if using {{ form }}
        order = ['full_name', 'email', 'password', 'confirm_password']
        remaining = [f for f in self.fields if f not in order]
        self.order_fields(order + remaining)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and password != confirm_password:
            raise ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        profile = super().save(commit=False)
        password = self.cleaned_data.get("password")

        if commit:
            profile.save()
            if password:
                user = profile.user
                user.set_password(password)
                user.save()

        return profile

# -------------------
# Optional: Existing full StaffProfile registration form (if needed)
# -------------------

class UserForm(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = "__all__"
