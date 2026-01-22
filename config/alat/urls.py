from django.urls import path
from .views import AlatListCreateView, AlatDetailView

urlpatterns = [
    path('alat/', AlatListCreateView.as_view(), name='alat-list-create'),
    path('alat/<int:pk>/', AlatDetailView.as_view()),
]
