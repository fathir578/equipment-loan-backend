from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group # Untuk menyembunyikan model Group jika tidak digunakan
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'full_name', 'role', 'is_active', 'is_staff', 'date_joined')
    list_display_links = ('username', 'email')
    
    list_filter = ('role', 'is_active', 'is_staff', 'date_joined')
    
    search_fields = ('username', 'email', 'full_name')
    
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}), # Basic Info
        ('Personal info', {'fields': ('full_name', 'email', 'phone_number')}), # Personal Info
        ('Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}), # Permissions
        ('Important dates', {'fields': ('last_login', 'date_joined')}), # Important Dates
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'full_name', 'phone_number', 'role', 'password1', 'password2'), # Gunakan password1/password2 untuk create
        }),
    )
    readonly_fields = ('date_joined', 'last_login')
admin.site.unregister(Group)
