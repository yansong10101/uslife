from django.db import models
# from django.contrib.auth.models import User, AbstractUser, BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone


class University(models.Model):
    org_name = models.CharField(max_length=225)
    # org_code = models.IntegerField(verbose_name='university code', null=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.org_name


# class USLifeUser(User):
#     org = models.ForeignKey(University, related_name='%(app_label)s_%(class)s_related')
#
#     class Meta(User.Meta):
#         abstract = True


# class USLifeAdmin(USLifeUser):
#     ROLE_CHOICE = ((1, 'university_president'), (2, 'university_admin'))
#     user_role = models.CharField(max_length=50, choices=ROLE_CHOICE, blank=True)
#
#     def __str__(self):
#         return self.username + ' -- ' + self.user_role
#
#     class Meta:
#         verbose_name = 'Org Admin'


# class USLifeSubAdmin(USLifeUser):
#     class Meta(User.Meta):
#         # proxy = True
#         app_label = 'auth'
#         verbose_name = 'sub admin account'
#         verbose_name_plural = 'sub admin accounts'


# class USLifeCustomer(USLifeUser):
#
#     def __str__(self):
#         return self.username
#
#     class Meta:
#         verbose_name = 'Org Customer'


# class BaseWebAdmin(AbstractUser):
#     email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
#     university = models.ForeignKey(University, related_name='%(app_label)s_%(class)s_related')
#     is_active = models.BooleanField(default=True)
#     REQUIRED_FIELDS = ['email']
#
#     class Meta(AbstractUser.Meta):
#         abstract = True
#
#     def get_full_name(self):
#         return self.email
#
#     def get_short_name(self):
#         return self.email.split('@')[0]
#
#     def email_user(self, subject, message, from_email=None, **kwargs):
#         send_mail(subject, message, from_email, [self.email], **kwargs)
#
#     def __str__(self):
#         return self.email
#
#
# class SuperWebMaster(BaseWebAdmin):
#     is_staff = models.BooleanField(default=True)
#

# class MyUserManager(BaseUserManager):
#     def create_user(self, email, date_of_birth, password=None):
#         """
#         Creates and saves a User with the given email, date of
#         birth and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         user = self.model(
#             email=self.normalize_email(email),
#             date_of_birth=date_of_birth,
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, date_of_birth, password):
#         """
#         Creates and saves a superuser with the given email, date of
#         birth and password.
#         """
#         user = self.create_user(email,
#             password=password,
#             date_of_birth=date_of_birth
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
#
#
# class MyUser(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )
#     date_of_birth = models.DateField(default=timezone.now)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#
#     # first_name = models.CharField(max_length=30, blank=True)
#     # middle_name = models.CharField(max_length=30, blank=True)
#     # last_name = models.CharField(max_length=30, blank=True)
#     # date_joined = models.DateTimeField(default=timezone.now)
#
#     objects = MyUserManager()
#
#     USERNAME_FIELD = 'email'
#     # REQUIRED_FIELDS = ['date_of_birth']
#
#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         # Simplest possible answer: All admins are staff
#         return self.is_admin
#
#     def get_full_name(self):
#         # The user is identified by their email address
#         return self.email
#
#     def get_short_name(self):
#         # The user is identified by their email address
#         return self.email
#
#     def __str__(self):              # __unicode__ on Python 2
#         return self.email
#
#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True
#
#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True
