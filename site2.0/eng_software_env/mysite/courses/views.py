from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login

from .forms import *
from .models import *

def index(request):
    return render(request, 'courses/index.html')

def admin_home(request):
    return render(request, 'courses/admin_home.html')

# Autenticação Login do Usuario
def user_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user.
            return render(request, '/account.html')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'courses/login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'courses/login.html')

#Página do Perfil e Cadastro
def profile(request):
    return render(request, 'courses/profile.html')

#Cadastro de um novo aluno 
def register_new_student(request):
    student_form = Aluno_Form(request.POST, request.FILES)

    if student_form.is_valid():
        student_form.save()

    context = {
        'student_form' : student_form
    }
    return render(request, 'courses/profile.html', context)


    

#Página do Chatbot 
def turing(request):
    return render(request, 'courses/turing.html')

def admin_home(request):
    return render(request, 'courses/admin_home.html')
