from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.urls import reverse
from account.models import EmailVerificationToken


class Command(BaseCommand):
    help = 'Resend verification email to a specific email address'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='Email address to resend verification to')

    def handle(self, *args, **options):
        email = options['email']
        
        try:
            # Find the user with this email
            user = User.objects.get(email=email)
            
            # Get or create a verification token
            token, created = EmailVerificationToken.objects.get_or_create(user=user)
            
            if not created:
                self.stdout.write(self.style.SUCCESS(f"Using existing token for {email}"))
            
            # Prepare the verification URL
            verification_url = f"{settings.SITE_URL}{reverse('account:verify_email', args=[str(token.token)])}"
            
            # Render the email template
            subject = 'Verify your email for Show Your Spot'
            html_message = render_to_string('account/email_verification_reminder.html', {
                'user': user,
                'verification_url': verification_url,
                'site_url': settings.SITE_URL,
            })
            plain_message = strip_tags(html_message)
            
            # Send the email
            send_mail(
                subject,
                plain_message,
                settings.DEFAULT_FROM_EMAIL,
                [email],
                html_message=html_message,
                fail_silently=False,
            )
            
            self.stdout.write(self.style.SUCCESS(f'Verification email resent to {email}'))
            
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'No user found with email {email}'))