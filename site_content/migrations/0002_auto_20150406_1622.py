# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sociallink',
            name='image',
        ),
        migrations.AddField(
            model_name='sociallink',
            name='image_dark',
            field=filebrowser.fields.FileBrowseField(max_length=400, null=True, verbose_name=b'Dark image', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sociallink',
            name='image_light',
            field=filebrowser.fields.FileBrowseField(max_length=400, null=True, verbose_name=b'Light image', blank=True),
            preserve_default=True,
        ),
    ]
