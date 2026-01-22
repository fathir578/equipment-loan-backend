# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from .models import Alat
from .serializers import AlatSerializer

class AlatListCreateView (APIView):
    def get (self, request):
        alat = Alat.objects.all()
        serializer = AlatSerializer(alat, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AlatSerializer(data=request.data)

        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
class AlatDetailView(RetrieveAPIView):
    queryset = Alat.objects.all()
    serializer_class = AlatSerializer    


# Create your views here.
