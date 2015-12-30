# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('feature_name', models.CharField(max_length=150, unique=True)),
                ('display_name', models.CharField(blank=True, max_length=150)),
                ('description_wiki_key', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeatureGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('feature_name', models.CharField(max_length=150, unique=True)),
                ('display_name', models.CharField(blank=True, max_length=150)),
                ('description_wiki_key', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('permission_name', models.CharField(max_length=255)),
                ('permission_type', models.CharField(choices=[('r', 'read only'), ('f', 'full access')], max_length=2, default='r')),
                ('is_active', models.BooleanField(default=True)),
                ('feature', models.ForeignKey(to='content.Feature', related_name='feature_permission')),
            ],
        ),
        migrations.CreateModel(
            name='PermissionGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('group_name', models.CharField(max_length=150)),
                ('is_org_admin', models.BooleanField(default=True)),
                ('is_super_user', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('user_level', models.IntegerField(default=0)),
                ('permission', models.ManyToManyField(to='content.Permission', related_name='group_permission')),
            ],
        ),
        migrations.AddField(
            model_name='feature',
            name='feature_group',
            field=models.ForeignKey(to='content.FeatureGroup', related_name='feature_group'),
        ),
    ]
