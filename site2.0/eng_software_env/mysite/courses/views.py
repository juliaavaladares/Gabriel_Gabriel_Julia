from django.shortcuts import render
from django.views.decorators.http import require_POST



def index(request):
    return render(request, 'courses/index.html')

def admin_home(request):
    return render(request, 'courses/admin_home.html')