# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0010_auto_20150417_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='image_desktop',
            field=filebrowser.fields.FileBrowseField(help_text=b'Transparent .png', max_length=400, null=True, verbose_name=b'Desktop image', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='logo',
            name='image_mobile',
            field=filebrowser.fields.FileBrowseField(help_text=b'Transparent .png', max_length=400, null=True, verbose_name=b'Mobile image', blank=True),
            preserve_default=True,
        ),
    ]
