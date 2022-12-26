from django.db import models

# Create your models here.

class Cadastro (models.Model):
    email = models.EmailField(max_length=254)
    senha = models.CharField(max_length=100)

class Cursos(models.Model):
    curso = models.CharField(max_length=150)
    tempoD = models.IntegerField()