from django.core.management.base import BaseCommand

from hotel_vote.utils import reset_today_scores


class Command(BaseCommand):
    help = "reser_today_score"

    def handle(self, *args, **options):
        reset_today_scores()

