# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='USLifeAdmin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, parent_link=True, to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False)),
                ('user_role', models.CharField(max_length=50, blank=True, choices=[(1, 'university_president'), (2, 'university_admin')])),
                ('org_name', models.ForeignKey(related_name='administration_uslifeadmin_related', to='administration.University')),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='USLifeCustomer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, parent_link=True, to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False)),
                ('org_name', models.ForeignKey(related_name='administration_uslifecustomer_related', to='administration.University')),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
