from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Alat
from .serializers import AlatSerializer


class AlatViewSet(ModelViewSet):
    queryset = Alat.objects.all()
    serializer_class = AlatSerializer
    permission_classes = [IsAuthenticated]
