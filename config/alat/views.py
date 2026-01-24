from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Alat
from .serializers import AlatSerializer
from .permision import IsAdminOrReadOnly, IsOwnerOrAdmin, AlatPermission, AlatObjectPermission

class AlatViewSet(ModelViewSet):
    queryset = Alat.objects.all()
    serializer_class = AlatSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminOrReadOnly,
        IsOwnerOrAdmin,
        AlatPermission,
        AlatObjectPermission,
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)    
    

