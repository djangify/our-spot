from django import forms
from .models import Location, Comment


class LocationForm(forms.ModelForm):
    """Display form for users to add a location"""
    class Meta:
        model = Location
        fields = [
            "title",
            "description",
            "image",
            "image_alt",
            "location_types",
        ]

        widget = {
            "description": forms.Textarea(attrs={"rows": 7}),
        }

        labels = {
            "title": "Give Your Spot A Title",
            "description": "Description of Your Spot",
            "image": "Location Image",
            "image_alt": "Describe Image",
            "location_types": "Choose Location",
        }


class CommentForm(forms.ModelForm):
    """Display comment form for users to add comments"""
    class Meta:
        model = Comment
        fields = ['text']
