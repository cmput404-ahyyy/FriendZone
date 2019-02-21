from django.shortcuts import render
from .models import Author
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.


def login(request):
    return render(request, 'author/login.html')
    pass


def index(request):
    pass

def register(request):
    pass

def profile(request):
    pass

def logout(request):
    pass

def notifications(request):
    pass
