# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20151217_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('permission_name', models.CharField(max_length=255)),
                ('is_feature_group', models.BooleanField(default=False)),
                ('permission_type', models.CharField(max_length=2, choices=[('a', 'add'), ('d', 'delete'), ('r', 'read'), ('w', 'write')])),
                ('is_active', models.BooleanField(default=True)),
                ('feature', models.ForeignKey(to='content.Feature', related_name='feature_permission')),
            ],
        ),
        migrations.CreateModel(
            name='PermissionGroup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('group_name', models.CharField(max_length=150)),
                ('is_org_admin', models.BooleanField(default=True)),
                ('is_president', models.BooleanField(default=False)),
                ('is_super_user', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('permission', models.ManyToManyField(related_name='group_permission', to='content.Permission')),
            ],
        ),
    ]
