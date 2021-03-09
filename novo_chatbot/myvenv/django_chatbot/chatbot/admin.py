from django.contrib import admin
from .models import *



@admin.register(Livro)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("nome", "especialidade", "disponibilidade", "autor", "edicao")

    def show_average(self, obj):
        from django.db.models import Avg
        result = Livro.objects.filter(person=obj).aggregate(Avg("grade"))
        return result["grade__avg"]


@admin.register(Site)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("nome", "especialidade", "link")

    def show_average(self, obj):
        from django.db.models import Avg
        result = Livro.objects.filter(person=obj).aggregate(Avg("grade"))
        return result["grade__avg"]

@admin.register(Video)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("nome", "especialidade", "link", "canal", "duracao")

    def show_average(self, obj):
        from django.db.models import Avg
        result = Livro.objects.filter(person=obj).aggregate(Avg("grade"))
        return result["grade__avg"]

@admin.register(Professor)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("nome", "especialidade", "sala", "email")

    def show_average(self, obj):
        from django.db.models import Avg
        result = Livro.objects.filter(person=obj).aggregate(Avg("grade"))
        return result["grade__avg"]

@admin.register(Materia)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("nome", "especialidade", "codigo")

    def show_average(self, obj):
        from django.db.models import Avg
        result = Livro.objects.filter(person=obj).aggregate(Avg("grade"))
        return result["grade__avg"]

