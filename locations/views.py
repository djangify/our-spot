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
from .forms import LocationForm, CommentForm, TagForm
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
    model = Location
    template_name = "locations/location_detail.html"
    context_object_name = "location"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['tags'] = self.object.tags.all()
        context['comment_form'] = CommentForm()
        context['tag_form'] = TagForm()
        return context

    # Handle comment form submission
    def post(self, request, slug, *args, **kwargs):
        location = get_object_or_404(Location, slug=slug)
        comment_form = CommentForm(request.POST)
        tag_form = TagForm(request.POST) # Define tag_form
        if comment_form.is_valid() and tag_form.is_valid(): # Check if both forms are valid
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.location = location
            new_comment.save()
            new_tag = tag_form.save(commit=False)
            new_tag.location = location
            new_tag.save()
            # Redirect to the same location detail page after adding a comment and tag
            return self.get(request, slug=slug)

        # Pass tag_form to the context dictionary
        return render(request, self.template_name, {
            'location': location,
            'comments': location.comments.all(),
            'tags': location.tags.all(),
            'comment_form': comment_form,
            'tag_form': tag_form,
        })


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

