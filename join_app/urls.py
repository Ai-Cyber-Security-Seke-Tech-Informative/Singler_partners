from django.urls import path
from .import views


app_name = 'join_app' 
urlpatterns = [
    path('join/', views.join_us, name='join'),
]
