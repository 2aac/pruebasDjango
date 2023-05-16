from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html', {'form': AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user is None:
            return render(request, 'index.html', {'form': AuthenticationForm})

        login(request, user)
        return redirect('log')


@login_required
def login(request):
    return render(request, 'login.html')
