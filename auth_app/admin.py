from django.contrib import admin
from django.utils.html import format_html
from django.core.mail import send_mail
from django.conf import settings
from .models import StaffProfile, AdminContactMessage, InviteToken

@admin.register(InviteToken)
class InviteTokenAdmin(admin.ModelAdmin):
    list_display = ('email', 'token', 'used', 'created_at', 'invite_link')
    readonly_fields = ('token', 'created_at')

    def save_model(self, request, obj, form, change):
        # Save the invite token normally
        super().save_model(request, obj, form, change)

        # If this is a new invite and it is unused, send the invitation email
        if not obj.used and not change:
            self.send_invitation_email(obj)
            # Show confirmation message in the admin interface
            self.message_user(request, f"Invitation email sent to {obj.email}")

    def send_invitation_email(self, invite_token):
        signup_url = f"http://127.0.0.1:8001/invite-signup/{invite_token.token}/"
        subject = "Your Invitation to Join Singler"
        message = (
            f"Hello,\n\n"
            f"You have been invited to join Singler. Please use the following link to complete your registration:\n\n"
            f"{signup_url}\n\n"
            f"Note: This link expires in 2 days.\n\n"
            f"Best regards,\n"
            f"The Singler Team"
        )
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [invite_token.email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

    def invite_link(self, obj):
        # Show clickable invite link in the admin list display
        return format_html(
            '<a href="http://127.0.0.1:8001/invite-signup/{}" target="_blank">Invite Link</a>',
            obj.token
        )
    invite_link.short_description = "Signup Link"


# Register your other models as usual if you want
# admin.site.register(StaffProfile)
# admin.site.register(AdminContactMessage)



@admin.register(StaffProfile)
class StaffProfileAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'email', 'department', 'role', 'employment_type',
        'is_verified', 'is_active', 'date_joined', 'last_updated', 'profile_picture_preview'
    )
    search_fields = ('full_name', 'email', 'id_number', 'department', 'role')
    list_filter = ('department', 'role', 'employment_type', 'is_verified', 'is_active', 'gender')
    readonly_fields = ('date_joined', 'last_updated', 'profile_picture_preview')
    
    fieldsets = (
        ('Personal Information', {
            'fields': (
                'user', 'full_name', 'id_number', 'email', 'gender', 'date_of_birth', 
                'phone', 'location', 'address', 'profile_picture', 'profile_picture_preview'
            ),
        }),
        ('Professional Information', {
            'fields': ('department', 'role', 'employment_type', 'social_provider'),
        }),
        ('Admin Status & Timestamps', {
            'fields': ('is_verified', 'is_active', 'date_joined', 'last_updated'),
        }),
    )

    def profile_picture_preview(self, obj):
        if obj.profile_picture:
            return format_html(
                '<img src="{}" style="max-height: 150px; max-width: 150px; border-radius: 5px;" />',
                obj.profile_picture.url
            )
        return "No image available"
    profile_picture_preview.short_description = "Profile Picture Preview"


@admin.register(AdminContactMessage)
class AdminContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'issue', 'submitted_at']
    search_fields = ['full_name', 'email', 'issue']
    list_filter = ['submitted_at']