from django.apps import AppConfig

class FeedbackAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'feedback_app'

    def ready(self):
        import feedback_app.signals
