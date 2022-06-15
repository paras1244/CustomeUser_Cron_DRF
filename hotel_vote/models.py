from pyexpat import model
import re
from django.db import models

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
# Create your models here.

class TaggUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractUser):
    max_votes = models.CharField(max_length=3)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    objects = TaggUserManager()

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
            models.Index(fields=["username"]),
            models.Index(fields=["max_votes"]),
        ]

class Hotel(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    votes = models.FloatField(default=0)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'name'

class history_winner(models.Model):
    winner = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    def __str__(self):
        return str(self.winner)
