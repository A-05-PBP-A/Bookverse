from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def show_landing(request):
    if 'last_login' not in request.COOKIES.keys():
        return redirect('authentication:login_user')
    context = {'name': request.user.username,
            'last_login': request.COOKIES['last_login'],
            }
    return render(request, "landing_page.html", context)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Get the value of 'is_Admin' from request.POST
            is_admin = request.POST.get('is_Admin', False)
            if is_admin:
                user.is_Admin = True
            else:
                user.is_User = True
            user.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('authentication:login_user')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("authentication:show_landing")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('daftar_buku:show_main'))
    response.delete_cookie('last_login')
    return response