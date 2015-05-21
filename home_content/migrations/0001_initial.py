# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billboard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=200)),
                ('image', filebrowser.fields.FileBrowseField(help_text=b'Approximately 1000 px wide by 650 px tall. (Keep subject towards the middle of image for best viewing on mobile.)', max_length=200)),
                ('header', models.CharField(max_length=35, null=True, blank=True)),
                ('sub_header', models.CharField(max_length=100, null=True, blank=True)),
                ('link', models.CharField(max_length=200, null=True, blank=True)),
                ('is_published', models.BooleanField(default=True)),
                ('publish_date', models.DateField(db_index=True)),
                ('expire_date', models.DateField(null=True, blank=True)),
                ('order', models.IntegerField(default=1)),
                ('site', models.ForeignKey(default=1, to='sites.Site', help_text=b'Choose which site you want this Billboard to appear on')),
            ],
            options={
                'ordering': ('order', '-publish_date'),
                'verbose_name': 'Billboard',
                'verbose_name_plural': 'Billboards',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HomeSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=200)),
                ('template', models.CharField(default=b's', max_length=50, choices=[(b'billboard', b'Billboards'), (b'mini_billboard', b'Mini Billboards'), (b'1_col', b'1 Column Free Form'), (b'2_col', b'2 Column Free Form'), (b'map', b'Map')])),
                ('image_background', filebrowser.fields.FileBrowseField(help_text=b'Leave blank for white.', max_length=200, null=True, verbose_name=b'Background image', blank=True)),
                ('is_published', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=1, unique=True)),
                ('site', models.ForeignKey(default=1, to='sites.Site', help_text=b'Choose which site you want this Section to appear on')),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MiniBillboard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=200)),
                ('image', filebrowser.fields.FileBrowseField(max_length=200, null=True, blank=True)),
                ('video', models.CharField(help_text=b'Embed video from Vimeo (preferably) or YouTube.', max_length=500, null=True, blank=True)),
                ('size', models.CharField(default=b's', max_length=50, choices=[(b's', b'Small'), (b'l', b'Large')])),
                ('link', models.CharField(max_length=200, null=True, blank=True)),
                ('is_published', models.BooleanField(default=True)),
                ('publish_date', models.DateField(db_index=True)),
                ('expire_date', models.DateField(null=True, blank=True)),
                ('order', models.IntegerField(default=1)),
                ('site', models.ForeignKey(default=1, to='sites.Site', help_text=b'Choose which site you want this Mini Billboard to appear on')),
            ],
            options={
                'ordering': ('order', '-publish_date'),
                'verbose_name': 'Mini Billboard',
                'verbose_name_plural': 'Mini Billboards',
            },
            bases=(models.Model,),
        ),
    ]
