# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_researcher_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published_on',
            field=models.DateField(verbose_name='Published on'),
            preserve_default=True,
        ),
    ]
