from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from account.models import EmailVerificationToken
from locations.models import Location


class Command(BaseCommand):
    help = 'Send reminder emails to users who have not verified their accounts after 14 days and delete unverified accounts older than 60 days'

    def handle(self, *args, **options):
        self._process_fourteen_day_reminders()
        self._process_sixty_day_deletions()

    def _process_fourteen_day_reminders(self):
        # Calculate the date 14 days ago
        fourteen_days_ago = timezone.now() - timedelta(days=14)
        # Calculate 15 days ago to ensure we only get users who are exactly at the 14-day mark
        fifteen_days_ago = timezone.now() - timedelta(days=15)
        
        # Find unverified users who registered approximately 14 days ago (between 14 and 15 days)
        # and haven't been sent a reminder yet
        unverified_users = User.objects.filter(
            is_active=False,
            date_joined__lt=fourteen_days_ago,
            date_joined__gte=fifteen_days_ago,
            emailverificationtoken__reminder_sent=False  # Check if reminder has not been sent
        )
        
        # Get the 6 most recent locations for the reminder email
        recent_spots = Location.objects.order_by('-posted_date')[:6]
        
        # Send reminder emails
        count = 0
        for user in unverified_users:
            # Check if user has a verification token
            try:
                token = EmailVerificationToken.objects.get(user=user)
                
                # Prepare the verification URL
                verification_url = f"{settings.SITE_URL}{reverse('account:verify_email', args=[str(token.token)])}"
                
                # Render the email template
                subject = 'Reminder: Verify your email for Show Your Spot'
                html_message = render_to_string('account/email_verification_reminder.html', {
                    'user': user,
                    'verification_url': verification_url,
                    'recent_spots': recent_spots,
                })
                plain_message = strip_tags(html_message)
                
                # Send the email
                send_mail(
                    subject,
                    plain_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [user.email],
                    html_message=html_message,
                    fail_silently=False,
                )
                
                # Mark that the reminder has been sent
                token.reminder_sent = True
                token.reminder_sent_at = timezone.now()
                token.save()
                
                count += 1
                
            except EmailVerificationToken.DoesNotExist:
                # If no token exists, log the issue
                self.stdout.write(self.style.WARNING(f"No verification token found for {user.username}"))
        
        self.stdout.write(
            self.style.SUCCESS(f'Sent {count} reminder emails to unverified users at the 14-day mark')
        )

    def _process_sixty_day_deletions(self):
        # Calculate the date 60 days ago
        sixty_days_ago = timezone.now() - timedelta(days=60)
        
        # Find unverified users who registered more than 60 days ago
        old_unverified_users = User.objects.filter(
            is_active=False,
            date_joined__lt=sixty_days_ago
        )
        
        # Count before deletion
        deletion_count = old_unverified_users.count()
        
        # Delete these users
        if deletion_count > 0:
            # Optional: Send a final deletion notification before deleting
            for user in old_unverified_users:
                subject = 'Your Show Your Spot account has been removed'
                message = f"""
                Dear {user.username},
                
                Your account on Show Your Spot has been automatically removed as it has been inactive 
                and unverified for more than 60 days.
                
                If you would like to use our service, please register again.
                
                Thank you,
                The Show Your Spot Team
                """
                try:
                    send_mail(
                        subject,
                        message,
                        settings.DEFAULT_FROM_EMAIL,
                        [user.email],
                        fail_silently=True,  # Silently fail as we're deleting anyway
                    )
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f"Failed to send deletion email to {user.email}: {str(e)}"))
            
            # Now delete the users
            old_unverified_users.delete()
        
        self.stdout.write(
            self.style.SUCCESS(f'Deleted {deletion_count} unverified user accounts older than 60 days')
        )
        