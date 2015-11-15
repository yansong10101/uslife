__author__ = 'yzhang'

from django.db import models
from django.contrib.auth.models import User


class University(models.Model):
    org_name = models.CharField(max_length=225)
    created_date = models.DateField(auto_now_add=True, editable=False)
    modified_date = models.DateField(auto_now=True, editable=False)

    def __str__(self):
        return self.org_name


class USLifeUser(User):
    org_name = models.ForeignKey(University, related_name='%(app_label)s_%(class)s_related')

    class Meta(User.Meta):
        abstract = True


class USLifeAdmin(USLifeUser):
    ROLE_CHOICE = ((1, 'university_president'), (2, 'university_admin'))
    user_role = models.CharField(max_length=50, choices=ROLE_CHOICE, blank=True)

    def __str__(self):
        return self.username + ' -- ' + self.user_role


class USLifeCustomer(USLifeUser):

    def __str__(self):
        return self.username
