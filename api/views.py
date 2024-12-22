from rest_framework.viewsets import ModelViewSet
from .models import Candidat, Recruteur
from .serializers import CandidatSerializer, RecruteurSerializer

# Vue pour les candidats
class CandidatViewSet(ModelViewSet):
    queryset = Candidat.objects.all()
    serializer_class = CandidatSerializer

# Vue pour les recruteurs
class RecruteurViewSet(ModelViewSet):
    queryset = Recruteur.objects.all()
    serializer_class = RecruteurSerializer