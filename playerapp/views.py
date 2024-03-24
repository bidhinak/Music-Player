from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from playerapp.forms import Customform, Usersform
from playerapp.models import Users


# Create your views here.
def homepage(request):
    return render(request, 'index.html')


def loginpage(request):
    return render(request, 'loginpage.html')


def Login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('adminpage')
            elif user.is_users:
                return redirect('userpage')

        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'loginpage.html')


def Aloginview(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_artist:
                return redirect('artistpage')
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'artisttemplate/aloginpage.html')


def adminpage(request):
    return render(request, 'admintemplate/adminpage.html')
