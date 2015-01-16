# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('contenttypes', '0001_initial'),
        ('filer', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('abstract', models.TextField(verbose_name='Abstract')),
                ('authors', models.CharField(max_length=500, verbose_name='Authors')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('meta_keywords', models.CharField(help_text='Comma separated list', max_length=500, verbose_name='Meta keywords')),
                ('meta_author', models.CharField(max_length=100, verbose_name='Meta author')),
                ('meta_description', models.CharField(max_length=155, verbose_name='Meta description')),
                ('google_analytics', models.CharField(max_length=50, verbose_name='Google Analytics')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Researcher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('last_name', models.CharField(max_length=20, verbose_name='Last name')),
                ('photo', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='filer.Image', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('background_color', models.CharField(help_text=b'#xxxxxx', max_length=9, verbose_name='Background color')),
                ('content', models.TextField(help_text='If you selected a page content, leave this blank. This field is for static contents only', null=True, verbose_name='Content', blank=True)),
                ('content_type', models.ForeignKey(verbose_name='Page content', blank=True, to='contenttypes.ContentType', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SectionOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField()),
                ('project', models.ForeignKey(to='projects.Project')),
                ('section', models.ForeignKey(to='projects.Section')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='project',
            name='sections',
            field=models.ManyToManyField(to='projects.Section', verbose_name='Sections', through='projects.SectionOrder'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='site',
            field=models.OneToOneField(verbose_name='Site', to='sites.Site', help_text='Domain where the project belongs'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='authors_local',
            field=models.ManyToManyField(to='projects.Researcher', verbose_name='Authors local'),
            preserve_default=True,
        ),
    ]
