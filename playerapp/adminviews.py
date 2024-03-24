from django.shortcuts import render, redirect

from playerapp.forms import artistaddform
from playerapp.models import Artist_add, songadd


# from playerapp.forms import artistaddform
# from playerapp.models import artistadd, songadd


def adminaddartist(request):
    add = artistaddform()
    if request.method == 'POST':
        add = artistaddform(request.POST, request.FILES)
        if add.is_valid():
            add.save()
            return redirect('adminviewartist')
    return render(request, 'admintemplate/artistadd.html', {"add": add})


def adminviewartist(request):
    view = Artist_add.objects.all()
    return render(request, 'admintemplate/artistview.html', {"view": view})

def artistdelete(request,id):
    delt=Artist_add.objects.get(id=id)
    delt.delete()
    return redirect('adminviewartist')


def adminsongsview(request):
    view = songadd.objects.all()
    return render(request, 'admintemplate/adminsongsview.html', {"view": view})


def adminsongplay(request,id):
    play = songadd.objects.filter(id=id)
    return render(request, 'admintemplate/adminsongplay.html', {"play": play})
