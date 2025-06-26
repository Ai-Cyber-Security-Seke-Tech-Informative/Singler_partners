from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from .models import LogEntry

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    LogEntry.objects.create(
        user=user,
        log_level='INFO',
        category='authentication',
        action='User logged in',
        ip_address=get_client_ip(request),
        request_path=request.path,
        user_agent=request.META.get('HTTP_USER_AGENT', ''),
    )

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    LogEntry.objects.create(
        user=user,
        log_level='INFO',
        category='authentication',
        action='User logged out',
        ip_address=get_client_ip(request),
        request_path=request.path,
        user_agent=request.META.get('HTTP_USER_AGENT', ''),
    )

@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    LogEntry.objects.create(
        user=None,
        log_level='WARN',
        category='authentication',
        action='Failed login attempt',
        ip_address=get_client_ip(request),
        request_path=request.path,
        user_agent=request.META.get('HTTP_USER_AGENT', ''),
        description=f"Username attempted: {credentials.get('username')}"
    )

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
