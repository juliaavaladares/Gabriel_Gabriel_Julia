from django.db import models

# Create your models here.

class Material(models.Model):
    class Meta:
        abstract = True
    
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome}, {self.especialidade}"

class Site(Material):
    link = models.CharField(max_length=200)

class Livro(Material):
    disponibilidade = models.BooleanField(default=True)
    autor = models.CharField(max_length=200)
    edicao = models.IntegerField()

class Video(Material):
    link = models.CharField(max_length=200)
    canal = models.CharField(max_length=200)
    duracao = models.DurationField()


class Professor(Material):
    sala = models.IntegerField()
    email = models.EmailField()

class Materia(Material):
    codigo = models.CharField(max_length=10)
