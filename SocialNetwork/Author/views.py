from django.shortcuts import render
from .models import Author
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect

def login(request):
    return render(request, 'login.html')
    return HttpResponse("your at login page")   


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
