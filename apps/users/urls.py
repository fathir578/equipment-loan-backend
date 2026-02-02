# apps/users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Inisialisasi router
router = DefaultRouter()
# Daftarkan ViewSet User ke router
router.register(r'', views.UserViewSet, basename='user') # Endpoint akan menjadi /users/

urlpatterns = [
    # Gunakan router untuk semua endpoint CRUD
    path('', include(router.urls)),
]
