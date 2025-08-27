# Import all Basic Necessary Libraries
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, TweetForm, ProfileForm
from .models import Tweet, Profile


# Homepage / Feed (All Tweets Show Here)
def index(request):
    # Show all tweets in the main feed
    tweets = Tweet.objects.select_related('author__profile').all()
    return render(request, 'tweetapp/index.html', {'tweets': tweets})


# Register View
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = user.profile   # get profile created by signal
            profile.image = profile_form.cleaned_data.get('image')
            profile.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
        else:
            messages.warning(request, "⚠️ Username already exists or invalid details.")
    else:
        form = UserRegistrationForm()
        profile_form = ProfileForm()

    return render(request, 'tweetapp/register.html', {
        'form': form,
        'profile_form': profile_form
    })


# Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('index')   # 👈 fixed
    else:
        form = AuthenticationForm()
    return render(request, 'tweetapp/login.html', {'form': form})


# Create Tweet
@login_required
def create_tweet(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.author = request.user
            tweet.save()
            messages.success(request, 'Tweet Posted Successfully!!!')
            return redirect('index')
    else:
        form = TweetForm()   

    
    return render(request, 'tweetapp/tweet_form.html', {'form': form})


# Tweet Detail
def tweet_detail(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    return render(request, 'tweetapp/tweet_detail.html', {'tweet': tweet})


# Edit Tweet
@login_required
def tweet_edit(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)

    if tweet.author != request.user:
        
        return redirect('tweet_detail', pk=pk)

    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('tweet_detail', pk=tweet.pk)
    else:
        form = TweetForm(instance=tweet)

    return render(request, 'tweetapp/tweet_edit.html', {'form': form, 'tweet': tweet})


# Delete Tweet
@login_required
def tweet_delete(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    if request.method == "POST":
        tweet.delete()
        return redirect('index')   # ✅ use index
    return render(request, 'tweetapp/tweet_delete.html', {'tweet': tweet})


# Profile View
@login_required
def profile(request):
    user = request.user
    tweets = user.tweets.all()
    if request.method == "POST":
        pform = ProfileForm(request.POST, request.FILES, instance=user.profile)
        if pform.is_valid():
            pform.save()
            messages.success(request, 'Profile Updated')
            return redirect('profile')
    else:
        pform = ProfileForm(instance=user.profile)
    return render(request, 'tweetapp/profile.html', {
        'user_obj': user,
        "tweets": tweets,
        "pform": pform
    })


# Logout View
def user_logout(request):
    logout(request)
    return redirect('login')
