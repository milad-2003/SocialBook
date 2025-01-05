from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import Profile


def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists!')
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.info(request, 'There is a username with this email!')
            return redirect('signup')
        
        if password != password2:
            messages.info(request, 'Passwords do not match!')
            return redirect('signup')
        
        if len(password) < 8:
            messages.info(request, 'Password should be at least 8 characters!')
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Create a profile object for the new user
        user_model = User.objects.get(username=username)
        user_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        user_profile.save()
        return redirect('signup')

    return render(request, 'signup.html')
