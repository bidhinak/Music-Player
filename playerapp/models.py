from email.policy import default

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
    DoesNotExist = None
    song_name = models.CharField(max_length=30)
    song_artist = models.ForeignKey(Artist_add, on_delete=models.CASCADE)
    song_singers = models.CharField(max_length=100)
    song_image = models.ImageField(upload_to="images/")
    song = models.FileField(upload_to="songs/")

    def __str__(self):
        return self.song_name


class notification(models.Model):
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(Login, on_delete=DO_NOTHING)
    description = models.TextField()


class playlist(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="playlist/", default="playlist/default.png", blank=True)

    def __str__(self):
        return str(self.name)


class playlistadd(models.Model):
    song1 = models.ForeignKey(songadd, on_delete=models.CASCADE)
    playlist_name = models.ForeignKey(playlist, on_delete=models.CASCADE)


class movieplaylist(models.Model):
    artist = models.ForeignKey(Login, on_delete=models.CASCADE)
    movie_name = models.CharField(max_length=150)
    movie_image = models.ImageField(upload_to="movies/")

    def __str__(self):
        return str(self.movie_name)


class movieplaylistadd(models.Model):
    song2 = models.ForeignKey(songadd, on_delete=models.CASCADE)
    mplaylist_name = models.ForeignKey(movieplaylist, on_delete=models.CASCADE)
