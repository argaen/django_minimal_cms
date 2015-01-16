# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_article_times_cited'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='content',
        ),
        migrations.AddField(
            model_name='sectionorder',
            name='content',
            field=models.TextField(help_text='If you selected a page content, leave this blank. This field is for static contents only', null=True, verbose_name='Content', blank=True),
            preserve_default=True,
        ),
    ]
