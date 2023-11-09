# Core Django imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import User, auth
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    TemplateView,
    View,
)

# Imports from apps
from .forms import LocationForm
from .models import Location, Like, Comment
from .forms import CommentForm


class Index(TemplateView):
    """HomePage/Index"""

    template_name = "locations/index.html"


class Locations(ListView):
    """View images uploaded by users"""

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

    def get(self, request, slug, *args, **kwargs):
        location = get_object_or_404(Location, slug=slug)
        form = CommentForm()
        liked = False
        if location.likes.filter(id=request.user.id).exists():
            liked = True
        return render(
            request,
            "locations/location_detail.html",
            {"location": location, "form": form, "liked": liked},  
        )

class LikeLocationView(LoginRequiredMixin, View):
    """Button users use to like photos"""

    def post(self, request, slug, *args, **kwargs):
        location = get_object_or_404(Location, slug=slug)
        like, created = Like.objects.get_or_create(user=request.user, location=location)

        if not created:
            like.delete()

        return HttpResponseRedirect(reverse("location_detail", args=[slug]))

        
class AddLocation(LoginRequiredMixin, CreateView):
    """User can add a new location/spot"""

    template_name = "locations/add_location.html"
    model = Location
    form_class = LocationForm
    success_url = "/locations/locations/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddLocation, self).form_valid(form)


class EditLocation(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """User can edit any image/description they add"""

    template_name = "locations/edit_location.html"
    model = Location
    form_class = LocationForm
    success_url = "/locations/locations/"

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteLocation(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """User can delete any image/description they add"""

    model = Location
    success_url = "/locations/locations"

    def test_func(self):
        return self.request.user == self.get_object().user


class LocationImage(LoginRequiredMixin, TemplateView):
    """User will see images they upload in their dashboard"""

    template_name = "account/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        locations = Location.objects.filter(user=current_user)
        context["locations"] = locations
        return context




# Comments Section


@login_required
def add_comment(request, slug):
    location = get_object_or_404(Location, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.location = location
            comment.save()
            return redirect("location_detail", slug=slug)
    else:
        form = CommentForm()
    return render(request, "locations/add_comment.html", {"form": form})


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.user:
        return redirect("location_detail", slug=comment.location.slug)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("location_detail", slug=comment.location.slug)
    else:
        form = CommentForm(instance=comment)
    return render(
        request, "locations/edit_comment.html", {"form": form, "object": comment}
    )


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.user:
        return redirect("location_detail", slug=comment.location.slug)
    if request.method == "POST":
        comment.delete()
        return redirect("location_detail", slug=comment.location.slug)
    return render(request, "locations/delete_comment.html", {"comment": comment})
