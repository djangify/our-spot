from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from account.models import EmailVerificationToken
from django.utils import timezone
from datetime import timedelta

class EmailVerificationTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword123',
            is_active=False
        )
        # Create verification token
        self.token = EmailVerificationToken.objects.create(user=self.user)
        self.client = Client()
        
    def test_verification_success(self):
        """Test successful email verification"""
        url = reverse('account:verify_email', args=[str(self.token.token)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        # Refresh user from database
        self.user.refresh_from_db()
        self.assertTrue(self.user.is_active)
        
        # Token should be deleted
        with self.assertRaises(EmailVerificationToken.DoesNotExist):
            EmailVerificationToken.objects.get(pk=self.token.pk)
    
    def test_verification_expired(self):
        """Test expired token verification"""
        # Set token creation time to 25 hours ago
        self.token.created_at = timezone.now() - timedelta(hours=25)
        self.token.save()
        
        url = reverse('account:verify_email', args=[str(self.token.token)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Verification Failed')
        
        # User should still be inactive
        self.user.refresh_from_db()
        self.assertFalse(self.user.is_active)
    
    def test_verification_invalid(self):
        """Test invalid token verification"""
        import uuid
        url = reverse('account:verify_email', args=[str(uuid.uuid4())])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Verification Failed')
        