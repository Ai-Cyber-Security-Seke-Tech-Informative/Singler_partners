from rest_framework import serializers
from .models import JoinApplication

class JoinApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinApplication
        fields = '__all__'  # o lista explícita si quieres

    def validate(self, data):
        # Ejemplo: validación de consentimientos obligatorios
        if not data.get('data_consent'):
            raise serializers.ValidationError("Debe aceptar el consentimiento de datos.")
        if not data.get('terms_agree'):
            raise serializers.ValidationError("Debe certificar que la información es verdadera.")
        return data
