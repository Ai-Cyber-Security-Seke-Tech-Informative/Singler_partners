from django.contrib import admin
from .models import LogEntry

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = (
        'timestamp', 'log_level', 'user', 'ip_address', 'category', 'action'
    )
    list_filter = ('log_level', 'category', 'timestamp')
    search_fields = ('action', 'description', 'user__username', 'user__email', 'ip_address', 'request_path')
    readonly_fields = ('timestamp',)
    ordering = ('-timestamp',)

    fieldsets = (
        (None, {
            'fields': (
                'timestamp', 'user', 'ip_address', 'log_level', 'category',
                'action', 'description', 'request_path', 'user_agent', 'attachment'
            )
        }),
    )
