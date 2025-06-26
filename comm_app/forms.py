# comm_app/forms.py
from django import forms
from .models import Notification

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['recipients', 'notification_type', 'title', 'message', 'url']
        widgets = {
            'recipients': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'notification_type': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter message'}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Optional link'}),
        }
