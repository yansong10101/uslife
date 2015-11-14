__author__ = 'yzhang'

from django.db import models
from django.contrib.auth.models import User


class LifeUserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='user_profile')
    first_username = models.CharField(max_length=50, blank=True)
    last_username = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return User.username
