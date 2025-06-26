# comm_app/admin.py
from django.contrib import admin
from .models import Notification, NotificationReadStatus

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'notification_type', 'sender', 'created_at')
    search_fields = ('title', 'message')
    list_filter = ('notification_type', 'created_at')
    filter_horizontal = ('recipients',)

@admin.register(NotificationReadStatus)
class NotificationReadStatusAdmin(admin.ModelAdmin):
    list_display = ('notification', 'user', 'read_at')
    search_fields = ('notification__title', 'user__username')
    list_filter = ('read_at',)
