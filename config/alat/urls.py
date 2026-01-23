from rest_framework.routers import DefaultRouter
from .views import AlatViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'alat', AlatViewSet, basename='alat')

urlpatterns = [
        path('', include(router.urls))
]
