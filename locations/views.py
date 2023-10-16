from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    TemplateView,
)

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Location, LikeLocation
from .forms import LocationForm
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


class Locations(ListView):
    """View all images"""

    template_name = "locations/locations.html"
    model = Location
    context_object_name = "locations"

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
        context["locations"] = locations
        return context


# class LocationDetailView(LoginRequiredMixin, DetailView):

#     model = Location
#     slug_field = 'slug'

#     def post(self, request, slug):

#         location = Location.objects.get(slug=slug)

#         if request.user in location.likes.all():
#             location.likes.remove(request.user)
#         else:
#             location.likes.add(request.user)

#         likes_count = location.likes.count()
#         return JsonResponse({'likes_count': likes_count})


@login_required
def like_location(request):
    username = request.user.username
    location_id = request.GET.get('location_id')

    location = Location.objects.get(id=location_id)

    like_filter = LikeLocation.objects.filter(
        location_id=location_id, username=username).first()

    if like_filter == None:
        new_like = LikeLocation.objects.create(location_id=location_id, username=username)
        new_like.save()
        location.no_of_likes = location.no_of_likes+1
        location.save()
        return redirect('/')
    else:
        like_filter.delete()
        location.no_of_likes = location.no_of_likes-1
        location.save()
        return redirect('/')
