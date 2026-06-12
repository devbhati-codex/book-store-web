from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout



def register_view(request):

    if request.method == 'POST':
        print("POST Request Received")

        form = RegisterForm(request.POST)

        if form.is_valid():
            print("Form Valid")

            user = form.save()
            print("User Saved:", user.username)

            login(request, user)

            return redirect('home')

        else:
            print(form.errors)

    else:
        form = RegisterForm()

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )

def login_view(request):

    if request.method == 'POST':

        form =  LoginForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect('home')

    else:
        form =  LoginForm()

    return render(
        request,
        'accounts/login.html',
        {'form': form}
    )

   


def logout_view(request):

    logout(request)

    return redirect('home')