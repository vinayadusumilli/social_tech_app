from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile



def loginUser(request):
    
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
    return render(request, 'login-register.html')
        
def logoutUser(request):
    logout(request)
    print("logout done")
    return render(request, 'login-register.html')
    




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