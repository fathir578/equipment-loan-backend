from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:  
            return True
        return request.user.is_authenticated and request.user.is_staff
    
# class IsOwnerOrAdmin(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
        
#         return obj.owner == request.user

# class AlatPermission(BasePermission):
#     def has_permission(self, request, view):
#         # Semua user login boleh lihat list & detail
#         if view.action in ['list', 'retrieve']:
#             return request.user.is_authenticated

#         # Create hanya admin
#         if view.action == 'create':
#             return request.user.is_staff

#         return True

# class AlatObjectPermission(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if view.action in ['update', 'partial_update']:
#             return obj.user == request.user 
        
#         if view.action == 'destroy':
#             return False
#         return True