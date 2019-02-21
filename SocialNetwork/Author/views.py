from django.shortcuts import render
from .models import Author
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    return render(request, 'author/login.html')


def index(request):
    return render(request,'<h1>logged In</h1>')

def register(request):
    pass

def profile(request):
    pass

def logout(request):
    pass

def notifications(request):
    pass
