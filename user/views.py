from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import RegisterForm
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            messages.success(request,
                             f'congrats {username} signed up successfully .')
            return redirect('home')
    else:
        form = RegisterForm()

    context = {'title': 'register', 'form': form}
    return render(request, 'register.html', context)
