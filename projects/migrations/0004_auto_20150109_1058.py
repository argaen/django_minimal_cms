# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_section_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='project',
            field=models.ManyToManyField(to='projects.Project', verbose_name='Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='researcher',
            name='project',
            field=models.ManyToManyField(to='projects.Project', verbose_name='Project'),
            preserve_default=True,
        ),
    ]
