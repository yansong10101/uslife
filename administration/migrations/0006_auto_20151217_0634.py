# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0005_auto_20151217_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='feature',
            field=models.ManyToManyField(related_name='org_feature', to='content.Feature'),
        ),
    ]
