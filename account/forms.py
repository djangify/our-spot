from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    """Form users use to login"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    """User registration form"""

    password = forms.CharField(
        label="Password",
        help_text="Your password must contain at least 8 characters, cannot be entirely numeric, and must not be too common.",
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="Repeat password",
        help_text="Enter the same password as before, for verification.",
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match.")
        return cd["password2"]

    def clean_email(self):
        data = self.cleaned_data.get("email")
        if data:
            if User.objects.filter(email=data).exists():
                raise forms.ValidationError("Email already in use.")
        return data


class UserEditForm(forms.ModelForm):
    """User can edit registration details"""

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def clean_email(self):
        data = self.cleaned_data["email"]
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError("Email already in use.")
        return data

class ProfileEditForm(forms.ModelForm):
    """User can edit profile form"""

    class Meta:
        model = Profile
        fields = ["date_of_birth", "photo", "about_me"]
        widgets = {
            'about_me': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us a bit about yourself...'}),
        }