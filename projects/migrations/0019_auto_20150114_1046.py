# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_auto_20150113_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='first_page',
            field=models.CharField(default=1, max_length=20, verbose_name='First page / Article #'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='journal',
            field=models.CharField(default=1, max_length=500, verbose_name='Journal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='last_page',
            field=models.CharField(max_length=20, verbose_name='Last page', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='volume',
            field=models.CharField(max_length=100, verbose_name='volume', blank=True),
            preserve_default=True,
        ),
    ]
