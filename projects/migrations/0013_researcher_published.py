# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20150113_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='researcher',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Published'),
            preserve_default=True,
        ),
    ]
