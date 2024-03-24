from django.contrib.auth.models import AbstractUser
from django.db import models


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
    phone_no = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.artist_name


#
class songadd(models.Model):
    song_name = models.CharField(max_length=30)
    song_artist = models.ForeignKey(Artist_Table, on_delete=models.CASCADE)
    song_singers = models.CharField(max_length=50)
    song_movie = models.CharField(max_length=30)
    song_image = models.ImageField(upload_to="images/")
    song = models.FileField(upload_to="songs/")


class Artist_add(models.Model):
    artist_image = models.ImageField(upload_to="images/")
    artist_name = models.ForeignKey(Artist_Table, on_delete=models.CASCADE)
