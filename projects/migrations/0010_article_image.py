# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '__first__'),
        ('projects', '0009_auto_20150112_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='filer.Image', null=True),
            preserve_default=True,
        ),
    ]
