from django.apps import AppConfig

class LogsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'logs_app'

    def ready(self):
        import logs_app.signals  # noqa
