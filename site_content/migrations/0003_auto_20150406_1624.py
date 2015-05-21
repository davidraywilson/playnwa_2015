# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0002_auto_20150406_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sociallink',
            name='image_dark',
            field=filebrowser.fields.FileBrowseField(default='/', max_length=400, verbose_name=b'Dark image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='image_light',
            field=filebrowser.fields.FileBrowseField(default='/media', max_length=400, verbose_name=b'Light image'),
            preserve_default=False,
        ),
    ]
