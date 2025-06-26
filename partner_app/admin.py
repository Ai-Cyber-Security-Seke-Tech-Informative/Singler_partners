from django.contrib import admin
from .models import PartnerInquiry

@admin.register(PartnerInquiry)
class PartnerInquiryAdmin(admin.ModelAdmin):
    list_display = (
        'org_name', 'contact_person', 'email', 'phone', 'partnership_type', 'submitted_at'
    )
    list_filter = ('partnership_type', 'submitted_at')
    search_fields = ('org_name', 'contact_person', 'email', 'description')
    readonly_fields = ('submitted_at',)
    ordering = ('-submitted_at',)

    fieldsets = (
        (None, {
            'fields': (
                'org_name', 'contact_person', 'email', 'phone', 'partnership_type',
                'description', 'attachments', 'consent', 'submitted_at'
            )
        }),
    )
