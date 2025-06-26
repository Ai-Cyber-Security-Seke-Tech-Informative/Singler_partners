from django.urls import path
from .import views

app_name = 'partner_app'
urlpatterns = [
    path('partner_us/', views.partner_us, name='partner_us'),
]
