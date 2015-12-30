# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('last_login_date', models.DateTimeField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(editable=False, default=False)),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('student_id', models.CharField(blank=True, max_length=50)),
                ('offer_number', models.CharField(blank=True, max_length=255)),
                ('photo_url', models.CharField(blank=True, max_length=150)),
                ('is_approved', models.BooleanField(default=False)),
                ('approval_level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerUPG',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('grant_level', models.IntegerField(default=0, verbose_name='grant user level')),
                ('customer', models.ManyToManyField(to='administration.Customer', related_name='customer_upg_customer')),
                ('permission_group', models.ManyToManyField(to='content.PermissionGroup', related_name='customer_upg_permission_group')),
            ],
        ),
        migrations.CreateModel(
            name='OrgAdmin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username', error_messages={'unique': 'A user with that username already exists.'}, max_length=50, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')])),
                ('email', models.EmailField(max_length=255, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('last_login_date', models.DateTimeField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_president', models.BooleanField(editable=False, default=False)),
                ('is_admin', models.BooleanField(editable=False, default=False)),
                ('prior_level', models.IntegerField(default=0)),
                ('permission', models.ManyToManyField(to='content.Permission', related_name='org_permission')),
                ('permission_group', models.ManyToManyField(to='content.PermissionGroup', related_name='org_permission_group')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('university_name', models.CharField(max_length=255)),
                ('university_code', models.CharField(max_length=50)),
                ('short_name', models.CharField(blank=True, max_length=50)),
                ('display_name', models.CharField(blank=True, max_length=255)),
                ('address_1', models.CharField(blank=True, max_length=255)),
                ('address_2', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('zip_code', models.CharField(blank=True, max_length=10)),
                ('contact_email', models.EmailField(blank=True, max_length=254)),
                ('support_email', models.EmailField(blank=True, max_length=254)),
                ('contact_phone', models.CharField(blank=True, max_length=20)),
                ('official_website', models.URLField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('feature', models.ManyToManyField(to='content.Feature', related_name='org_feature')),
            ],
        ),
        migrations.AddField(
            model_name='orgadmin',
            name='university',
            field=models.ForeignKey(to='administration.University', related_name='org_admin_university'),
        ),
        migrations.AddField(
            model_name='customerupg',
            name='university',
            field=models.ManyToManyField(to='administration.University', related_name='customer_upg_university'),
        ),
    ]
