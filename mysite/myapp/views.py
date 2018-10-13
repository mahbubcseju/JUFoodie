from django.shortcuts import render,redirect
from django.contrib.auth import authenticate

# Create your views here.
from django.http import HttpResponse
from .forms import showMenue

def index(request):
    if request.user.is_authenticated:
        return redirect('loggedon')
    return render(request,"myapp/index.html")


def test(request):
    return render(request,"myapp/test.html")

def showmenue(request):
    form = showMenue(request.POST or None,request.FILES or None)
    context = {
        "form": form
    }
    if form.is_valid():
        form.save()
        print('lol')
        return render(request,"myapp/showmenue.html",context)
    return render(request,"myapp/showmenue.html",context)