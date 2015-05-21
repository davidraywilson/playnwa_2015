# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0004_auto_20150407_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitecolor',
            name='color',
            field=models.CharField(help_text=b'Hex code starting with #. Ex: #219CDC', max_length=7),
            preserve_default=True,
        ),
    ]
