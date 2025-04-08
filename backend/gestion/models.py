from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Utilisateur(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('etudiant', 'Étudiant'),
        ('enseignant', 'Enseignant'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='etudiant')

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    stock_disponible = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.titre

class Emprunt(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    date_emprunt = models.DateField(auto_now_add=True)
    date_retour_prevue = models.DateField()
    statut = models.CharField(max_length=20, choices=[('en cours', 'En cours'), ('retourne', 'Retourné')], default='en cours')

class Reservation(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    date_reservation = models.DateField(auto_now_add=True)
    statut = models.CharField(max_length=20, default='en attente')

class Notification(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, default='non lu')
