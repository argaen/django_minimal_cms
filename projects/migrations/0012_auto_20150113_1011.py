# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20150112_1141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-published_on',)},
        ),
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Published'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='published_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 13, 10, 11, 41, 203718, tzinfo=utc), verbose_name='Published on'),
            preserve_default=False,
        ),
    ]
