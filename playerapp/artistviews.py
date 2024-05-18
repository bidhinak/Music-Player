from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from playerapp.forms import Customform, Artistform, songaddform, notificationform, movieplaylistform, \
    movieplaylistaddform
from playerapp.models import songadd, Artist_Table, notification, Artist_add, movieplaylist, movieplaylistadd


def artistpage(request):
    view = songadd.objects.all()

    return render(request, 'artisttemplate/artistpage.html', {"view": view})


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


@login_required(login_url='/Alogout_view/')
def artistaddsong(request):
    view = songaddform()
    if request.method == "POST":
        view = songaddform(request.POST, request.FILES)
        if view.is_valid():
            view.save()
            return redirect('artistsongview')
    return render(request, 'artisttemplate/addsong.html', {"view": view})


@login_required(login_url='/Alogout_view/')
def artistsongview(request):
    show = songadd.objects.all()
    # view=Artist_add.objects.all()
    # list=zip(show,view)
    return render(request, 'artisttemplate/songsview.html', {"show": show})


@login_required(login_url='/Alogout_view/')
def otherartists(request):
    view = Artist_add.objects.all()
    return render(request, 'artisttemplate/otherartists.html', {"view": view})


@login_required(login_url='/Alogout_view/')
def otherartistsongs(request, id):
    show = songadd.objects.filter(song_artist=id)
    return render(request, 'artisttemplate/otherartistsongs.html', {"show": show})


@login_required(login_url='/Alogout_view/')
def otherartistsongplay(request, id):
    play = songadd.objects.filter(id=id)
    return render(request, 'artisttemplate/otherartistsongplay.html', {"play": play})


@login_required(login_url='/Alogout_view/')
def songdelete(request, id):
    delt = songadd.objects.get(id=id)
    delt.delete()
    return redirect('artistsongview')


@login_required(login_url='/Alogout_view/')
def songupdate(request, id):
    show = songadd.objects.get(id=id)
    upd = songaddform(instance=show)
    if request.method == 'POST':
        upd = songaddform(request.POST, instance=show)
        if upd.is_valid():
            upd.save()
            return redirect('artistsongview')
    return render(request, 'artisttemplate/songupdate.html', {"upd": upd})


@login_required(login_url='/Alogout_view/')
def artistprofile(request):
    u = request.user
    prof = Artist_Table.objects.get(two=u)
    return render(request, 'artisttemplate/artistprofile.html', {"prof": prof})


@login_required(login_url='/Alogout_view/')
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


@login_required(login_url='/Alogout_view/')
def notview(request):
    u = request.user.id
    view = notification.objects.filter(user=u)
    return render(request, 'artisttemplate/notview.html', {"view": view})


@login_required(login_url='/Alogout_view/')
def notupdate(request, id):
    nget = notification.objects.get(id=id)
    up = notificationform(instance=nget)
    if request.method == 'POST':
        up = notificationform(request.POST, instance=nget)
        if up.is_valid():
            up.save()
            return redirect('notview')
    return render(request, 'artisttemplate/notupdate.html', {"up": up})


@login_required(login_url='/Alogout_view/')
def notdelete(request, id):
    delt = notification.objects.get(id=id)
    delt.delete()
    messages.info(request, 'Notification deleted successfully')
    return redirect('notview')


@login_required(login_url='/Alogout_view/')
def movieplaylistcreate(request):
    create = movieplaylistform()
    u = request.user
    if request.method == 'POST':
        create = movieplaylistform(request.POST, request.FILES)
        if create.is_valid():
            data = create.save(commit=False)
            data.artist = u
            create.save()
            messages.info(request, 'New movie playlist created successfully')
    return render(request, 'artisttemplate/movieplaylistcreate.html', {"create": create})


@login_required(login_url='/Alogout_view/')
def movieplaylistview(request):
    u = request.user
    view = movieplaylist.objects.filter(artist=u)
    return render(request, 'artisttemplate/movieplaylistview.html', {"view": view})


@login_required(login_url='/Alogout_view/')
def movieplaylistdelete(request, id):
    delt = movieplaylist.objects.get(id=id)
    delt.delete()
    return redirect('movieplaylistview')


# def songaddtomplaylist(request, id):
#     data = songadd.objects.get(id=id)
#     print(data)
#     # u = request.user
#     # print(u)
#     # z = movieplaylist.objects.filter(artist=u)
#     # print(z)
#     add = movieplaylistaddform()
#     if request.method == 'POST':
#         add = movieplaylistaddform(request.POST)
#         if add.exists():
#             messages.info(request, 'you have already added this song')
#             return redirect('#')
#         else:
#             if add.is_valid():
#                 v = add.save(commit=False)
#                 v.song2 = data
#                 add.save()
#                 messages.info(request, 'Song added successfully')
#
#     return render(request, 'artisttemplate/mplaylistadd.html', {"add": add})
@login_required(login_url='/Alogout_view/')
def songaddtomplaylist(request, id):
    data = songadd.objects.get(id=id)
    # u = request.user
    # v = Artist_Table.objects.get(two=u)
    z = movieplaylistadd.objects.filter(song2=data)
    if z.exists():
        messages.info(request, 'You have already added this song')
        return redirect('artistsongview')
    else:
        add = movieplaylistaddform(artist=request.user)
        if request.method == 'POST':
            add = movieplaylistaddform(request.POST, artist=request.user)
            if add.is_valid():
                v = add.save(commit=False)
                v.song2 = data
                add.save()
                messages.info(request, 'Song added successfully')

    return render(request, 'artisttemplate/mplaylistadd.html', {"add": add})


@login_required(login_url='/Alogout_view/')
def mplaylistsongsview(request, id):
    view = movieplaylistadd.objects.filter(mplaylist_name=id)
    return render(request, 'artisttemplate/mplaylistsongsview.html', {"view": view})


@login_required(login_url='/Alogout_view/')
def artistmsongplay(request, id):
    play = movieplaylistadd.objects.filter(id=id)
    # print(play)
    return render(request, 'artisttemplate/artistmsongplay.html', {"play": play})


@login_required(login_url='/Alogout_view/')
def mplaylistsongdelete(request, id):
    delt = movieplaylistadd.objects.get(id=id)
    delt.delete()
    return redirect('movieplaylistview')


# def search(request):
#     if request.method == 'GET': # this will be GET now
#         show =  request.GET.get('search') # do some research what it does
#         try:
#             status = songadd.objects.filter(song_name=show)
#         except songadd.DoesNotExist:
#             status=None
#         return render(request,"artisttemplate/search.html",{"status":status})
#     else:
#         return render(request,"artisttemplate/search.html",{})
@login_required(login_url='/Alogout_view/')
def searchartist(request):
    if request.GET.get('myform'):  # write your form name here
        item = request.GET.get('myform')
        try:
            status = songadd.objects.filter(song_name__icontains=item)
            return render(request, "artisttemplate/artistsearch.html", {"view": status})
        except:
            return render(request, "artisttemplate/artistsearch.html")
    else:
        return render(request, 'artisttemplate/artistsearch.html')
