from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from  .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'full_name', 'role',
            'phone_number', 'is_active', 'is_staff', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username', 'email', 'full_name', 'role',
            'phone_number', 'password', 'password_confirm'
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password_confirm": "Password dan konfirmasi password tidak cocok."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm') # Hapus password_confirm sebelum menyimpan
        # Gunakan method create_user dari custom UserManager untuk hashing
        user = User.objects.create_user(**validated_data)
        return user
    class UserUpdateSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = [
                'username', 'email', 'full_name', 'role',
                'phone_number', 'is_active'
            ]
        
        def validate_email(self, value ):
            user = self.context['request'].user
            if User.objects.filter(email=value).exclude(pk=user.pk).exists():
                raise serializers.ValidationError("Email ini sudah digunakan oleh user lain.")
            return value
        
        def validate_username(self, value):

            user = self.context['request'].user
            if User.objects.filter(username=value).exclude(pk=user.pk).exists():
                raise serializers.ValidationError("Username ini sudah digunakan oleh user lain.")
            return value