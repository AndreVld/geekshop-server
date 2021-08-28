from django.core.management.base import BaseCommand
from users.models import User, UserProfileInfo


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            users_profile = UserProfileInfo.objects.create(user=user)
            users_profile.save()
