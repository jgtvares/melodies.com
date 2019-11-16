from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, request

import jinja2

# Create your views here.
def home(request):
    return render(request, 'website/home.html')