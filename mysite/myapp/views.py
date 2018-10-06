from django.shortcuts import render,redirect
from django.contrib.auth import authenticate

# Create your views here.
from django.http import HttpResponse


def index(request):
    if request.user.is_authenticated:
        return redirect('loggedon')
    return render(request,"myapp/index.html")


def test(request):
    return render(request,"myapp/test.html")