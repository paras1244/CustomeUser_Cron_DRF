from django.contrib import admin
from .models import Hotel,CustomUser,history_winner
# Register your models here.

@admin.register(Hotel)
class hotel(admin.ModelAdmin):
    list_display = ['id','name', 'address', 'votes']

@admin.register(CustomUser)
class hotel(admin.ModelAdmin):
    list_display = ['username','max_votes','id', 'username']

@admin.register(history_winner)
class history_winners(admin.ModelAdmin):
    list_display = ['winner',  'created']