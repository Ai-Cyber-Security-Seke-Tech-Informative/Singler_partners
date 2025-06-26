from django.apps import AppConfig

class PartnerAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'partner_app'

    def ready(self):
        import partner_app.signals  # noqa
