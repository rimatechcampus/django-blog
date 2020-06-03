from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
# from .forms import LoginForm
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


# !******************************************
# ! login from forms,py file #2

# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.warning(request,
#                              f'sorry  {username}  or {password } not exist')

#     else:
#         form = LoginForm()

#     return render(request, 'login.html', {'title': 'login', 'form': form})

# ! logout  #2

# def logout(request):
#     logout(request)
#     return render(request, 'logout.html', context={'title': 'logout'})

# !***************************
#! login  #3
# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.warning(request,
#                              f'sorry  {username}  or {password } not exist')

#     return render(request, 'login.html', {'title': 'login'})