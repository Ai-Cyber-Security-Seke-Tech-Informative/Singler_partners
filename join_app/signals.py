from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import JoinApplication

@receiver(post_save, sender=JoinApplication)
def application_created(sender, instance, created, **kwargs):
    if created:
        # Aquí puedes poner la lógica que quieres ejecutar cuando se cree una nueva aplicación
        print(f"Nueva aplicación recibida de: {instance.full_name}")
        # Por ejemplo, enviar un email de confirmación o notificación al admin
        # send_email_to_admin(instance)
