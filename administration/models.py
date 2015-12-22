from django.db import models
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, User,
)
from content.models import Feature, Permission, PermissionGroup


class UniversityManager(models.Manager):
    """
        create new university:
        1. with all default features (recommend only toggle existing features)
        2. create a super user (president)
        3. grant all permissions to president
        4. can create group
    """
    def create_university(self, **kwargs):
        pass

    def get_queryset(self, is_active=True):
        return super(UniversityManager, self).get_queryset().filter(is_active=is_active)


class University(models.Model):
    feature = models.ManyToManyField(Feature, related_name='org_feature')
    university_name = models.CharField(max_length=255)
    university_code = models.CharField(max_length=50)
    short_name = models.CharField(max_length=50, blank=True)
    display_name = models.CharField(max_length=255, blank=True)
    address_1 = models.CharField(max_length=255, blank=True)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    contact_email = models.EmailField(blank=True)
    support_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    official_website = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    universities = UniversityManager()

    def __str__(self):
        return self.university_name

    def has_relationship(self):
        return self.is_active


class OrgAdminQuerySet(models.QuerySet):

    def org_president(self, **kwargs):
        return self.filter(is_president=True, is_active=True, **kwargs)

    def org_admin(self, **kwargs):
        return self.filter(is_president=False, is_active=True, **kwargs)


class OrgAdminManager(BaseUserManager):

    def get_queryset(self):
        return OrgAdminQuerySet(self.model, using=self._db).filter(is_active=True)

    def org_president(self, **kwargs):
        return self.get_queryset().org_president(**kwargs)

    def org_admin(self, **kwargs):
        return self.get_queryset().org_admin(**kwargs)


class OrgAdmin(AbstractBaseUser):
    university = models.ForeignKey(University, related_name='org_admin_university')
    permission = models.ManyToManyField(Permission, related_name='org_permission')
    permission_group = models.ManyToManyField(PermissionGroup, related_name='org_permission_group')
    username = models.CharField(_('username'), max_length=50, unique=True,
                                help_text=_('Required. 30 characters or fewer. Letters, digits and '
                                            '@/./+/-/_ only.'),
                                validators=[
                                    validators.RegexValidator(r'^[\w.@+-]+$',
                                                              _('Enter a valid username. '
                                                                'This value may contain only letters, numbers '
                                                                'and @/./+/-/_ characters.'), 'invalid'),
                                ],
                                error_messages={
                                    'unique': _("A user with that username already exists."),
                            })
    email = models.EmailField(verbose_name='email address', max_length=255)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified_date = models.DateTimeField(auto_now=True, editable=False)
    last_login_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_president = models.BooleanField(default=False, editable=False)
    is_admin = models.BooleanField(default=False, editable=False)
    prior_level = models.IntegerField(default=0)

    objects = models.Manager()
    org_admins = OrgAdminManager()

    USERNAME_FIELD = 'username'

    def get_full_name(self):
        return self.get_username()

    def get_short_name(self):
        return self.get_username()

    def __str__(self):
        return self.get_full_name()


class CustomerQuerySet(models.QuerySet):

    def get_customers(self, is_active=True, **kwargs):
        return self.filter(is_active=is_active, **kwargs)

    def unauthorized_user(self):
        return self.get_customers(approval_level=0)

    def authorized_user(self):
        return self.get_customers(approval_level=1)

    def alumni(self):
        return self.get_customers(approval_level=2)


class CustomerManager(BaseUserManager):

    def get_queryset(self):
        return CustomerQuerySet(self.model, using=self._db)

    def get_customer(self, **kwargs):
        return self.get_customer(**kwargs)

    def unauthorized_user(self):
        return self.get_queryset().unauthorized_user()

    def authorized_user(self):
        return self.get_queryset().authorized_user()

    def alumni(self):
        return self.get_queryset().alumni()


class Customer(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified_date = models.DateTimeField(auto_now=True, editable=False)
    last_login_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False, editable=False)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    student_id = models.CharField(max_length=50, blank=True)
    offer_number = models.CharField(max_length=255, blank=True)
    photo_url = models.CharField(max_length=150, blank=True)
    is_approved = models.BooleanField(default=False)
    approval_level = models.IntegerField(default=0)

    USERNAME_FIELD = 'email'

    objects = models.Manager()
    customers = CustomerManager()

    def has_name(self):
        if not self.first_name and not self.last_name:
            return True
        return False

    def get_full_name(self):
        if self.has_name():
            return self.first_name, self.last_name
        return self.email

    def get_short_name(self):
        if self.has_name():
            return self.first_name
        return self.email.split('@')[0]

    @property
    def is_staff(self):
        return self.is_admin

    def inactive_user(self):
        self.is_active = False
        self.save()

    def update_password(self, password):
        self.set_password(password)

    def __str__(self):
        return self.email


class CustomerUPG(models.Model):
    """
    CustomerUPG == Customer University Permission Group
    """
    customer = models.ManyToManyField(Customer, related_name='customer_upg_customer')
    university = models.ManyToManyField(University, related_name='customer_upg_university')
    permission_group = models.ManyToManyField(PermissionGroup, related_name='customer_upg_permission_group')
    grant_level = models.IntegerField(default=0, verbose_name='grant user level')

    db_table = 'customer_university_permission'
