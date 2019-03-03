from django.shortcuts import render
from .models import Author
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.


def login(request):
    return render(request, 'login.html')

def homepage(request, auth_id):
    print(auth_id)
    return render(request, 'homepage.html')

def index(request):
    return redirect('login/')

def home(request):
    pass

def register(request):
    pass

def profile(request):
    pass

def logout(request):
    pass

def notifications(request):
    pass

