from rest_framework import serializers
from .models import Conversation, Message, MessageReadReceipt, TypingStatus
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class MessageReadReceiptSerializer(serializers.ModelSerializer):
    reader = UserSerializer(read_only=True)

    class Meta:
        model = MessageReadReceipt
        fields = ['id', 'reader', 'read_at']

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    read_receipts = MessageReadReceiptSerializer(many=True, read_only=True)
    attachments = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = Message
        fields = ['id', 'conversation', 'sender', 'content', 'attachments', 'sent_at', 'edited_at', 'read_receipts']
        read_only_fields = ['sent_at', 'edited_at', 'read_receipts']

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['sender'] = request.user
        return super().create(validated_data)

class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['id', 'title', 'participants', 'created_at', 'updated_at', 'messages']

class TypingStatusSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = TypingStatus
        fields = ['id', 'conversation', 'user', 'is_typing', 'last_updated']
