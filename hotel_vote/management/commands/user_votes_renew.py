from django.core.management.base import BaseCommand

from hotel_vote.utils import user_votes_renew


class Command(BaseCommand):
    help = "user_votes_renew"

    def handle(self, *args, **options):
        user_votes_renew()

