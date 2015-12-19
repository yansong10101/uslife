# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20151217_0618'),
        ('administration', '0004_auto_20151211_0824'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrgAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], unique=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=50)),
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
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='university',
            name='feature',
            field=models.ManyToManyField(related_name='org_feature', null=True, to='content.Feature'),
        ),
        migrations.AddField(
            model_name='orgadmin',
            name='university',
            field=models.ForeignKey(related_name='org_admin_university', to='administration.University'),
        ),
    ]
