from django.shortcuts import render, redirect

from playerapp.forms import Customform, Artistform, songaddform
from playerapp.models import songadd, Artist_Table


def artistpage(request):
    return render(request, 'artisttemplate/artistpage.html')


def artistsignup(request):
    login_form = Customform()
    signup_form = Artistform()
    if request.method == 'POST':
        login_form = Customform(request.POST)
        signup_form = Artistform(request.POST)
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
    return render(request,'artisttemplate/songupdate.html', {"upd": upd})


def artistprofile(request):
    u = request.user
    prof = Artist_Table.objects.get(two=u)
    return render(request, 'artisttemplate/artistprofile.html', {"prof": prof})
