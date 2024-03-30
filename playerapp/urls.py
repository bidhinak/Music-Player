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
    path("songupdate/<int:id>/", artistviews.songupdate, name="songupdate"),
    # admin artist add section
    path("adminartistadd", adminviews.adminartistadd, name="adminartistadd"),
    path("adminartistlist",adminviews.adminartistlist,name="adminartistlist"),
    path("artistlistdelete/<int:id>/",adminviews.artistlistdelete,name="artistlistdelete"),
    path("adminviewartist", adminviews.adminviewartist, name="adminviewartist"),
    path("adminartistdelete/<int:id>/", adminviews.adminartistdelete, name="adminartistdelete"),
    # adminsongview
    path("adminsongsview/<int:id>/", adminviews.adminsongsview, name="adminsongsview"),
    path("adminsongplay/<int:id>/", adminviews.adminsongplay, name="adminsongplay"),
    path("otherartistsongs", artistviews.otherartistsongs, name="otherartistsongs"),
    # users songs view
    path("userssongsview/<int:id>/", usersviews.userssongsview, name="userssongsview"),
    path("usersongplay/<int:id>/", usersviews.usersongplay, name="usersongplay"),
    path("playbymovies", usersviews.playbymovies, name="playbymovies"),
    # userprofile
    path("userprofile", usersviews.userprofile, name="userprofile"),
    # artistprofile
    path("artistprofile", artistviews.artistprofile, name="artistprofile"),
    # notification
    path("notadd", artistviews.notadd, name="notadd"),
    path("notview", artistviews.notview, name="notview"),
    path("notupdate/<int:id>/", artistviews.notupdate, name="notupdate"),
    path("notdelete/<int:id>/", artistviews.notdelete, name="notdelete"),
    path("usernotview",usersviews.usernotview,name="usernotview"),
    path("adminnotview",adminviews.adminnotview,name="adminnotview")
]
