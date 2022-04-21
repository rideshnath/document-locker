from django.urls import path
from .import views
urlpatterns = [
    path("index", views.index, name="index"),
    path("", views.home, name="home"),
    path("login/", views.Login, name="login"),
    path("signup/",views.SignUp,name="signup"),
    path("folder/<int:folderid>/",views.folder, name="folder"),
    path("addFolder/", views.addfolder, name="addfolder"),
    path("logout/", views.Logout, name="logout"),
    path("reduce/", views.reduce, name="reduce"),

]
