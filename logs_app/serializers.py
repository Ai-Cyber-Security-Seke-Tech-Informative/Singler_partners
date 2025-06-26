from rest_framework import serializers
from .models import LogEntry
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class LogEntrySerializer(serializers.ModelSerializer):
    user = UserSummarySerializer(read_only=True)
    attachment = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = LogEntry
        fields = [
            'id', 'timestamp', 'user', 'ip_address', 'log_level', 'category', 'action',
            'description', 'request_path', 'user_agent', 'attachment'
        ]
        read_only_fields = ['timestamp', 'user']

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user') and request.user.is_authenticated:
            validated_data['user'] = request.user
        return super().create(validated_data)
