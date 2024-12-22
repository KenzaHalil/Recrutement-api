from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Candidat, Recruteur

class CandidatTests(APITestCase):

    def setUp(self):
        
        self.valid_candidat_data = {
            'nom': 'Halil',
            'prenom': 'Nihad',
            'email': 'halilnihad@gmail.com',
            'telephone': '0123456789',
            'date_naissance': '1990-01-01'
        }
        self.invalid_candidat_data = {
            'nom': '',
            'prenom': 'Jean',
            'email': '.....@',
            'telephone': '2',
            'date_naissance': '1990-01-01'
        }
        self.candidat_url = reverse('candidat-list')  

    def test_create_candidat_valid(self):
        response = self.client.post(self.candidat_url, self.valid_candidat_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Candidat.objects.count(), 1)
        self.assertEqual(Candidat.objects.get().nom, 'Halil')  

    def test_create_candidat_invalid(self):
        response = self.client.post(self.candidat_url, self.invalid_candidat_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_candidats(self):
        Candidat.objects.create(**self.valid_candidat_data)
        response = self.client.get(self.candidat_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nom'], 'Halil') 


    