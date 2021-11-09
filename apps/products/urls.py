from django.urls import path
from . import views

name = 'products'
urlpatterns = [
    path("", views.home, name="home"),
    path("category/bathroom/", views.bathroom, name="bathroom"),
    path("category/kitchen/", views.kitchen, name="kitchen"),
    path("category/commercial/", views.commercial, name="commercial"),
    path("category/hardware/", views.hardware, name="hardware"),

    path("closets/", views.closets, name="closets"),
    path("enclosure/", views.enclosure, name="enclosure"),
    path("no-search/", views.noSearch, name="no-search"),
    path("search/", views.search, name="search"),
    path("single-product/", views.singleProduct, name="single-product"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
