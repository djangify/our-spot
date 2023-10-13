from django.views.generic import (
    CreateView, ListView,
    DetailView, DeleteView,
    UpdateView, TemplateView
)

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Location
from .forms import LocationForm


class Locations(ListView):
    """View all images"""

    template_name = "locations/locations.html"
    model = Location
    context_object_name = "locations"

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            location = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(location_types__icontains=query)
            )
        else:
            location = self.model.objects.all()
        return location


class LocationDetail(DetailView):
    """View a single location"""

    template_name = "locations/location_detail.html"
    model = Location
    context_object_name = "location"


class AddLocation(LoginRequiredMixin, CreateView):
    """Add location view"""

    template_name = "locations/add_location.html"
    model = Location
    form_class = LocationForm
    success_url = "/locations/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddLocation, self).form_valid(form)


class EditLocation(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a location"""
    template_name = 'locations/edit_location.html'
    model = Location
    form_class = LocationForm
    success_url = '/locations/'

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteLocation(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete an Image"""
    model = Location
    success_url = '/locations/'

    def test_func(self):
        return self.request.user == self.get_object().user


class LocationImage(LoginRequiredMixin, TemplateView):
    """View user images in dashboard"""
    template_name = 'account/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        location_count = current_user.location_owner.count()
        context['location_count'] = location_count
        return context