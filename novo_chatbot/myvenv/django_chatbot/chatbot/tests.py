from django.test import TestCase
from .models import *


##Teste Livro 
class LivroModelTest(TestCase):
    def test_class_str(self):
        livro = Livro()
        livro.nome = 'A arte da ciência de dados'
        livro.autor = 'David Matos'
        livro.especialidade = 'ciência de dados'
        livro.descricao = 'livro sobre ciencia de dados '
        livro.disponibilidade = True
        livro.edicao = 5

        self.assertEquals(livro.__str__(), 'A arte da ciência de dados, ciência de dados, True, David Matos, 5 ')

class LivroViewTests(TestCase):
    @classmethod

    def setUpTestData(cls):
        Livro.objects.create(nome= 'A arte da ciência de dados', autor= 'David Matos',disponibilidade= True,
                                descricao= 'livro sobre ciencia de dados',
                                especialidade= 'ciência de dados',
                                edicao= 5) 


##Teste Materia

class MateriaModelTest(TestCase):
    def test_class_str(self):
        materia = Materia()
        materia.nome = 'Qualidade de Software'
        materia.descricao = 'materia sobre qualidade de software'
        materia.especialidade = 'Desenvolvimento'
        materia.codigo = 'DCC083'
        
        

        self.assertEquals(materia.__str__(), 'Qualidade de Software, Desenvolvimento, DCC083 ')

class MateriaViewTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        Materia.objects.create(nome= 'Qualidade de Software', descricao= 'David Matos', especialidade= 'Desenvolvimento',
                                codigo= 'DCC083') 


##Teste Site

class SiteModelTest(TestCase):
    def test_class_str(self):
        site = Site()
        site.nome = 'Medium'
        site.descricao = 'site que possui artigos sobre múltiplos assuntos'
        site.especialidade = 'Engenharia de software'
        site.link = 'www.medium.com'
        
        

        self.assertEquals(site.__str__(), 'Medium, Engenharia de software, www.medium.com ')

class SiteViewTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        Site.objects.create(nome= 'Medium',
                                descricao= 'site que possui artigos sobre múltiplos assuntos',
                                especialidade= 'Engenharia de software',
                                link= 'www.medium.com') 


##Teste Video

class VideoModelTest(TestCase):
    def test_class_str(self):
        video = Video()
        video.nome = 'Node.js: Iniciando da teoria à prática'
        video.descricao = 'Fala dev !! Mayk Brito na área! O que acha de hoje estudarmos sobre o Node.js?'
        video.especialidade = 'Desenvolvimento'
        video.link = 'https://www.youtube.com/watch?v=DiXbJL3iWVs&ab_channel=Rocketseat'
        video.canal = 'Rocketseat'
        video.duracao = '1:33:18'
        
        

        self.assertEquals(video.__str__(), 'Node.js: Iniciando da teoria à prática, Desenvolvimento, https://www.youtube.com/watch?v=DiXbJL3iWVs&ab_channel=Rocketseat ')

class VideoViewTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        Video.objects.create(nome= 'Node.js: Iniciando da teoria à prática', descricao= 'Fala dev !! Mayk Brito na área! O que acha de hoje estudarmos sobre o Node.js?', especialidade= 'Desenvolvimento',
                                link= 'https://www.youtube.com/watch?v=DiXbJL3iWVs&ab_channel=Rocketseat', canal='Rocketseat', duracao='1:33:18') 


##Teste Professor

class ProfessorModelTest(TestCase):
    def test_class_str(self):
        professor = Professor()
        professor.nome = 'Alessandreia'
        professor.descricao = 'Professora com especialidade em Engenharia de software e gamificação'
        professor.especialidade = 'Engenharia de Software'
        professor.sala = '104'
        professor.email = 'alessandreia@ice.ufjf.br' 
        

        self.assertEquals(professor.__str__(), 'Alessandreia, Engenharia de Software, 104, alessandreia@ice.ufjf.br ')

class ProfessorViewTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        Professor.objects.create(nome= 'Alessandreia',
                                descricao= 'Professora com especialidade em Engenharia de Software e gamificação',
                                especialidade= 'Engenharia de Software',
                                sala= '104',
                                email= 'alessandreia@ice.ufjf.br' ) 
