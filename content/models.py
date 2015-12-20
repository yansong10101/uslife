from django.db import models


class FeatureGroupManager(models.Manager):
    """
        create new feature group:
        1. add to administration permission model
    """
    def create_feature_group(self, **kwargs):
        feature_group = self.create(**kwargs)
        return feature_group

    def get_queryset(self, is_active=True):
        return super(FeatureGroupManager, self).get_queryset().filter(is_active=is_active)


class FeatureGroup(models.Model):
    feature_name = models.CharField(max_length=150)
    display_name = models.CharField(max_length=150, blank=True)
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
        feature = self.create(**kwargs)
        return feature

    def get_queryset(self, is_active=True):
        return super(FeatureManager, self).get_queryset().filter(is_active=is_active)


class Feature(models.Model):
    feature_group = models.ForeignKey(FeatureGroup, related_name='sub_feature_feature_group')
    feature_name = models.CharField(max_length=150)
    display_name = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    features = FeatureManager()

    def __str__(self):
        return self.feature_name


class PermissionManager(models.Manager):

    def create_permission(self, **kwargs):
        can_add = self.create(permission_type='a', **kwargs)
        can_delete = self.create(permission_type='d', **kwargs)
        can_read = self.create(permission_type='r', **kwargs)
        can_write = self.create(permission_type='w', **kwargs)
        return can_add, can_delete, can_read, can_write

    def get_queryset(self):
        return super(PermissionManager, self).get_queryset().filter(is_active=True)


class Permission(models.Model):
    """
        Only insert rows when create new features and feature groups
    """
    PERMISSION_TYPE = (
        ('a', 'add'),
        ('d', 'delete'),
        ('r', 'read'),
        ('w', 'write'),
    )
    feature = models.ForeignKey(Feature, related_name='feature_permission')
    permission_name = models.CharField(max_length=255)
    is_feature_group = models.BooleanField(default=False)
    permission_type = models.CharField(choices=PERMISSION_TYPE, max_length=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.permission_name


class PermissionGroupManager(models.Manager):

    def create_permission_group(self, permission_list=None, **kwargs):
        if permission_list:
            permission_group = self.create(**kwargs)
            for permission in permission_list:
                permission_group.permission.add(permission)
            return permission_group
        return None

    def get_queryset(self):
        return super(PermissionGroupManager, self).get_queryset().filter(is_active=True)


class PermissionGroup(models.Model):
    """
        insert rows:
        1. new feature added
        2. org president grant sub admin users
    """
    permission = models.ManyToManyField(Permission, related_name='group_permission')
    group_name = models.CharField(max_length=150)
    is_org_admin = models.BooleanField(default=True)
    is_president = models.BooleanField(default=False)
    is_super_user = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.group_name