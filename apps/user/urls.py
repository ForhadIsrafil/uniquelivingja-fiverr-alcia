from django.urls import path
from . import views

name = 'user'
urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout, name="logout"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

]
