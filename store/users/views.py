from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth
from django.urls import reverse
from users.models import User

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    
    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    
    context = {'form': form}
    return render(request, 'users/register.html', context)



def profile(request):
    if request.method == "POST":
        form = UserProfileForm(isinstance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return 
        else:
            return form.add_error()
    return render(request, 'users/profile.html')