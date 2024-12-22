from rest_framework import serializers
from .models import Candidat, Recruteur

class CandidatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidat
        fields = ['id', 'nom', 'prenom', 'email', 'telephone', 'date_naissance']
        

class RecruteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruteur
        fields = ['id', 'entreprise', 'email', 'telephone', 'site_web']