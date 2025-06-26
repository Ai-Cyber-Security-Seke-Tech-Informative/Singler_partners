from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'feedback_type', 'email', 'country', 'city', 'privacy_consent', 'submitted_at')
    list_filter = ('feedback_type', 'country', 'privacy_consent', 'submitted_at')
    search_fields = ('full_name', 'email', 'message', 'city')
    readonly_fields = ('submitted_at',)
    ordering = ('-submitted_at',)

    fieldsets = (
        (None, {
            'fields': (
                'feedback_type', 'full_name', 'email', 'phone',
                'country', 'city', 'message', 'attachment',
                'privacy_consent', 'submitted_at'
            )
        }),
    )
