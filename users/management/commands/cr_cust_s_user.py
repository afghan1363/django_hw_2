from django.core.management import BaseCommand
from users.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='afghan1363@ya.ru',
            first_name='admin',
            last_name='admins'
        )
        user.set_password('SkyPro123')
        user.save()
