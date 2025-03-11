from django.db import models

# Create your models here.

class Contact(models.Model):
    RESEAU_CHOICES = [('Airtel', 'Airtel'),('MTN', 'MTN'),]
    CATEGORIE_CHOICES = [('Famille', 'Famille'),('Professionnel', 'Professionnel'),('Autres', 'Autres'),]

    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    reseau = models.CharField(max_length=10, choices=RESEAU_CHOICES)
    categorie = models.CharField(max_length=15, choices=CATEGORIE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"