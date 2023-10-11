from django import forms
from .models import Location


class LocationForm(forms.ModelForm):
    """Form to create a spot"""

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
