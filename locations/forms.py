from django import forms
from .models import Location, Comment, Tag
from django.utils.text import slugify


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



class LocationForm(forms.ModelForm):
    """Form for creating and editing locations"""
    tags = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full border border-gray-300 rounded p-2',
            'placeholder': 'Add tags separated by commas (e.g., beach, sunset, mountain)'
        })
    )
    
    class Meta:
        model = Location
        fields = ['title', 'description', 'image', 'image_alt', 'location_types']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            # If editing existing location, pre-populate tags
            self.initial['tags'] = ', '.join([tag.name for tag in self.instance.tags.all()])
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        if commit:
            instance.save()
            
            # Clear existing tags and add new ones
            instance.tags.clear()
            tag_names = [name.strip() for name in self.cleaned_data['tags'].split(',') if name.strip()]
            
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(
                    name=tag_name,
                    defaults={'slug': slugify(tag_name)}
                )
                instance.tags.add(tag)
                
        return instance