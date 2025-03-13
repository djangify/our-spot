# Core Django imports
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.urls import reverse

# Imports from the current app
from .forms import LoginForm, UserRegistrationForm, UserEditForm
from .forms import ProfileEditForm
from .models import Profile, EmailVerificationToken

# Imports from other apps
from locations.models import Location


def register(request):
    """User registration form with email verification"""
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create inactive user until email is verified
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.is_active = False  # User inactive until email verified
            new_user.save()
            
            # Create the user profile
            Profile.objects.create(user=new_user)
            
            # Send verification email
            send_verification_email(request, new_user)
            
            # Redirect to verification sent page
            return redirect('account:verification_sent')
        else:
            # Form is not valid, it will be re-rendered with errors
            pass
    else:
        user_form = UserRegistrationForm()
    
    return render(request, "account/register.html", {"user_form": user_form})


def send_verification_email(request, user):
    """Send email verification link to newly registered user"""
    try:
        # Delete any existing tokens for this user
        EmailVerificationToken.objects.filter(user=user).delete()
        
        # Create new token
        token = EmailVerificationToken.objects.create(user=user)
        
        verification_url = request.build_absolute_uri(
            reverse('account:verify_email', args=[str(token.token)])
        )
        
        subject = 'Verify your email for Show Your Spot'
        html_message = render_to_string('account/email_verification_email.html', {
            'user': user,
            'verification_url': verification_url,
        })
        plain_message = strip_tags(html_message)
        
        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            html_message=html_message,
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Error sending verification email: {e}")
        return False


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
                    return redirect('account:dashboard')
                else:
                    messages.error(request, "Account not activated. Please check your email for verification link.")
                    return redirect('login')
            else:
                messages.error(request, "Invalid username or password.")
                return redirect('login')
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


def verification_sent(request):
    return render(request, "account/verification_sent.html")


def verify_email(request, token):
    try:
        verification_token = EmailVerificationToken.objects.get(token=token)
        if verification_token.is_valid():
            user = verification_token.user
            user.is_active = True
            user.save()
            verification_token.delete()
            return render(request, "account/email_verified.html")
        else:
            # Token expired
            return render(request, "account/email_verification_invalid.html")
    except EmailVerificationToken.DoesNotExist:
        # Invalid token
        return render(request, "account/email_verification_invalid.html")


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
            messages.success(request, "Profile updated successfully")
            return redirect('account:dashboard')
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


@login_required  # Provides a list of all members
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


@login_required  # Display user profile information
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