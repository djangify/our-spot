# Core Django imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.db import models  # Add this for the models.Count
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
from account.models import UserFollow


class Index(TemplateView):
    """HomePage/Index"""

    template_name = "index.html"


class Locations(ListView):
    """View locations uploaded by followed users."""
    template_name = "locations/locations.html"
    model = Location
    context_object_name = "locations"
    paginate_by = 7  # Reasonable number of posts per load

    def get_queryset(self):
        if self.request.user.is_authenticated:
            # Get users being followed
            followed_users = self.request.user.get_following()
            
            # Get content from followed users and the current user, ordered by date
            queryset = self.model.objects.filter(
                Q(user__in=followed_users) | Q(user=self.request.user)
            ).order_by('-posted_date')
        else:
            # For non-authenticated users, just show most recent content
            queryset = self.model.objects.all().order_by('-posted_date')[:20]
            
        # Check if there's a search query
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | 
                Q(description__icontains=query) | 
                Q(location_types__icontains=query)
            )
            
        return queryset
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add recent locations for sidebar
        context['recent_locations'] = Location.objects.all().order_by('-posted_date')[:5]
        
        if self.request.user.is_authenticated:
            # Add recent followers for sidebar
            recent_followers = UserFollow.objects.filter(
                followed_user=self.request.user
            ).order_by('-created_at')[:5]
            context['recent_followers'] = [follow.user for follow in recent_followers]
            
            # Popular locations based on likes
            context['popular_locations'] = Location.objects.annotate(
                like_count=models.Count('likes')
            ).order_by('-like_count')[:5]
        
        # Add a flag to indicate if this is an AJAX request for more content
        context['is_ajax_request'] = self.request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        
        return context

    def render_to_response(self, context, **response_kwargs):
        """Override render_to_response to handle AJAX requests."""
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            from django.template.loader import render_to_string
            from django.http import JsonResponse
            
            # Get the total number of pages for max page check
            total_pages = context['paginator'].num_pages
            current_page = context['page_obj'].number
            
            # Debug info
            print(f"AJAX request - Page {current_page} of {total_pages}")
            
            # Render only the location items, not the whole page
            html = render_to_string(
                'partials/location_list_items.html',
                {'locations': context['locations']},
                request=self.request
            )
            
            # Create response with has_next and current/total page info
            response_data = {
                'html': html,
                'has_next': context['page_obj'].has_next(),
                'current_page': current_page,
                'total_pages': total_pages
            }
            
            return JsonResponse(response_data)
            
        return super().render_to_response(context, **response_kwargs)


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
    """Like button functionality with AJAX support"""
    def post(self, request, slug):
        location = get_object_or_404(Location, slug=slug)
        
        # Toggle like status
        if location.likes.filter(id=request.user.id).exists():
            location.likes.remove(request.user)
            liked = False
        else:
            location.likes.add(request.user)
            liked = True
            
        # Check if AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'liked': liked,
                'likes_count': location.likes.count()
            })
        else:
            # Fallback for non-JS browsers
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
