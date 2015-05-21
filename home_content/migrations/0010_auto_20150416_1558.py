# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_content', '0009_auto_20150416_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homesection',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
