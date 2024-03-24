from django import forms
from django.contrib.auth.forms import UserCreationForm

from playerapp.models import Login, Users, Artist_Table, songadd, Artist_add


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


class artistaddform(forms.ModelForm):
    class Meta:
        model = Artist_add
        fields = "__all__"
