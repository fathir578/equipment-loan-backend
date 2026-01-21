from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
    class meta:
        model = User
        fields = [
            'id',
            'ussername',
            'email',
            'first_name',
            'last_name'
        ]
        