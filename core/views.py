from django.views.generic import TemplateView, DetailView
from .models import HomePage, HeroBanner, Page
from locations.models import Location
from django.apps import apps
from django.shortcuts import render
from django.db.models import Q
from locations.models import Location
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
                Category = apps.get_model('blog', 'Category')
                
                # Get Spot Highlights category
                spot_highlights = Category.objects.filter(slug='spot-highlights').first()
                if spot_highlights:
                    # Get published posts from this category
                    context['blog_features'] = Post.objects.filter(
                        category=spot_highlights, 
                        status='published'
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