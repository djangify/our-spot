from django import forms
from .models import Locations


class LocationForm(forms.ModelForm):
    """Form to create a spot"""

    class Meta:
        model = Locations
        fields = [
            "title",
            "description",
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
