
from . models import *

def reset_today_scores():
    reset_data = Hotel.objects.update(votes = 0)

def winners_history():
    hotel_data = Hotel.objects.order_by('-votes').first()
    data = history_winner(winner=hotel_data)
    data.save() 


def user_votes_renew():
    reset_data = CustomUser.objects.update(max_votes = 2.00)

