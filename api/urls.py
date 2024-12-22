from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CandidatViewSet, RecruteurViewSet

# routeur
router = DefaultRouter()
router.register(r'candidats', CandidatViewSet, basename='candidat')
router.register(r'recruteurs', RecruteurViewSet, basename='recruteur')

urlpatterns = [
    path('', include(router.urls)),  
]