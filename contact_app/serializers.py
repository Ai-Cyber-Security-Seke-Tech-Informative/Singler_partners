from rest_framework import serializers
from .models import ContactInquiry

class ContactInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInquiry
        fields = '__all__'

    def validate_privacy_consent(self, value):
        if not value:
            raise serializers.ValidationError("You must consent to privacy terms.")
        return value
