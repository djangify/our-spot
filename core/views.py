from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, DetailView
from django.views.decorators.http import require_GET
from django.db.models import Q
from django.utils import timezone
from django.apps import apps
from django.conf import settings
from django.core.mail import send_mail

from .models import HomePage, HeroBanner, Page, Report
from .forms import ReportForm
from locations.models import Location, Comment
from blog.models import Post
from account.models import User


class HomeView(TemplateView):
    """View for the home page"""
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get home page content
        try:
            home_content = HomePage.objects.filter(is_active=True).first()
            context['home'] = home_content
        except HomePage.DoesNotExist:
            context['home'] = None
            
        # Get active hero banner
        try:
            banner = HeroBanner.objects.filter(is_active=True).first()
            context['banner'] = banner
        except HeroBanner.DoesNotExist:
            context['banner'] = None
            
        # Get latest locations (6 most recent)
        context['latest_locations'] = Location.objects.all().order_by('-posted_date')[:6]
        
        # Get featured spots from blog 
        context['blog_features'] = []
        try:
            # Check if blog app is installed
            if 'blog' in [app.name for app in apps.get_app_configs()]:
                # Import models only if app exists
                Post = apps.get_model('blog', 'Post')
                
                # Get featured posts
                context['blog_features'] = Post.objects.filter(
                    status='published',
                    featured=True,
                    publish_date__lte=timezone.now()
                ).order_by('-publish_date')[:3]
                
                # Fallback to category if no featured posts found
                if not context['blog_features']:
                    Category = apps.get_model('blog', 'Category')
                    spot_highlights = Category.objects.filter(slug='spot-highlights').first()
                    if spot_highlights:
                        # Get published posts from this category
                        context['blog_features'] = Post.objects.filter(
                            category=spot_highlights, 
                            status='published',
                            publish_date__lte=timezone.now()
                        ).order_by('-publish_date')[:3]
        except (LookupError, ImportError):
            # If blog app doesn't exist or models aren't available
            pass
            
        return context


class PageDetailView(DetailView):
    """View for standard pages (About, Privacy Policy, etc.)"""
    model = Page
    template_name = "core/page_detail.html"
    context_object_name = "page"

    def get_queryset(self):
        return Page.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def search(request):
    """Search functionality across the site"""
    query = request.GET.get('q', '')
    search_type = request.GET.get('type', 'all')
    
    # If no type specified, use the one from session or default to 'all'
    if not search_type:
        search_type = request.session.get('last_search_type', 'all')
    else:
        # Save the current search type to session
        request.session['last_search_type'] = search_type

    locations = []
    blog_posts = []
    members = []
    
    if query:
        # Filter based on search_type or search all
        if search_type == 'all' or search_type == 'locations':
            locations = Location.objects.filter(
                Q(title__icontains=query) | 
                Q(description__icontains=query)
            )[:5]  # Limit to 5 results per category
            
        if search_type == 'all' or search_type == 'blog':
            blog_posts = Post.objects.filter(
                Q(title__icontains=query) | 
                Q(content__icontains=query)
            )[:5]
            
        if search_type == 'all' or search_type == 'members':
            members = User.objects.filter(
                Q(username__icontains=query) | 
                Q(first_name__icontains=query) | 
                Q(last_name__icontains=query)
            )[:5]
    
    context = {
        'query': query,
        'locations': locations,
        'blog_posts': blog_posts,
        'members': members,
        'search_type': search_type,
    }
    
    return render(request, 'core/components/search_results.html', context)


def policies_index(request):
    """View for displaying the policies index page"""
    context = {
        'breadcrumbs': [
            {'title': 'Policies', 'url': None}
        ]
    }
    return render(request, 'core/policy/policies_index.html', context)


def privacy_policy(request):
    """View for displaying the privacy policy"""
    context = {
        'breadcrumbs': [
            {'title': 'Policies', 'url': reverse('core:policies_index')},
            {'title': 'Privacy Policy', 'url': None}
        ]
    }
    return render(request, 'core/policy/privacy_policy.html', context)


def cookies_policy(request):
    """View for displaying the cookies policy"""
    context = {
        'breadcrumbs': [
            {'title': 'Policies', 'url': reverse('core:policies_index')},
            {'title': 'Cookies Policy', 'url': None}
        ]
    }
    return render(request, 'core/policy/cookies_policy.html', context)


def advertising_policy(request):
    """View for displaying the advertising policy"""
    context = {
        'breadcrumbs': [
            {'title': 'Policies', 'url': reverse('core:policies_index')},
            {'title': 'Advertising Policy', 'url': None}
        ]
    }
    return render(request, 'core/policy/advertising_policy.html', context)


def terms_policy(request):
    """View for displaying the terms and conditions"""
    context = {
        'breadcrumbs': [
            {'title': 'Policies', 'url': reverse('core:policies_index')},
            {'title': 'Terms & Conditions', 'url': None}
        ]
    }
    return render(request, 'core/policy/terms_policy.html', context)


def moderation_policy(request):
    """View for displaying the content moderation policy"""
    context = {
        'breadcrumbs': [
            {'title': 'Policies', 'url': reverse('core:policies_index')},
            {'title': 'Moderation Policy', 'url': None}
        ]
    }
    return render(request, 'core/policy/moderation_policy.html', context)


@require_GET
def robots_txt(request):
    """Generate robots.txt content"""
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
        "Disallow: /account/login/",
        "Disallow: /account/register/",
        "Disallow: /account/password-reset/",
        f"Sitemap: {request.build_absolute_uri('/sitemap.xml')}",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


@login_required
def report_content(request):
    """Simple contact-style reporting form"""
    if request.method == 'POST':
        # Create a report object directly
        try:
            # Clear any existing messages to prevent duplicates
            storage = messages.get_messages(request)
            storage.used = True
            
            report = Report(
                reporter=request.user,
                report_type=request.POST.get('report_type', 'location'),
                report_content_type=request.POST.get('report_content_type', 'photo'),
                reason=request.POST.get('reason', ''),
                details=request.POST.get('details', '')
            )
            
            # Set content type and object id if provided
            content_type_id = request.POST.get('content_type_id')
            object_id = request.POST.get('object_id')
            
            if content_type_id and object_id:
                try:
                    report.content_type_id = int(content_type_id)
                    report.object_id = int(object_id)
                except (ValueError, TypeError):
                    # If conversion fails, use defaults
                    content_type = ContentType.objects.get_for_model(User)
                    report.content_type = content_type
                    report.object_id = request.user.id
            else:
                # Default to reporting the user's own profile if no object specified
                content_type = ContentType.objects.get_for_model(User)
                report.content_type = content_type
                report.object_id = request.user.id
                
            # Save the report
            report.save()
            
            messages.success(request, "Thank you for your report and for keeping the site safe. We will review the content and take appropriate action.")
            return redirect('locations:locations')
            
        except Exception as e:
            messages.error(request, f"An error occurred while submitting your report: {str(e)}")
    
    # GET request - show the form
    return render(request, 'core/components/report.html', {
        'content_type_id': request.GET.get('content_type_id', ''),
        'object_id': request.GET.get('object_id', ''),
        'report_type': request.GET.get('report_type', 'location')
    })