from django.contrib import messages
from django.shortcuts import render, redirect

from playerapp.forms import Customform, Artistform, songaddform, notificationform
from playerapp.models import songadd, Artist_Table, notification, Artist_add


def artistpage(request):
    return render(request, 'artisttemplate/artistpage.html')


def artistsignup(request):
    login_form = Customform()
    signup_form = Artistform()
    if request.method == 'POST':
        login_form = Customform(request.POST)
        signup_form = Artistform(request.POST, request.FILES)
        if login_form.is_valid() and signup_form.is_valid():
            obj1 = login_form.save(commit=False)
            obj1.is_artist = True
            obj1.save()
            obj2 = signup_form.save(commit=False)
            obj2.two = obj1
            obj2.save()
            return redirect('aloginpage')
    return render(request, 'artisttemplate/asignup.html', {"signup1": login_form, "signup2": signup_form})


def aloginpage(request):
    return render(request, 'artisttemplate/aloginpage.html')


def artistaddsong(request):
    view = songaddform()
    if request.method == "POST":
        view = songaddform(request.POST, request.FILES)
        if view.is_valid():
            view.save()
            return redirect('artistsongview')
    return render(request, 'artisttemplate/addsong.html', {"view": view})


def artistsongview(request):
    show = songadd.objects.all()
    # view=Artist_add.objects.all()
    # list=zip(show,view)
    return render(request, 'artisttemplate/songsview.html', {"show": show})


def otherartistsongs(request):
    show = songadd.objects.all()
    return render(request, 'artisttemplate/otherartistsongs.html', {"show": show})


def songdelete(request, id):
    delt = songadd.objects.get(id=id)
    delt.delete()
    return redirect('artistsongview')


def songupdate(request, id):
    show = songadd.objects.get(id=id)
    upd = songaddform(instance=show)
    if request.method == 'POST':
        upd = songaddform(request.POST, instance=show)
        if upd.is_valid():
            upd.save()
            return redirect('artistsongview')
    return render(request, 'artisttemplate/songupdate.html', {"upd": upd})


def artistprofile(request):
    u = request.user
    prof = Artist_Table.objects.get(two=u)
    return render(request, 'artisttemplate/artistprofile.html', {"prof": prof})


def notadd(request):
    add = notificationform()
    user1 = request.user
    if request.method == 'POST':
        add = notificationform(request.POST)
        if add.is_valid():
            data = add.save(commit=False)
            data.user = user1
            add.save()
            messages.info(request, 'notification added successfully')
            return redirect('notadd')
    return render(request, 'artisttemplate/notadd.html', {"add": add})


def notview(request):
    u = request.user.id
    view = notification.objects.filter(user=u)
    return render(request, 'artisttemplate/notview.html', {"view": view})

def notupdate(request,id):
    nget=notification.objects.get(id=id)
    up=notificationform(instance=nget)
    if request.method == 'POST':
        up=notificationform(request.POST,instance=nget)
        if up.is_valid():
            up.save()
            return redirect('notview')
    return render(request,'artisttemplate/notupdate.html',{"up":up})

def notdelete(request,id):
    delt=notification.objects.get(id=id)
    delt.delete()
    messages.info(request, 'notification deleted successfully')
    return redirect('notview')