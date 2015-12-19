from django.db import models


class FeatureGroupManager(models.Manager):
    """
        create new feature group:
        1. add to administration permission model
    """

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
    permission_name = models.CharField(max_length=255)
    feature = models.ForeignKey(Feature, related_name='feature_permission')
    is_feature_group = models.BooleanField(default=False)
    permission_type = models.CharField(choices=PERMISSION_TYPE, max_length=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.permission_name


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