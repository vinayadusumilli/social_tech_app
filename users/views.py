from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .form import RegistrationForm

from .models import Profile



def loginUser(request):
    
    state = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')
    
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profiles')
            else:
                messages.error(request, "Username or Password is incorrect")
    context = {'state': state}
    return render(request, 'login-register.html', context=context)
        
def logoutUser(request):
    state = 'login'
    logout(request)
    context = {'state': state}
    return render(request, 'login-register.html', context=context)

def registerUser(request):
    state = 'register'
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, f"{user.username} Account Created")
            login(request, user)
            return redirect('profiles')
    context = {'form':form, 'state': state}
    return render(request, 'login-register.html', context=context)



def AccountUser(request):
    return render(request, 'account.html')

@login_required(login_url='login')
def ProfileView(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'profiles.html', context=context)

@login_required(login_url='login')
def SingleProfileView(request, pk):
    profile = Profile.objects.get(pk=pk)
    topskills = profile.skill_set.exclude(description__exact="")
    otherskills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'topskills':topskills, 'otherskills':otherskills}
    return render(request, 'single-profile.html', context=context)