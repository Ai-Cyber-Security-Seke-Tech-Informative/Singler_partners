from rest_framework import serializers
from django.contrib.auth.models import User
from .models import StaffProfile

# 👤 1. StaffProfile Serializer – View/Update Staff Info
class StaffProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffProfile
        fields = [
            'full_name', 'id_number', 'email', 'gender', 'date_of_birth',
            'phone', 'location', 'address', 'profile_picture',
            'department', 'role', 'employment_type',
            'social_provider', 'is_verified', 'is_active',
            'date_joined', 'last_updated'
        ]
        read_only_fields = ['is_verified', 'is_active', 'date_joined', 'last_updated', 'social_provider']

# 👤 2. User Serializer – Optional if you want to expose user fields
class UserSerializer(serializers.ModelSerializer):
    staff_profile = StaffProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'staff_profile']

# 📝 3. Registration Serializer – Staff signup
class StaffRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')  # Remove confirmation field
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
