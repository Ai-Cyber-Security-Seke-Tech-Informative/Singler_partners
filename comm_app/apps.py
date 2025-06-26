# comm_app/apps.py
from django.apps import AppConfig

class CommAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comm_app'

    def ready(self):
        import comm_app.signals
