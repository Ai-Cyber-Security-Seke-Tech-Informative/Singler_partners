from django.urls import path
from . import views

app_name = 'comm_app'

urlpatterns = [

    path('notification-create/create/', views.notification_create, name='notification_create'),
    path('notifications-list/', views.notification_list, name='notification_list'),
    path('notifications-detail/<int:pk>/', views.notification_detail, name='notification_detail'),
    path('notifications/<int:pk>/delete/', views.notification_delete, name='notification_delete'),
]
