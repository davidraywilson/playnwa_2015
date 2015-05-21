# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page_content', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrimaryNavigation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('link_type', models.CharField(blank=True, max_length=50, null=True, choices=[(b'page', b'Page'), (b'custom', b'Link')])),
                ('link', models.CharField(max_length=200, null=True, blank=True)),
                ('is_published', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=1)),
                ('url_search_target', models.CharField(max_length=400, blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('page', models.ForeignKey(blank=True, to='page_content.WebPage', null=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='navigation.PrimaryNavigation', null=True)),
            ],
            options={
                'ordering': ('order', 'title'),
                'verbose_name': 'Primary Navigation',
                'verbose_name_plural': 'Primary Navigation',
            },
        ),
        migrations.CreateModel(
            name='UrlRedirect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_url', models.CharField(max_length=200)),
                ('to_url', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('from_url',),
                'verbose_name': 'Redirect',
                'verbose_name_plural': 'Redirects',
            },
        ),
    ]
