from django.urls import path
from . import views

name = 'user'
urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout, name="logout"),
]
