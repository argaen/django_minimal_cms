# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20150112_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='researcher',
            name='email',
            field=models.EmailField(max_length=75, null=True, verbose_name='Email', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='researcher',
            name='twitter',
            field=models.CharField(max_length=30, null=True, verbose_name='Twitter', blank=True),
            preserve_default=True,
        ),
    ]
