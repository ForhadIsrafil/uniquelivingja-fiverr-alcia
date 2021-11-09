from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import UniUser as User

def login_view(request):
    if request.user.is_authenticated:
        return redirect('store')
    elif request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        url = request.POST["url"]

        user = authenticate(request, username=username, password=password)
        # user = User.objects.get(username=username)
        if user is not None:
        # if user.check_password(raw_password=password):
            login(request, user)
            try:
                next_url = url.split('=')[1]
                return HttpResponseRedirect(next_url)
            except Exception as e:
                return redirect('store')
        else:
            messages.error(
                request,
                "Please use correct credential to login.",
            )
            return render(request, 'users/login.html')
    else:
        return render(request, 'users/login.html')

@login_required
def logout(request):
    # logout(request)
    request.session.flush()
    return redirect('login')



