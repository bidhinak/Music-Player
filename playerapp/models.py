from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import DO_NOTHING


# Create your models here.
class Login(AbstractUser):
    is_artist = models.BooleanField(default=False)
    is_users = models.BooleanField(default=False)


class Users(models.Model):
    one = models.ForeignKey(Login, on_delete=models.CASCADE)
    your_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_no = models.CharField(max_length=10)


class Artist_Table(models.Model):
    two = models.ForeignKey(Login, on_delete=models.CASCADE)
    artist_name = models.CharField(max_length=30)
    artist_image = models.ImageField(upload_to="images/")
    phone_no = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.artist_name


class Artist_add(models.Model):
    name = models.ForeignKey(Artist_Table, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="artistimage/")

    def __str__(self):
        return str(self.name)


class songadd(models.Model):
    song_name = models.CharField(max_length=30)
    song_artist = models.ForeignKey(Artist_add, on_delete=models.CASCADE)
    song_singers = models.CharField(max_length=50)
    song_movie = models.CharField(max_length=30)
    song_image = models.ImageField(upload_to="images/")
    song = models.FileField(upload_to="songs/")


class notification(models.Model):
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(Login, on_delete=DO_NOTHING)
    description = models.TextField()
