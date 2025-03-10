# Core Django imports
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import logout
from django.shortcuts import redirect

# Imports from the current app
from .forms import LoginForm, UserRegistrationForm, UserEditForm
from .forms import ProfileEditForm
from .models import Profile

# Imports from other apps
from locations.models import Location


def register(request):
    """User registration form"""
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request, "account/register_done.html",
                          {"new_user": new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, "account/register.html", {"user_form": user_form})


def user_login(request):
    """User login form"""
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


@login_required
def dashboard(request):
    # Get locations for the current user
    locations = Location.objects.filter(user=request.user)
    return render(
        request, 
        "account/dashboard.html", 
        {
            "section": "dashboard",
            "locations": locations,
            "user": request.user 
        }
    )


@login_required  # User can edit their profile image/account
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES
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


@login_required       # Provides a list of all members
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(
        request, "account/user/list.html", {"section": "people", "users": users}
    )


@login_required  # Displays images uploaded by a user on their profile page
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    locations = Location.objects.filter(user=user)
    context = {"user": user, "locations": locations}

    return render(request, "account/user/detail.html", context)


@login_required   # Display user profile information
def user_profile(request, username):
    user = User.objects.get(username=username)

    context = {
        "user": user,
    }
    return render(request, "account/user/detail.html", context)

def logout_view(request):
    """Custom logout view that works with any HTTP method"""
    logout(request)
    return redirect('core:home')  # Redirects to the homepage after logout