from rest_framework.routers import DefaultRouter
from .views import AlatViewSet

router = DefaultRouter()
router.register(r'alat', AlatViewSet, basename='alat')

urlpatterns = router.urls
