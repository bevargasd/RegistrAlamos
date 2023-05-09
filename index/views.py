from django.shortcuts import render, redirect
from .models import *
from .forms import UserRegisterForm
from django.contrib import messages

def inicio(request):
    return render(request, 'index.html') 

def login(request):
    return render(request, 'login.html') 

def home(request):
    return render(request, 'home.html') 

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return redirect('home')

    else: 
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'registro.html', context)
