# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_permission_permissiongroup'),
        ('administration', '0007_auto_20151217_0829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='feature',
        ),
        migrations.RemoveField(
            model_name='permissiongroup',
            name='permission',
        ),
        migrations.AddField(
            model_name='customer',
            name='permission',
            field=models.ManyToManyField(related_name='customer_permission', to='content.Permission'),
        ),
        migrations.AddField(
            model_name='orgadmin',
            name='permission',
            field=models.ManyToManyField(related_name='org_permission', to='content.Permission'),
        ),
        migrations.DeleteModel(
            name='Permission',
        ),
        migrations.DeleteModel(
            name='PermissionGroup',
        ),
    ]
