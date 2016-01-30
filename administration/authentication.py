import binascii
import os

from administration.models import OrgAdmin, Customer
from api.lmb_cache import LMBCache
from rest_framework import authentication
from rest_framework import exceptions


class UserAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        username = request.META.get('X_USERNAME')
        if not username:
            return None
        try:
            user = OrgAdmin.objects.get(username=username) or Customer.objects.get(email=username)
        except Customer.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        return user

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    @classmethod
    def is_authenticate(cls, token):
        lmb_cache = LMBCache()
        if lmb_cache.is_exists(token):
            return True
        return False
