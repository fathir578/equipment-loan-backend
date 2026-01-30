
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        # Validasi username
        if not username:
            raise ValueError('Username harus diisi')
        
        # Validasi email
        if not email:
            raise ValueError('Email harus diisi')
        
        # Normalisasi email (lowercase domain)
        email = self.normalize_email(email)
        
        # Set default role jika tidak ada
        if 'role' not in extra_fields:
            extra_fields['role'] = 'peminjam'
        
        # Set default is_active
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        
        # Buat user instance
        user = self.model(
            username=username,
            email=email,
            **extra_fields
        )
        
        # Hash password
        user.set_password(password)
        
        # Simpan ke database
        user.save(using=self._db)
        
        return user