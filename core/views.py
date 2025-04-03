from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView
from .models import HomePage, HeroBanner, Page
from locations.models import Location
from django.apps import apps
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from django.views.decorators.http import require_GET

from django.utils import timezone
from locations.models import Location, Comment
from blog.models import Post
from account.models import User  
from .models import Report
from .forms import ReportForm
from django.conf import settings


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

@login_required
def report_content(request):
    """AJAX view to handle report submissions"""
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.reporter = request.user
            
            # In your report_content view:
            report_count = Report.objects.filter(
                reporter=request.user, 
                created_at__date=timezone.now().date()
            ).count()

            daily_limit = settings.MODERATION_SETTINGS.get('DAILY_REPORT_LIMIT', 4)  # Default to 4 if not set
            if report_count >= daily_limit:
                return JsonResponse({
                    'status': 'error',
                    'message': f'You have reached the maximum number of {daily_limit} reports allowed per day.'
                })

            # Get content type and object ID from form
            content_type_id = request.POST.get('content_type_id')
            object_id = request.POST.get('object_id')
            report_type = request.POST.get('report_type')
            
            if content_type_id and object_id and report_type:
                report.content_type_id = content_type_id
                report.object_id = object_id
                report.report_type = report_type
                report.save()
                
                return JsonResponse({
                    'status': 'success',
                    'message': 'Thank you for your report. Our moderation team has been notified.'
                })
            
        return JsonResponse({
            'status': 'error',
            'message': 'There was an error with your report. Please try again.'
        })
        
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@login_required
def moderation_dashboard(request):
    """Dashboard for moderators to review reports"""
    if not request.user.is_staff:
        messages.error(request, "You don't have permission to access the moderation dashboard.")
        return redirect('core:home')
        
    pending_reports = Report.objects.filter(status='pending')
    recent_reports = Report.objects.exclude(status='pending').order_by('-updated_at')[:20]
    
    return render(request, 'moderation/dashboard.html', {
        'pending_reports': pending_reports,
        'recent_reports': recent_reports
    })

@login_required
def report_detail(request, report_id):
    """View for moderators to review a specific report"""
    if not request.user.is_staff:
        messages.error(request, "You don't have permission to access this page.")
        return redirect('core:home')
        
    report = get_object_or_404(Report, id=report_id)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        if action in ['reviewed', 'actioned', 'dismissed']:
            report.status = action
            report.reviewed_by = request.user
            report.review_notes = request.POST.get('review_notes', '')
            report.save()
            messages.success(request, f"Report #{report.id} has been marked as {report.get_status_display()}.")
            return redirect('moderation:dashboard')
    
    return render(request, 'core/report.html', {'report': report})

def send_moderation_action_notification(report):
    """Send email notification when moderation action is taken"""
    subject = f"Moderation Action: Report #{report.id} - {report.get_status_display()}"
    message = f"""
    A moderation action has been taken:
    
    Report ID: {report.id}
    Content Type: {report.get_report_type_display()}
    Status: {report.get_status_display()}
    Reviewed by: {report.reviewed_by.username if report.reviewed_by else 'Unknown'}
    Review Notes: {report.review_notes}
    
    This content has now been processed and can be removed from the system.
    """
    from django.core.mail import send_mail
    send_mail(
        subject,
        message,
        'noreply@showyourspot.com',
        ['djangify@gmail.com'],
        fail_silently=False,
    )

def moderation_policy(request):
    """View for displaying the content moderation policy"""
    return render(request, 'core/policy/moderation_policy.html')

@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
        "Disallow: /account/login/",
        "Disallow: /account/register/",
        "Disallow: /account/password-reset/",
        f"Sitemap: {request.build_absolute_uri('/sitemap.xml')}",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")