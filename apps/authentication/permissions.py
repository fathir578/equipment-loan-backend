from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'
    
class isPetugas(BasePermission):
    """
    Allows access only to petugas users.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'petugas'

class isPemnjam(BasePermission):
    """
    Allows access only to peminjam users.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'peminjam'