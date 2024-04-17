from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from playerapp.forms import Customform, Usersform, playlistform, playlistaddform, songaddform
from playerapp.models import Users, songadd, notification, Artist_add, playlist, playlistadd, movieplaylist, \
    movieplaylistadd


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
    view = Artist_add.objects.all()
    return render(request, 'userstemplate/userpage.html', {"view": view})


def userssongsview(request, id):
    uview = songadd.objects.filter(song_artist=id)

    return render(request, 'userstemplate/usersongsview.html', {"view": uview})


def usersongplay(request, id):
    play = songadd.objects.filter(id=id)

    return render(request, 'userstemplate/usersongplay.html', {"play": play})


def playbymovies(request):
    view=movieplaylist.objects.all()
    return render(request, 'userstemplate/playbymovies.html',{"view":view})


def userprofile(request):
    u = request.user
    # print(u)
    prof = Users.objects.get(one=u)
    # print(prof)
    return render(request, 'userstemplate/userprofile.html', {"prof": prof})


def usernotview(request):
    view = notification.objects.all()
    return render(request, 'userstemplate/usernotview.html', {"view": view})


def userplaylistcreate(request):
    create = playlistform()
    u = request.user
    if request.method == 'POST':
        create = playlistform(request.POST, request.FILES)
        if create.is_valid():
            data = create.save(commit=False)
            data.user = u
            create.save()
            return redirect('userplaylistview')
    return render(request, 'userstemplate/playlistcreate.html', {"create": create})


def userplaylistview(request):
    u = request.user
    view = playlist.objects.filter(user=u)
    return render(request, 'userstemplate/playlistview.html', {"view": view})


def userplaylistdelete(request, id):
    delt = playlist.objects.get(id=id)
    delt.delete()
    return redirect('userplaylistview')


def userplaylistadd(request, id):
    data = songadd.objects.get(id=id)
    u = request.user
    print(u)
    z = playlist.objects.filter(user=u)
    print(z)
    add = playlistaddform()
    if request.method == 'POST':
        add= playlistaddform(request.POST)
        if add.is_valid():
            v = add.save(commit=False)
            v.song1 = data
            add.save()
            messages.info(request, 'Song added successfully')

    return render(request, 'userstemplate/playlistadd.html', {"add": add})


def userplaylistsongsview(request, id):
    view = playlistadd.objects.filter(playlist_name=id)
    print(view)
    return render(request, 'userstemplate/playlistsongsview.html', {"view": view})

def userplaylistsongplay(request,id):
    # view=playlistadd.objects.filter(song1=id)
    # print(view)
    play=playlistadd.objects.filter(id=id)
    print(play)
    return render(request,'userstemplate/userplaylistsongplay.html',{"play":play})


def playlistsongdelete(request, id):
    delt = playlistadd.objects.get(id=id)
    delt.delete()
    return redirect('userplaylistview')
def usersmplaylist(request,id):
    view=movieplaylistadd.objects.filter(mplaylist_name=id)
    return render(request,'userstemplate/usersmplaylist.html',{"view":view})

def usermsongplay(request,id):

    play=movieplaylistadd.objects.filter(id=id)
    # print(play)
    return render(request,'userstemplate/usermsongplay.html',{"play":play})