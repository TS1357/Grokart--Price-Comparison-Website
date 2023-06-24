from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def register_page(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        password1 = request.POST["password1"]

        if password == password1:
            if User.objects.filter(username = username).exists():
                messages.info(request, "Username taken")
                return redirect('accounts/register')
            user = User.objects.create_user(username = username, password = password)
            user.save()
            return render(request, 'login.html')
        else:
            messages.info(request, "Password not matching")
            return redirect('/')

            # if the request is a post request that meets validation then save users data.
    else:  # this means it is a GET request.
        
        return render(request, "register.html")


def login_page(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

    return render(request, "login.html")


def logout_page(request):
    auth.logout(request)
    return redirect("/")
