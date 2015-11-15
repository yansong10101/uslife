# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('org_name', models.CharField(max_length=225)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
