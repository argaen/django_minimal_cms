# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20150113_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='times_cited',
            field=models.PositiveIntegerField(default=0, verbose_name='Times cited', blank=True),
            preserve_default=True,
        ),
    ]
