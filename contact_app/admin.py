from django.contrib import admin
from .models import ContactInquiry

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'email', 'subject', 'contact_method', 'contact_time',
        'country', 'city', 'privacy_consent', 'submitted_at'
    )
    list_filter = (
        'subject', 'contact_method', 'contact_time', 'country', 'privacy_consent', 'submitted_at'
    )
    search_fields = ('full_name', 'email', 'company', 'message', 'city')
    readonly_fields = ('submitted_at',)
    ordering = ('-submitted_at',)

    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'email', 'phone', 'company')
        }),
        ('Inquiry Details', {
            'fields': ('subject', 'contact_method', 'contact_time')
        }),
        ('Message', {
            'fields': ('message', 'attachment')
        }),
        ('Location', {
            'fields': ('country', 'city')
        }),
        ('Consent & Metadata', {
            'fields': ('privacy_consent', 'submitted_at')
        }),
    )
