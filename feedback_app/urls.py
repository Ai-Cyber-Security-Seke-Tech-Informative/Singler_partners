# feedback_app/urls.py

from django.urls import path
from .import views

app_name = 'feedback_app'  # Optional: use for namespacing

urlpatterns = [
    path('feedback/', views.feedback, name='feedback'),
]
