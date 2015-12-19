# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_university'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='approval_level',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_login_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='offer_number',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='photo_url',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='student_id',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='university',
            field=models.ForeignKey(to='administration.University', related_name='customer_university', null=True),
        ),
        migrations.AddField(
            model_name='university',
            name='cn_name',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='university',
            name='contact_email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='university',
            name='contact_phone',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='university',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='university',
            name='official_website',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='university',
            name='short_name',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='university',
            name='support_email',
            field=models.EmailField(max_length=254, blank=True),
        ),
    ]
