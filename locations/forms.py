from django import forms
from .models import Location, Comment


class LocationForm(forms.ModelForm):
    """Display form for users to add a location"""

    class Meta:
        model = Location
        fields = [
            "title",
            "description",
            "location_types",
            "image",
            "image_alt",
        ]

        widgets = {
            "title": forms.Textarea(attrs={"cols": 70, "rows": 1}),
            "description": forms.Textarea(attrs={"cols": 70, "rows": 20}),
        }

        labels = {
            "title": "Give Your Spot A Title",
            "description": "Description of Your Spot",
            "location_types": "Choose Location",
            "image": "Location Image",
            "image_alt": "Describe Image",
        }


class CommentForm(forms.ModelForm):
    """Display comment form for users to add comments"""

    class Meta:
        model = Comment
        fields = ["text"]
