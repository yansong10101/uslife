from django.db import models
from django.shortcuts import get_object_or_404


class FeatureGroupManager(models.Manager):
    """
        create new feature group:
        1. add to administration permission model
    """
    def create_feature_group(self, **kwargs):
        feature_group = self.create(**kwargs)
        return feature_group

    def get_queryset(self, is_active=True, **kwargs):
        return super(FeatureGroupManager, self).get_queryset().filter(is_active=is_active, **kwargs)


class FeatureGroup(models.Model):
    feature_name = models.CharField(max_length=150, unique=True)
    display_name = models.CharField(max_length=150, blank=True)
    description_wiki_key = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    feature_groups = FeatureGroupManager()

    def __str__(self):
        return self.feature_name


class FeatureManager(models.Manager):
    """
        create new feature:
        1. add to administration permission model
    """
    def create_feature(self, **kwargs):
        # FIXME : update all universities to add this new feature
        feature = self.create(**kwargs)
        Permission.permissions.create_permission(feature)   # create corresponding permissions based on feature
        return feature

    def get_queryset(self, is_active=True):
        return super(FeatureManager, self).get_queryset().filter(is_active=is_active)


class Feature(models.Model):
    feature_group = models.ForeignKey(FeatureGroup, related_name='feature_group')
    feature_name = models.CharField(max_length=150, unique=True)
    display_name = models.CharField(max_length=150, blank=True)
    description_wiki_key = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    features = FeatureManager()

    def __str__(self):
        return self.feature_name


class PermissionManager(models.Manager):
    PERMISSION_NAME_SUFFIX = {
        'r': 'ReadOnlyAccess',
        'f': 'FullAccess',
    }

    def create_permission(self, feature, **kwargs):
        if not isinstance(feature, Feature):
            return  # TODO : add error object return error msg
        feature_name = feature.feature_name
        read_only = self.create(feature=feature, permission_name=self.make_permission_name(feature_name, 'r'),
                                permission_type='r', **kwargs)
        full_access = self.create(feature=feature, permission_name=self.make_permission_name(feature_name, 'f'),
                                  permission_type='f', **kwargs)
        return read_only, full_access

    def get_queryset(self, **kwargs):
        return super(PermissionManager, self).get_queryset().filter(is_active=True, **kwargs)

    def make_permission_name(self, feature_name, permission_type):
        return ''.join(feature_name.title().split()) + self.PERMISSION_NAME_SUFFIX[permission_type]


class Permission(models.Model):
    """
        Only do insertion when create new features and feature groups
    """
    PERMISSION_TYPE = (
        ('r', 'read only'),
        ('f', 'full access'),
    )
    feature = models.ForeignKey(Feature, related_name='feature_permission')
    permission_name = models.CharField(max_length=255)
    permission_type = models.CharField(choices=PERMISSION_TYPE, max_length=2, default='r')
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    permissions = PermissionManager()

    def __str__(self):
        return self.permission_name


class PermissionGroupManager(models.Manager):

    def create_permission_group(self, permission_list=None, **kwargs):
        permission_group = self.create(**kwargs)
        if permission_list:
            for permission_id in permission_list:
                permission = Permission.permissions.get(pk=permission_id)
                if isinstance(permission, Permission):
                    permission_group.permission.add(permission)
        return permission_group

    @staticmethod
    def update_permissions(permission_group, permission_list):
        origin_permissions = permission_group.permission.all()
        # remove permissions which are in group but not in passed-in list
        for permission in origin_permissions:
            if permission.pk not in permission_list:
                permission_group.permission.remove(permission)
        # add permissions which are not in passed-in list
        for permission_id in permission_list:
            if not permission_group.permission.filter(pk=permission_id).exists():
                permission = get_object_or_404(Permission, pk=permission_id)
                permission_group.permission.add(permission)

    def get_queryset(self, is_active=True, **kwargs):
        return super(PermissionGroupManager, self).get_queryset().filter(is_active=is_active, **kwargs)


class PermissionGroup(models.Model):
    """
        insert rows:
        1. new feature added
        2. org president grant sub admin users
    """
    USER_LEVEL = (
        (0, '游客'),
        (1, '在校生'),
        (2, '临校生'),
        (3, '毕业生'),
        (4, '赞助商'),
        (5, '黑名单'),
    )
    USER_LEVEL_MAP = {
        0, '游客',
        1, '在校生',
        2, '临校生',
        3, '毕业生',
        4, '赞助商',
        5, '黑名单',
    }
    permission = models.ManyToManyField(Permission, related_name='group_permission')
    group_name = models.CharField(max_length=150)
    is_org_admin = models.BooleanField(default=True)
    is_super_user = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    user_level = models.IntegerField(default=0)

    objects = models.Manager()
    permission_groups = PermissionGroupManager()

    def __str__(self):
        return self.group_name

    def __unicode__(self):
        return self.__str__()
