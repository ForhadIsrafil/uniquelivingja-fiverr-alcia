from django.urls import path
from . import views

name = 'product'
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("bathroom/", views.bathroom, name="bathroom"),
    path("closet/", views.closet, name="closet"),
    path("enclosure/", views.enclosure, name="enclosure"),
    path("hardware/", views.hardware, name="hardware"),
    path("no-search/", views.noSearch, name="no-search"),
    path("search/", views.search, name="search"),
    path("single-product/", views.singleProduct, name="single-product"),

]
