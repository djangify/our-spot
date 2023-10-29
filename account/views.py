from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import LoginForm, UserRegistrationForm, \
    UserEditForm, ProfileEditForm
from .models import Profile, FollowersCount
from locations.models import Location


# User registration form

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data["password"])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request, "account/register_done.html",
                          {"new_user": new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, "account/register.html", {"user_form": user_form})


# user login form

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authenticated successfully")
                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()
    return render(request, "account/login.html", {"form": form})


# User dashboard area

@login_required
def dashboard(request):
    return render(request, "account/dashboard.html", {"section": "dashboard"})


# User can edit their profile image/account

@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST,
            files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated " "successfully")
        else:
            messages.error(request, "Error updating your profile")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(
        request,
        "account/edit.html",
        {"user_form": user_form, "profile_form": profile_form},
    )

# Provides a list of all members


@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request,
                  'account/user/list.html',
                  {'section': 'people',
                   'users': users})

# to show photos that a user has uploaded on their profile


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    locations = Location.objects.filter(user=user)
    context = {
        'user': user,
        'locations': locations
    }

    return render(request, 'account/user/detail.html', context)

# Display user profile information


@login_required
def user_profile(request, username):
    user = User.objects.get(username=username)

    context = {
        'user': user,
        
    }


# User follow count system


def follow(request):
    current_user = request.GET.get('user')
    logged_in_user = request.user.username
    user_followers = len(FollowersCount.objects.filter(user=current_user))
    user_following = len(FollowersCount.objects.filter(follower=current_user))
    user_followers0 = FollowersCount.objects.filter(user=current_user)
    user_followers1 = []
    for i in user_followers0:
        user_followers0 = i.follower
        user_followers1.append(user_followers0)
    if logged_in_user in user_followers1:
        follow_button_value = 'unfollow'
    else:
        follow_button_value = 'follow'

    print(user_followers)
    return render(request, 'account/user/detail.html', {
        'current_user': current_user,
        'user_followers': user_followers,
        'user_following': user_following,
        'follow_button_value': follow_button_value
    })

def followers_count(request):
    if request.method == 'POST':
        value = request.POST['value']
        user = request.POST['user']
        follower = request.POST['follower']
        if value == 'follow':
            followers_cnt = FollowersCount.objects.create(follower=follower, user=user)
            followers_cnt.save()
        else:
            followers_cnt = FollowersCount.objects.get(follower=follower, user=user)
            followers_cnt.delete()
        
        return redirect('/?user='+user)

