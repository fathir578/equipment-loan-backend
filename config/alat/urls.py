from django.urls import path
from .views import AlatListCreateView

urlpatterns = [
    path('alat/', AlatListCreateView.as_view(), name='alat-list-create'),
]
