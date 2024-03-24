from django.urls import path

from playerapp import views, usersviews, artistviews, adminviews

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("loginpage", views.loginpage, name="loginpage"),
    path("Login_view", views.Login_view, name="Login_view"),
    path("Aloginview", views.Aloginview, name="Aloginview"),
    path("userssignup", usersviews.userssignup, name="userssignup"),
    path("userpage", usersviews.userpage, name="userpage"),
    path("adminpage", views.adminpage, name="adminpage"),
    path("artistpage", artistviews.artistpage, name="artistpage"),
    path("aloginpage", artistviews.aloginpage, name="aloginpage"),
    path("artistsignup", artistviews.artistsignup, name="artistsignup"),
    #     artist  song section
    path("artistaddsong", artistviews.artistaddsong, name="artistaddsong"),
    path("artistsongview", artistviews.artistsongview, name="artistsongview"),
    path("songdelete/<int:id>", artistviews.songdelete, name="songdelete"),
    path("songupdate/<int:id>/",artistviews.songupdate,name="songupdate"),
    # admin artist add section
    path("adminaddartist", adminviews.adminaddartist, name="adminaddartist"),
    path("adminviewartist", adminviews.adminviewartist, name="adminviewartist"),
    path("artistdelete/<int:id>/",adminviews.artistdelete,name="artistdelete"),
    # adminsongview
    path("adminsongsview", adminviews.adminsongsview, name="adminsongsview"),
    path("adminsongplay/<int:id>/", adminviews.adminsongplay, name="adminsongplay"),
    path("otherartistsongs",artistviews.otherartistsongs,name="otherartistsongs"),
    # users songs view
    path("userssongsview/<int:id>/", usersviews.userssongsview, name="userssongsview"),
    path("usersongplay/<int:id>/",usersviews.usersongplay,name="usersongplay"),
    path("playbymovies",usersviews.playbymovies,name="playbymovies"),
    #userprofile
    path("userprofile",usersviews.userprofile,name="userprofile"),
    # artistprofile
    path("artistprofile",artistviews.artistprofile,name="artistprofile")
]
