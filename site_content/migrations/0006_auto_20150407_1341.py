# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0005_auto_20150407_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagramname',
            name='name',
            field=models.CharField(default=' ', max_length=400),
            preserve_default=False,
        ),
    ]
