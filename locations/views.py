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
from .forms import LocationForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Location


# View all images


class Locations(ListView):

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


# View a single location. Includes comment and tag submission


class LocationDetail(DetailView):
    """View a single location"""
    def get(self, request, slug, *args, **kwargs):
        location = get_object_or_404(Location, slug=slug)
        # liked = False
        # if request.user.is_authenticated and location.likes.filter(id=request.user.id).exists():
        #     liked = True
        return render(
            request,
            "locations/location_detail.html",
            {
                "location": location,
                # "liked": liked
            },
        )


# Add location view


class AddLocation(LoginRequiredMixin, CreateView):

    template_name = "locations/add_location.html"
    model = Location
    form_class = LocationForm
    success_url = "/locations/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddLocation, self).form_valid(form)


# Edit a location


class EditLocation(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    template_name = "locations/edit_location.html"
    model = Location
    form_class = LocationForm
    success_url = "/locations/"

    def test_func(self):
        return self.request.user == self.get_object().user

# Delete an Image


class DeleteLocation(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Location
    success_url = "/locations/"

    def test_func(self):
        return self.request.user == self.get_object().user

# View user images in dashboard


class LocationImage(LoginRequiredMixin, TemplateView):

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

# Like Button


class LikeLocationView(LoginRequiredMixin, View):

    def post(self, request, slug, *args, **kwargs):
        location = get_object_or_404(Location, slug=slug)
        like, created = Like.objects.get_or_create(
            user=request.user, location=location)

        if not created:
            like.delete()

        return HttpResponseRedirect(reverse('location_detail', args=[slug]))

# comments - add, edit and delete

def add_comment(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.location = location
            comment.user = request.user
            comment.photo = request.user.profile.photo  # Assuming the user's profile has a photo field
            comment.save()
            return redirect('location_detail', location_id=location.id)
    else:
        form = CommentForm()
    return render(request, 'locations/comments.html', {'form': form})

def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('location_detail', location_id=comment.location.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'locations/location_edit.html', {'form': form})

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        location_id = comment.location.id
        comment.delete()
        return redirect('location_detail', location_id=location_id)
    return render(request, 'locations/location_confirm_delete.html', {'object': comment})