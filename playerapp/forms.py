from django import forms
from django.contrib.auth.forms import UserCreationForm

from playerapp.models import Login, Users, Artist_Table, songadd, notification, Artist_add, playlist, playlistadd, \
    movieplaylist, movieplaylistadd


class Customform(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ("username", "password1", "password2")


class Usersform(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"
        exclude = ("one",)


class Artistform(forms.ModelForm):
    class Meta:
        model = Artist_Table
        fields = "__all__"
        exclude = ("two",)


class songaddform(forms.ModelForm):
    class Meta:
        model = songadd
        fields = "__all__"


class notificationform(forms.ModelForm):
    class Meta:
        model = notification
        fields = ('description',)


class artist_addform(forms.ModelForm):
    class Meta:
        model = Artist_add
        fields = "__all__"




class playlistform(forms.ModelForm):
    class Meta:
        model = playlist
        fields = "__all__"
        exclude=('user',)


class playlistaddform(forms.ModelForm):
    class Meta:
        model = playlistadd
        fields = "__all__"
        exclude = ('song1','user')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['playlist_name'].queryset = playlist.objects.filter(user=user)

class movieplaylistform(forms.ModelForm):
    class Meta:
        model=movieplaylist
        fields="__all__"
        exclude=('artist',)

class movieplaylistaddform(forms.ModelForm):
    class Meta:
        model=movieplaylistadd
        fields="__all__"
        exclude=('artist','song2')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('artist', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['mplaylist_name'].queryset = movieplaylist.objects.filter(artist=user)
