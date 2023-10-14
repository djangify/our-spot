from django.views.generic import ListView, TemplateView
from locations.models import Location
from django.shortcuts import render
import random
import cloudinary
import cloudinary.api
from locations.models import Location


class Index(ListView):
    template_name = "home/index.html"
    model = Location
    context_object_name = "location"

    def get_queryset(self):
        return self.model.objects.all()[:7]


class HomePageImage(TemplateView):
    template_name = "home/index.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     all_images = cloudinary.api.resources(type="upload", resource_type="image")
    #     random.shuffle(all_images['resources'])
    #     random_image = all_images['resources'][0]
    #     context['random_image'] = random_image
    #     return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["locations"] = Location.objects.all()[:5]
        return context
