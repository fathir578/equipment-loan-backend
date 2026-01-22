from rest_framework import serializers
from .models import Alat
class AlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alat
        fields = ['id', 'nama', 'stok', 'kategori']

