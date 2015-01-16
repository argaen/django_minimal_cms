# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20150109_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='icon',
            field=models.CharField(help_text="Icons are built from font-awesome. Choose one from <a href='http://fortawesome.github.io/Font-Awesome/icons/'>fontawesome page</a>. Example, if you like the 'fa-users' icon, just write fa-users in this field", max_length=20, null=True, verbose_name='Icon', blank=True),
            preserve_default=True,
        ),
    ]
