from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from account.models import EmailVerificationToken

class Command(BaseCommand):
    help = 'Mark all existing users as email verified'

    def add_arguments(self, parser):
        parser.add_argument(
            '--all',
            action='store_true',
            help='Mark all users as verified',
        )

    def handle(self, *args, **kwargs):
        mark_all = kwargs['all']
        
        if mark_all:
            # Get all users
            users = User.objects.all()
            
            # Set all users as active
            count = users.update(is_active=True)
            
            # Delete any verification tokens
            token_count = EmailVerificationToken.objects.all().delete()[0]
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully marked {count} users as verified')
            )
            self.stdout.write(
                self.style.SUCCESS(f'Removed {token_count} verification tokens')
            )
        else:
            # Only mark inactive users as active
            inactive_users = User.objects.filter(is_active=False)
            count = inactive_users.update(is_active=True)
            
            # Delete their verification tokens
            token_count = EmailVerificationToken.objects.filter(
                user__in=inactive_users
            ).delete()[0]
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully marked {count} inactive users as verified')
            )
            self.stdout.write(
                self.style.SUCCESS(f'Removed {token_count} verification tokens')
            )
            