from django.db import models
from django.db.models import Avg

# Create your models here.
class Material(models.Model):
    class Meta:
        abstract = True
    
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        result = Material.objects.aggregate(Avg("grade"))
        

class Site(Material):
    link = models.URLField(("Trip Number") ,max_length=200)

    def __str__(self):
         return f"{self.nome}, {self.especialidade}, {self.link} "

class Livro(Material):
    disponibilidade = models.BooleanField(default=True)
    autor = models.CharField(max_length=200)
    edicao = models.IntegerField()

    def __str__(self):
         return f"{self.nome}, {self.especialidade}, {self.disponibilidade}, {self.autor}, {self.edicao} "

class Video(Material):
    link = models.URLField(max_length=200)
    canal = models.CharField(max_length=200)
    duracao = models.DurationField()

    def __str__(self):
         return f"{self.nome}, {self.especialidade}, {self.link} "


class Professor(Material):
    sala = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
         return f"{self.nome}, {self.especialidade}, {self.sala}, {self.email} "

class Materia(Material):
    codigo = models.CharField(max_length=10)

    def __str__(self):
         return f"{self.nome}, {self.especialidade}, {self.codigo} "
