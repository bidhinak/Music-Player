from django.contrib import messages
from django.shortcuts import render, redirect

from playerapp.forms import Artistform, artist_addform
from playerapp.models import songadd, Artist_Table, Artist_add, notification


# def adminartistadd(request, id):
#     data = Artist_Table.objects.get(id=id)
#     u = Artist_add.objects.filter(name=data)
#     if u.exists():
#         messages.info(request, 'This artist is already on the list')
#         return redirect('artistview')
#     else:
#         add = artist_addform()
#         if request.method == 'POST':
#             add = artist_addform(request.POST, request.FILES)
#             if add.is_valid():
#                 add.save()
#             return redirect('adminartistlist')
#     return render(request, 'admintemplate/adminartistadd.html', {"add": add})


def adminartistadd(request, id):
    add = Artist_Table.objects.get(id=id)
    z = Artist_add.objects.filter(name=add)
    if z.exists():
        messages.info(request, 'You have already added this song')
        return redirect('#')
    else:
        if request.method == 'POST':
            v = artist_addform()
            v.name = add
            v.save()
            return redirect('adminartistlist')
    return render(request, 'admintemplate/adminartistadd.html', {"add": add})


def adminartistlist(request):
    show = Artist_add.objects.all()
    return render(request, 'admintemplate/adminartistlist.html', {"show": show})


def artistlistdelete(request, id):
    delt = Artist_add.objects.get(id=id)
    delt.delete()
    return redirect('adminartistlist')


def adminpage(request):
    return render(request, 'admintemplate/adminpage.html')


def artistview(request):
    view = Artist_Table.objects.all()
    return render(request, 'admintemplate/artistview.html', {"view": view})


def adminviewartist(request):
    view = Artist_Table.objects.all()
    return render(request, 'admintemplate/adminartistview.html', {"view": view})


def adminartistdelete(request, id):
    delt = Artist_Table.objects.get(id=id)
    delt.delete()
    return redirect('adminviewartist')


def adminsongsview(request, id):
    view = songadd.objects.filter(song_artist=id)

    return render(request, 'admintemplate/adminsongsview.html', {"view": view})


def adminsongplay(request, id):
    play = songadd.objects.filter(id=id)
    return render(request, 'admintemplate/adminsongplay.html', {"play": play})


def adminsongdelete(request, id):
    delt = songadd.objects.filter(id=id)
    delt.delete()
    return redirect('adminartistlist')


def adminnotview(request):
    view = notification.objects.all()
    return render(request, 'admintemplate/adminnotview.html', {"view": view})
