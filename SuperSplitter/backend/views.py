from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as DjangoUser
from .forms import CustomUserCreationForm


def registerUser(request):
    form = CustomUserCreationForm
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'User account was created!')
            login(request, user)
            return redirect('home')

    context = {'form': form}
    return render(request, 'backend/login_register.html', context)


def profiles(request):
    user_profiles = User.objects.all()
    context = {'profiles': user_profiles}
    return render(request, 'backend/profiles.html', context)


def user_profile(request, pk):
    profile = User.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'backend/user_profile.html', context)