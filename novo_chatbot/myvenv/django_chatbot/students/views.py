from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentCreationForm, StudentUpdateForm, ProfileUpdateform
from django.contrib.auth.decorators import login_required


## View para rgistro do Aluno
def register(request):
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada com sucesso! Você pode entrar na sua conta')
            return redirect ('login')

    else:
        form = StudentCreationForm()
    return render(request,'students/register.html', {'form': form})

## View para atualização do perfil do aluno
@login_required
def profile(request):
    if request.method == 'POST':
        s_form = StudentUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateform(request.POST, request.FILES,instance=request.user.profile)
        if s_form.is_valid() and p_form.is_valid():
            s_form.save()
            p_form.save()
            messages.success(request, f'Sua conta foi atualizada com sucesso!')
            return redirect('profile')
    
    else:
        s_form = StudentUpdateForm(instance=request.user)
        p_form = ProfileUpdateform(instance=request.user.profile)

    context = {
        's_form': s_form,
        'p_form': p_form
    }
    return render(request, 'students/profile.html', context)

