from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.validators import RegexValidator
from ..users.models import User

class CustomTokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=6, write_only=True)

    def validation (self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if not email or not password:
            raise serializers.ValidationError('Email dan password harus diisi.')
        
        user = authenticate(request=self.context.get('request'), email=email, password=password)
        if not user or not user.is_active:
            raise serializers.ValidationError('Email atau password salah, atau akun tidak aktif.')
        
        attrs['user'] = user
        return attrs
    
    def to_representation(self, instance):
        from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

        jwt_serializer = TokenObtainPairSerializer()
        token_data = jwt_serializer.validate({
            'email': instance.email,
            'password': instance.password
        })

        user_data = { 
            'id': instance.id,
            'ussername': instance.username,
            'email': instance.email,
            'full_name': instance.full_name,
            'role': instance.role,
        }
        token_data.update({'user': user_data})
        return token_data 


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        validators=[validate_password],
        min_length=8

    )
    password_confirm = serializers.charfield(write_only=True)




    

