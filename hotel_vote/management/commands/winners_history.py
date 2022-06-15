from django.core.management.base import BaseCommand

from hotel_vote.utils import winners_history


class Command(BaseCommand):
    help = "winners_history"

    def handle(self, *args, **options):
        winners_history()

