# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '__first__'),
        ('projects', '0021_remove_article_times_cited'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='background_image',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='filer.Image', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='background_color',
            field=models.CharField(help_text=b'#xxxxxx', max_length=9, null=True, verbose_name='Background color', blank=True),
            preserve_default=True,
        ),
    ]
