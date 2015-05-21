# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home_content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billboard',
            name='header',
        ),
        migrations.RemoveField(
            model_name='billboard',
            name='sub_header',
        ),
        migrations.AddField(
            model_name='billboard',
            name='content',
            field=models.TextField(default=' ', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='billboard',
            name='image',
            field=filebrowser.fields.FileBrowseField(help_text=b'Approximately 1000px wide (Keep subject towards the middle of image for best viewing on mobile.)', max_length=200),
            preserve_default=True,
        ),
    ]
