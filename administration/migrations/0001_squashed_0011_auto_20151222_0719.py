# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    replaces = [('administration', '0001_initial'), ('administration', '0002_auto_20151126_0431'), ('administration', '0003_university'), ('administration', '0004_auto_20151211_0824'), ('administration', '0005_auto_20151217_0618'), ('administration', '0006_auto_20151217_0634'), ('administration', '0007_auto_20151217_0829'), ('administration', '0008_auto_20151217_0925'), ('administration', '0009_orgadmin_permission_group'), ('administration', '0010_auto_20151222_0704'), ('administration', '0011_auto_20151222_0719')]

    dependencies = [
        ('content', '0002_auto_20151217_0618'),
        ('content', '0004_permission_permissiongroup'),
        ('content', '0003_auto_20151217_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='email address')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False, editable=False)),
                ('first_name', models.CharField(max_length=50, blank=True)),
                ('last_name', models.CharField(max_length=50, blank=True)),
                ('approval_level', models.IntegerField(default=0)),
                ('is_approved', models.BooleanField(default=False)),
                ('last_login_date', models.DateTimeField(null=True, blank=True)),
                ('offer_number', models.CharField(max_length=255, blank=True)),
                ('photo_url', models.CharField(max_length=150, blank=True)),
                ('student_id', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=255)),
                ('university_code', models.CharField(max_length=50)),
                ('address_1', models.CharField(max_length=255, blank=True)),
                ('address_2', models.CharField(max_length=255, blank=True)),
                ('city', models.CharField(max_length=255, blank=True)),
                ('state', models.CharField(max_length=50, blank=True)),
                ('zip_code', models.CharField(max_length=10, blank=True)),
                ('display_name', models.CharField(max_length=255, blank=True)),
                ('contact_email', models.EmailField(max_length=254, blank=True)),
                ('contact_phone', models.CharField(max_length=20, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('official_website', models.URLField(blank=True)),
                ('short_name', models.CharField(max_length=50, blank=True)),
                ('support_email', models.EmailField(max_length=254, blank=True)),
                ('feature', models.ManyToManyField(to='content.Feature', related_name='org_feature')),
            ],
        ),
        migrations.CreateModel(
            name='OrgAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', verbose_name='username', unique=True, error_messages={'unique': 'A user with that username already exists.'}, max_length=50, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')])),
                ('email', models.EmailField(max_length=255, verbose_name='email address')),
                ('first_name', models.CharField(max_length=50, blank=True)),
                ('last_name', models.CharField(max_length=50, blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('last_login_date', models.DateTimeField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_president', models.BooleanField(default=False, editable=False)),
                ('is_admin', models.BooleanField(default=False, editable=False)),
                ('prior_level', models.IntegerField(default=0)),
                ('university', models.ForeignKey(related_name='org_admin_university', to='administration.University')),
                ('permission', models.ManyToManyField(to='content.Permission', related_name='org_permission')),
                ('permission_group', models.ManyToManyField(to='content.PermissionGroup', related_name='org_permission_group')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerUPG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grant_level', models.IntegerField(default=0, verbose_name='grant user level')),
                ('customer', models.ManyToManyField(to='administration.Customer', related_name='customer_upg_customer')),
                ('permission_group', models.ManyToManyField(to='content.PermissionGroup', related_name='customer_upg_permission_group')),
                ('university', models.ManyToManyField(to='administration.University', related_name='customer_upg_university')),
            ],
        ),
    ]
