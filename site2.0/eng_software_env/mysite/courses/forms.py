from django import forms
from django.forms import fields
from .models import *


#Form para a adição do Site
class Site_Form(forms.ModelForm):

    nome = forms.CharField(max_length=200,
       widget=forms.TextInput(
        attrs={
            'placeholder': 'ex.: Medium'
        }), label='Nome do Site')

    descricao = forms.CharField( widget=forms.Textarea(attrs=
    {'placeholder': 'ex.: Esse site apresenta vários conteúdos sobre Engenharia de Software'}))
   
    especialidade = forms.CharField(max_length=200,
       widget=forms.TextInput(
        attrs={
            'placeholder': 'ex.: Engenharia de Software'
        }), label='Especialidade')

    link = forms.CharField(max_length=200,
       widget=forms.TextInput(
        attrs={
            'placeholder': 'ex.: www.medium.com/nome_artigo'
        }), label='Site')
    class Meta:
        model = Site
        fields = '__all__'

#Form para a adição do Livro
class Livro_form(forms.ModelForm):

    nome = forms.CharField(max_length=200,
       widget=forms.TextInput(
        attrs={
            'placeholder': 'ex.: Engenharia de Software Moderna'
        }), label='Nome do Livro')

    descricao = forms.CharField( widget=forms.Textarea(attrs=
    {'placeholder': 'ex.: Esse livro apresenta muitas informações sobre Engenharia de Software'}))
   
    especialidade = forms.CharField(max_length=200,
       widget=forms.TextInput(
        attrs={
            'placeholder': 'ex.: Engenharia de Software'
        }), label='Especialidade')

    disponibilidade = forms.BooleanField(required=False, label='Disponibilidade Livro')
    
    autor = forms.CharField(max_length=200,
       widget=forms.TextInput(
        attrs={
            'placeholder': 'ex.: David Ascher'
        }), label='Nome autor')

    class Meta:
        model = Livro
        fields = '__all__'

#Form para a adição do Vídeo
class Video_form(forms.ModelForm):

    nome = forms.CharField(max_length=200,
       widget=forms.TextInput(
        attrs={
            'placeholder': 'ex.: O que é Engenharia de Software?'
        }), label='Nome do Video')

    descricao = forms.CharField( widget=forms.Textarea(attrs=
    {'placeholder': 'ex.: Esse video apresenta um conteúdo muito bom sobre Engenharia de Software'}))
   
    especialidade = forms.CharField(max_length=200,
       widget=forms.TextInput(
        attrs={
            'placeholder': 'ex.: Engenharia de Software'
        }), label='Especialidade')

    link = forms.CharField(max_length=200,
       widget=forms.TextInput(
        attrs={
            'placeholder': 'ex.: www.youtube.com/video'
        }), label='Site')

    canal = forms.CharField(max_length=200,
       widget=forms.TextInput(
        attrs={
            'placeholder': 'ex.: Programação Dinâmica'
        }), label='Nome autor')
    
    duracao = forms.DurationField(attrs={
            'placeholder': 'ex.: 00:10:52 -> hora:minutos:segundos'
        }, label='Duração do vídeo')
    class Meta:
        model = Video
        fields = '__all__'

#Form para a adição do Professor

class Professor_form(forms.ModelForm):

    nome = forms.CharField(max_length=200,
       widget=forms.TextInput(
        attrs={
            'placeholder': 'ex.: Alessandreia'
        }), label='Nome do(a) Professor(a)')

    descricao = forms.CharField( widget=forms.Textarea(attrs=
    {'placeholder': 'ex.: Essa professora apresenta um grande conhecimento sobre Engenharia de Software'}))
   
    especialidade = forms.CharField(max_length=200,
       widget=forms.TextInput(
        attrs={
            'placeholder': 'ex.: Engenharia de Software'
        }), label='Especialidade')

    sala = forms.IntegerField(
       widget=forms.TextInput(
        attrs={
            'placeholder': 'ex.: 206'
        }), label='Sala')

    email = forms.EmailField(max_length=200,
       widget=forms.TextInput(
        attrs={
            'placeholder': 'ex.: alessandreia@gmail.com'
        }), label='Email professor')
    
    class Meta:
        model = Professor
        fields = '__all__'

#Form para a adição da Materias
class Materia_form(forms.ModelForm):

    nome = forms.CharField(max_length=200,
       widget=forms.TextInput(
        attrs={
            'placeholder': 'ex.: Engenharia de Software'
        }), label='Nome da Materia')

    descricao = forms.CharField( widget=forms.Textarea(attrs=
    {'placeholder': 'ex.: Essa aborda sobre tais e tais assuntos'}))
   
    especialidade = forms.CharField(max_length=200,
       widget=forms.TextInput(
        attrs={
            'placeholder': 'ex.: Engenharia de Software'
        }), label='Especialidade')

    codigo = forms.CharField(max_length=6,
       widget=forms.TextInput(
        attrs={
            'placeholder': 'ex.: DCC061'
        }), label='Codigo da Disciplina')

    
    class Meta:
        model = Materia
        fields = '__all__'
