# apps/users/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import get_user_model
from .models import User
from .serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer
from .authentication.permissions import IsAdminOrPetugas # Impor permission dari auth

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # Default permission: harus authenticated
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action in ('update', 'partial_update'):
            return UserUpdateSerializer
        else:
            return UserSerializer

    def get_permissions(self):

        permission_classes = self.permission_classes
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        elif self.action in ['list', 'retrieve']:
             permission_classes = [IsAuthenticated, IsAdminOrPetugas]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
       
        return User.objects.all()