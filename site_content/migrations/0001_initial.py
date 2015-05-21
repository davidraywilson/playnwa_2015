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
            name='InstagramName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', filebrowser.fields.FileBrowseField(help_text=b'Transparent .png', max_length=400, null=True, blank=True)),
                ('site', models.OneToOneField(default=1, to='sites.Site', help_text=b'Choose which site you want this link to appear on')),
            ],
            options={
                'verbose_name': 'Instagram Name',
                'verbose_name_plural': 'Instagram Names',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', filebrowser.fields.FileBrowseField(help_text=b'Transparent .png', max_length=400, null=True, blank=True)),
                ('site', models.OneToOneField(default=1, to='sites.Site', help_text=b'Choose which site you want this link to appear on')),
            ],
            options={
                'verbose_name': 'Logo',
                'verbose_name_plural': 'Logos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SiteColor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', filebrowser.fields.FileBrowseField(help_text=b'Hex code starting with #. Ex: #219CDC', max_length=7)),
                ('site', models.OneToOneField(default=1, to='sites.Site', help_text=b'Choose which site you want this link to appear on')),
            ],
            options={
                'verbose_name': 'Site Color',
                'verbose_name_plural': 'Site Colors',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=200)),
                ('image', filebrowser.fields.FileBrowseField(max_length=400)),
                ('link', models.URLField()),
                ('order', models.IntegerField(default=1)),
                ('is_published', models.BooleanField(default=True)),
                ('site', models.ForeignKey(default=1, to='sites.Site', help_text=b'Choose which site you want this link to appear on')),
            ],
            options={
                'ordering': ('order', 'label'),
                'verbose_name': 'Social Link',
                'verbose_name_plural': 'Social Links',
            },
            bases=(models.Model,),
        ),
    ]
