from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from account.models import EmailVerificationToken
from django.utils import timezone
from datetime import timedelta
import uuid

class Command(BaseCommand):
    help = 'Test email verification edge cases'

    def handle(self, *args, **kwargs):
        # Create test user if not exists
        test_user, created = User.objects.get_or_create(
            username='testverify',
            email='testverify@example.com',
            defaults={'is_active': False}
        )
        
        if created:
            test_user.set_password('testpassword123')
            test_user.save()
            self.stdout.write(self.style.SUCCESS(f'Created test user: {test_user.username}'))
        
        # Create a valid token
        valid_token = EmailVerificationToken.objects.create(user=test_user)
        self.stdout.write(self.style.SUCCESS(f'Created valid token: {valid_token.token}'))
        
        # Create an expired token
        expired_user, _ = User.objects.get_or_create(
            username='expiredverify',
            email='expiredverify@example.com',
            defaults={'is_active': False}
        )
        
        expired_token = EmailVerificationToken.objects.create(user=expired_user)
        # Set creation time to 25 hours ago
        expired_token.created_at = timezone.now() - timedelta(hours=25)
        expired_token.save()
        
        self.stdout.write(self.style.SUCCESS(f'Created expired token: {expired_token.token}'))
        
        # Create an invalid token format
        self.stdout.write(self.style.SUCCESS(f'Test with invalid token: {uuid.uuid4()}'))
        
        self.stdout.write(self.style.SUCCESS(
            'Test URLs:\n'
            f'Valid: /account/verify-email/{valid_token.token}/\n'
            f'Expired: /account/verify-email/{expired_token.token}/\n'
            f'Invalid: /account/verify-email/{uuid.uuid4()}/'
        ))
        