from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model untuk sistem peminjaman alat.

    Menyimpan informasi dasar tentang user termasuk role (admin, petugas, peminjam).
    Menggunakan email sebagai identifier utama daripada username.

    Attributes:
        id (BigAutoField): Primary key unik.
        username (CharField): Username unik untuk login.
        email (EmailField): Alamat email unik untuk login dan komunikasi.
        full_name (CharField): Nama lengkap user.
        role (CharField): Role user dalam sistem ('admin', 'petugas', 'peminjam').
        phone_number (CharField): Nomor telepon user.
        is_active (BooleanField): Status akun aktif/tidak.
        is_staff (BooleanField): Izin untuk mengakses admin site.
        is_superuser (BooleanField): Izin untuk akses tingkat superuser.
        created_at (DateTimeField): Waktu pembuatan akun.
        updated_at (DateTimeField): Waktu terakhir akun diperbarui.
        last_login (DateTimeField): Waktu login terakhir.
    """
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('petugas', 'Petugas'),
        ('peminjam', 'Peminjam'),
    ]

    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='peminjam'
    )
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'  # Gunakan email untuk login
    REQUIRED_FIELDS = ['username', 'full_name']  # Field wajib selain email dan password

