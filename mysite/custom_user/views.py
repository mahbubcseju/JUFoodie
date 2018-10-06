from django.contrib.auth import authenticate, login, get_user_model,logout
from django.views.generic import CreateView, FormView
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url


from .forms import LoginForm, RegisterForm

User = get_user_model()
def register(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        form.save()
        return redirect('login')
    # print("lol")
    return render(request, 'custom_user/register.html', context)

def loginv(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        username  = form.cleaned_data.get("email")
        password  = form.cleaned_data.get("password")
        # print(username)
        # print(password)
        user = authenticate(request, username=username, password=password)
        # print(user)
        if user is not None:
            login(request, user)
            request.session['user'] = user
            return redirect('loggedon')
        else:
            # Return an 'invalid login' error message.
            print("Error lol")
    return render(request, "custom_user/login.html", context)

def loggedon(request):
    form=request.session['user']
    username=User.objects.get(email=form)
    print(username.full_name)
    print(form)
    context={
        'form': username
    }
    return render(request,'custom_user/loggedin.html',context)

def logoutc(request):
    # logout(request)
    if request.user.is_authenticated:
        print(request.session['user'])

    del request.session['user']
    logout(request)
    # if request.session['user']==None:
    #     print('lol')
    return redirect('index')
