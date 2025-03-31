# Core Django imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
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
from .models import Location, Comment
from .forms import CommentForm


class Index(TemplateView):
    """HomePage/Index"""

    template_name = "index.html"


class Locations(ListView):
    """View locations uploaded by followed users."""
    template_name = "locations/locations.html"
    model = Location
    context_object_name = "locations"
    paginate_by = 12

    def get_queryset(self):
        # Get users that the current user follows
        if self.request.user.is_authenticated:
            followed_users = self.request.user.get_following()
            # Include the user's own posts
            queryset = self.model.objects.filter(
                Q(user__in=followed_users) | Q(user=self.request.user)
            ).order_by('-posted_date')
        else:
            # For unauthenticated users, show a selection of recent locations
            queryset = self.model.objects.all().order_by('-posted_date')[:20]
            
        return queryset

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


class LocationLike(View):
    """Like button"""
    def post(self, request, slug):
        location = get_object_or_404(Location, slug=slug)

        if location.likes.filter(id=request.user.id).exists():
            location.likes.remove(request.user)
        else:
            location.likes.add(request.user)

        return HttpResponseRedirect(reverse("locations:location_detail", args=[slug]))

        
class AddLocation(LoginRequiredMixin, CreateView):
    """User can add a new location/spot"""

    template_name = "locations/add_location.html"
    model = Location
    form_class = LocationForm
    success_url = reverse_lazy("locations:locations")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddLocation, self).form_valid(form)


class EditLocation(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """User can edit any image/description they add"""

    template_name = "locations/edit_location.html"
    model = Location
    form_class = LocationForm
    success_url = reverse_lazy("locations:locations")

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteLocation(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """User can delete any image/description they add"""

    model = Location
    success_url = reverse_lazy("locations:locations")

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

# Comments Section - add, edit and delete

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
            return redirect("locations:location_detail", slug=slug)
    else:
        form = CommentForm()
    return render(request, "locations/add_comment.html", {"form": form})


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.user:
        return redirect("locations:location_detail", slug=comment.location.slug)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("locations:location_detail", slug=comment.location.slug)
    else:
        form = CommentForm(instance=comment)
    return render(
        request, "locations/edit_comment.html", {"form": form, "object": comment}
    )


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.user:
        return redirect("locations:location_detail", slug=comment.location.slug)
    if request.method == "POST":
        comment.delete()
        return redirect("locations:location_detail", slug=comment.location.slug)
    return render(request, "locations/delete_comment.html", {"comment": comment})
