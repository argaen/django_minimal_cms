# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_auto_20150114_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='subtitle',
            field=models.CharField(max_length=200, verbose_name='Subtitle', blank=True),
            preserve_default=True,
        ),
    ]
