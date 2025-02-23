from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Profile, Post, LikePost, FollowUser


@login_required(login_url='signin')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    posts = Post.objects.all()
    return render(request, 'index.html', {'user_profile': user_profile, 'posts': posts})

@login_required(login_url='signin')
def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    post = Post.objects.get(id=post_id)

    if like_filter:
        like_filter.delete()
        post.no_of_likes -= 1
        post.save()

        return redirect('/')
    else:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes += 1
        post.save()

        return redirect('/')

@login_required(login_url='signin')
def follow_user(request):
    if request.method == 'POST':
        user = get_object_or_404(User, username=request.POST['user'])
        follower = get_object_or_404(User, username=request.POST['follower'])
        user_object = get_object_or_404(Profile, user=user)
        follower_object = get_object_or_404(Profile, user=follower)

        if FollowUser.objects.filter(user=user_object, follower=follower_object):
            delete_follower = FollowUser.objects.get(user=user_object, follower=follower_object)
            delete_follower.delete()
            
            return redirect('/profile/' + request.POST['user'])
        
        else:
            new_follower = FollowUser.objects.create(user=user_object, follower=follower_object)
            new_follower.save()

            return redirect('/profile/' + request.POST['user'])
        
    else:
        return redirect('/')
    
def format_count(count, label):
    if count == 1:
        return f"{count} {label}"
    elif count < 2000:
        return f"{count} {label}s"
    elif count < 1000000:
        return f"{count / 1000:.1f}K {label}s"
    else:
        return f"{count / 1000000:.1f}M {label}s"

@login_required(login_url='signin')
def profile(request, pk):
    user_object = get_object_or_404(User, username=pk)
    user_profile = get_object_or_404(Profile, user=user_object)
    user_posts = Post.objects.filter(user=user_profile)
    user_posts_count = len(user_posts)

    follower = get_object_or_404(Profile, user=request.user)

    button_text = 'Unfollow' if FollowUser.objects.filter(user=user_profile, follower=follower).first() else 'Follow'

    follower_count = len(FollowUser.objects.filter(user=user_profile))
    following_count = len(FollowUser.objects.filter(follower=user_profile))

    follower_count_display = format_count(follower_count, "Follower")
    following_count_display = format_count(following_count, "Following")


    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_posts_count': user_posts_count,
        'button_text': button_text,
        'follower_count_display': follower_count_display,
        'following_count_display': following_count_display
    }

    return render(request, 'profile.html', context)

@login_required(login_url='signin')
def upload(request):
    if request.method == 'POST':
        user = get_object_or_404(Profile, user=request.user)
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()

        return redirect('/')
    else:
        return redirect('/')

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
