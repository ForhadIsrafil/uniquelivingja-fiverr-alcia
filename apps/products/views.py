from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, get_query, get_or_create_customer, send_contact_email
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.template import RequestContext
from django.utils import timezone


def home(request):
    # todo: product start (FEATRED PRODUCTS)
    products = Product.objects.all().order_by('-id')
    # todo: product end

    # todo: sliders start
    first_slider = HomeSlider.objects.all()[0]
    sliders = HomeSlider.objects.all()[1:]
    # todo: sliders end

    return render(request, 'home.html', {'sliders': sliders, 'first_slider': first_slider, })


def bathroom(request):
    return render(request, 'bathroom.html')


def kitchen(request):
    return render(request, 'kitchen.html')


def commercial(request):
    return render(request, 'commercial.html')


def hardware(request):
    return render(request, 'hardware.html')


def closets(request):
    return render(request, 'closet.html')


def enclosure(request):
    return render(request, 'enclosure.html')


def noSearch(request):
    return render(request, 'no-search-result.html')


def search(request):
    return render(request, 'search.html')


def singleProduct(request):
    return render(request, 'singleProduct.html')


def search(request):
    data = cartData(request)
    cartItems = data["cartItems"]
    order = data["order"]
    items = data["items"]

    query_string = ""
    found_entries = None
    query_string = request.GET["query"]

    entry_query = get_query(
        query_string,
        ["name", "brand"],
    )
    products = Product.objects.filter(entry_query).order_by('-id')

    paginator = Paginator(products, 25)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "query_string": query_string,
        "products": products,
        "cartItems": cartItems,
        "page_obj": page_obj,
    }
    if products:
        return render(request, "store/store.html", context)
    else:
        return render(request, "store/nosearchresults.html")


def about(request):
    return render(request, 'about.html')


from django.contrib import messages


def contact(request):
    if request.POST:
        send_contact = send_contact_email(request)
        if send_contact:
            messages.error(
                request,
                "Thanks for your message. We will contact with sortly.",
            )
            return render(request, 'contact.html')
        else:
            messages.error(
                request,
                "Something wrong. please try again.",
            )
            return render(request, 'contact.html')
    return render(request, 'contact.html')
