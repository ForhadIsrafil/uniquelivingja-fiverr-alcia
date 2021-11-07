from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, get_query, get_or_create_customer, send_order_email
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.template import RequestContext
from django.utils import timezone


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
