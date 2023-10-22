from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    TemplateView,
    View,
)

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Location, Like
from .forms import LocationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator


class Locations(ListView):
    """View all images"""

    template_name = "locations/locations.html"
    model = Location
    context_object_name = "locations"
    paginate_by = 2

    def get_queryset(self, **kwargs):
        query = self.request.GET.get("q")
        if query:
            location = self.model.objects.filter(
                Q(title__icontains=query)
                | Q(description__icontains=query)
                | Q(location_types__icontains=query)
            )
        else:
            location = self.model.objects.all()
        return location


class LocationDetail(DetailView):
    """View a single location"""

    def get(self, request, slug, *args, **kwargs):
        location = get_object_or_404(Location, slug=slug)
        # liked = False
        # if request.user.is_authenticated and
        # location.likes.filter(id=request.user.id).exists():
        #     liked = True

        return render(
            request,
            "locations/location_detail.html",
            {
                "location": location,
                # "liked": liked
            },
        )


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

    template_name = "locations/edit_location.html"
    model = Location
    form_class = LocationForm
    success_url = "/locations/"

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteLocation(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete an Image"""

    model = Location
    success_url = "/locations/"

    def test_func(self):
        return self.request.user == self.get_object().user


class LocationImage(LoginRequiredMixin, TemplateView):
    """View user images in dashboard"""

    template_name = "account/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        locations = Location.objects.filter(user=current_user)
        paginator = Paginator(locations, 2)

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context["locations"] = locations
        return context


class LikeLocationView(LoginRequiredMixin, View):
    """Like Button"""

    def post(self, request, slug, *args, **kwargs):
        location = get_object_or_404(Location, slug=slug)
        like, created = Like.objects.get_or_create(
            user=request.user, location=location)

        if not created:
            like.delete()

        return HttpResponseRedirect(reverse('location_detail', args=[slug]))
