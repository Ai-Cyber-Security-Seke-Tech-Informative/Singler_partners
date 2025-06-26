from django.urls import path
from . import views

app_name = 'logs_app'

urlpatterns = [
    path('logs/', views.log_list, name='logs'),
]
