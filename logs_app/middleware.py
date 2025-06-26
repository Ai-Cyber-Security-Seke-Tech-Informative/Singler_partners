from .models import LogEntry

class ActivityLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        try:
            user = request.user if request.user.is_authenticated else None
            ip = self.get_client_ip(request)
            user_agent = request.META.get('HTTP_USER_AGENT', '')
            path = request.path

            LogEntry.objects.create(
                user=user,
                ip_address=ip,
                log_level='INFO',
                category='request',
                action=f'Accessed {path}',
                request_path=path,
                user_agent=user_agent,
            )
        except Exception:
            # Fail silently to not break requests
            pass

        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
