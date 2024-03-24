from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from playerapp.forms import Customform, Usersform
from playerapp.models import Users, songadd, Artist_add


def userssignup(request):
    login_form = Customform()
    signup_form = Usersform()
    if request.method == 'POST':
        login_form = Customform(request.POST)
        signup_form = Usersform(request.POST)
        if login_form.is_valid() and signup_form.is_valid():
            obj1 = login_form.save(commit=False)
            obj1.is_users = True
            obj1.save()
            obj2 = signup_form.save(commit=False)
            obj2.one = obj1
            obj2.save()
            return redirect('loginpage')
    return render(request, 'userstemplate/userssignup.html', {"signup1": login_form, "signup2": signup_form})


def userpage(request):
    viewpage = Artist_add.objects.all()
    return render(request, 'userstemplate/userpage.html', {"viewpage": viewpage})


def userssongsview(request, id):
    uview = songadd.objects.filter(Artist_table=id)
    # print(uview)
    return render(request, 'userstemplate/usersongsview.html', {"view": uview})


def usersongplay(request, id):
    play = songadd.objects.filter(id=id)

    return render(request, 'userstemplate/usersongplay.html', {"play": play})


def playbymovies(request):
    return render(request, 'userstemplate/playbymovies.html')


def userprofile(request):
    u = request.user
    # print(u)
    prof = Users.objects.get(one=u)
    # print(prof)
    return render(request, 'userstemplate/userprofile.html', {"prof": prof})
