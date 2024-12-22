from django.db import models

# Create your models here.

class Candidat(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=15)
    date_naissance = models.DateField()

    def __str__(self):
        return f'{self.nom} {self.prenom}'

class Recruteur(models.Model):
    entreprise = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=15)
    site_web = models.URLField()

    def __str__(self):
        return self.entreprise
