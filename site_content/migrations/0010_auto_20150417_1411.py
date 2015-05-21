# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0009_auto_20150407_1446'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logo',
            old_name='image',
            new_name='image_desktop',
        ),
        migrations.AddField(
            model_name='logo',
            name='image_mobile',
            field=filebrowser.fields.FileBrowseField(help_text=b'Transparent .png', max_length=400, null=True, blank=True),
            preserve_default=True,
        ),
    ]
