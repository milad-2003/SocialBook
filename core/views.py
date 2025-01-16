from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import Profile


@login_required(login_url='signin')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':

        image = request.FILES.get('image')
        if not image:
            image = user_profile.profileimg

        bio = request.POST['bio']
        location = request.POST['location']

        user_profile.profileimg = image
        user_profile.bio = bio
        user_profile.location = location
        user_profile.save()

        return redirect('settings')

    return render(request, 'settings.html', {'user_profile': user_profile})

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

        # Login the user
        user_login = auth.authenticate(username=username, password=password)
        auth.login(request, user_login)

        # Create a profile object for the new user and redirect to the settings page
        user_model = User.objects.get(username=username)
        user_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        user_profile.save()
        return redirect('settings')

    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        
        messages.info(request, "Can't login with the given credentials!")
        return redirect('signin')

    return render(request, 'signin.html')

@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')
