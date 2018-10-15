from django.shortcuts import render,redirect
from django.contrib.auth import authenticate

# Create your views here.
from django.http import HttpResponse
from .forms import addMenue,searchMenue
from .models import menue
from custom_user.models import User

def index(request):

    form="guest@gmail.com"
    if request.user.is_authenticated:
        form = request.session['user']

    username = User.objects.get(email=form)
    print(username.full_name)
    print(form)
    context = {
        'form': username
    }
    # return render(request, 'custom_user/loggedin.html', context)
    return render(request,"myapp/index.html",context)


def test(request):
    return render(request,"myapp/test.html")

def addmenue(request):

    form = addMenue(request.POST or None,request.FILES or None)
    context = {
        "form": form
    }
    if form.is_valid():
        form.save()
        print('lol')
        return render(request,"myapp/addmenue.html",context)
    return render(request,"myapp/addmenue.html",context)

def showmenue(request):
    search = searchMenue(request.POST or None)
    form = menue.objects.all()
    context={
        "form":form,
        "search":search
    }
    return render(request,"myapp/showmenue.html",context)


def ordermenue(request,id):
    print(id)

    return redirect('showmenue')
