from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, User,
)


class University(models.Model):
    university_name = models.CharField(max_length=255)
    university_code = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=255, blank=True)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.university_name


class CustomerManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email.normalize_email(email),)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.model(email.normalize_email(email),)

        user.is_admin = True
        user.save(using=self._db)
        return user


class Customer(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified_date = models.DateTimeField(auto_now=True, editable=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False, editable=False)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email.split('@')[0]

    @property
    def is_staff(self):
        return self.is_admin
