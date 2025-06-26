from django.contrib import admin
from .models import JoinApplication

@admin.register(JoinApplication)
class JoinApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'email', 'phone', 'position', 'location',
        'experience_years', 'work_schedule', 'submitted_at'
    )
    list_filter = (
        'position', 'location', 'experience_years', 'work_schedule', 'submitted_at'
    )
    search_fields = ('full_name', 'email', 'phone', 'skills', 'why_join', 'unique_skills')
    readonly_fields = ('submitted_at',)
    ordering = ('-submitted_at',)

    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'email', 'phone', 'linkedin')
        }),
        ('Position Details', {
            'fields': ('position', 'location')
        }),
        ('Experience and Qualifications', {
            'fields': ('experience_years', 'skills', 'resume', 'cover_letter')
        }),
        ('Availability', {
            'fields': ('start_date', 'work_schedule')
        }),
        ('Motivation & Fit', {
            'fields': ('why_join', 'unique_skills')
        }),
        ('Consent', {
            'fields': ('data_consent', 'terms_agree')
        }),
        ('Metadata', {
            'fields': ('submitted_at',)
        }),
    )
