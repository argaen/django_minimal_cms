# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_article_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sectionorder',
            options={'ordering': ('order',), 'verbose_name': 'Section', 'verbose_name_plural': 'Sections'},
        ),
        migrations.AddField(
            model_name='article',
            name='doi',
            field=models.CharField(default=1, max_length=50, verbose_name='DOI'),
            preserve_default=False,
        ),
    ]
