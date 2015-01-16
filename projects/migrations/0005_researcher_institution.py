# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20150109_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='researcher',
            name='institution',
            field=models.CharField(default=1, max_length=100, verbose_name='Institution'),
            preserve_default=False,
        ),
    ]
