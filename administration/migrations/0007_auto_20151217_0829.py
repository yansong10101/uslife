# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20151217_0829'),
        ('administration', '0006_auto_20151217_0634'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('permission_name', models.CharField(max_length=255)),
                ('is_feature_group', models.BooleanField(default=False)),
                ('permission_type', models.CharField(max_length=2, choices=[('a', 'add'), ('d', 'delete'), ('r', 'read'), ('w', 'write')])),
                ('feature', models.ForeignKey(related_name='feature_permission', to='content.Feature')),
            ],
        ),
        migrations.CreateModel(
            name='PermissionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('group_name', models.CharField(max_length=150)),
                ('is_org_admin', models.BooleanField(default=True)),
                ('is_president', models.BooleanField(default=False)),
                ('is_super_user', models.BooleanField(default=False)),
                ('permission', models.ManyToManyField(related_name='group_permission', to='administration.Permission')),
            ],
        ),
        migrations.RenameField(
            model_name='university',
            old_name='cn_name',
            new_name='display_name',
        ),
    ]
