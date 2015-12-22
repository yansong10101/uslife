# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('content', '0001_initial'), ('content', '0002_auto_20151217_0618'), ('content', '0003_auto_20151217_0829'), ('content', '0004_permission_permissiongroup')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureGroup',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('feature_name', models.CharField(max_length=150)),
                ('display_name', models.CharField(max_length=150, blank=True)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('feature_name', models.CharField(max_length=150)),
                ('display_name', models.CharField(max_length=150, blank=True)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('feature_group', models.ForeignKey(related_name='sub_feature_feature_group', to='content.FeatureGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('permission_name', models.CharField(max_length=255)),
                ('is_feature_group', models.BooleanField(default=False)),
                ('permission_type', models.CharField(max_length=2, choices=[('a', 'add'), ('d', 'delete'), ('r', 'read'), ('w', 'write')])),
                ('is_active', models.BooleanField(default=True)),
                ('feature', models.ForeignKey(related_name='feature_permission', to='content.Feature')),
            ],
        ),
        migrations.CreateModel(
            name='PermissionGroup',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('group_name', models.CharField(max_length=150)),
                ('is_org_admin', models.BooleanField(default=True)),
                ('is_president', models.BooleanField(default=False)),
                ('is_super_user', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('permission', models.ManyToManyField(related_name='group_permission', to='content.Permission')),
            ],
        ),
    ]
