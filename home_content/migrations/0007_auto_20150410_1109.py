# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_content', '0006_auto_20150410_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homesection',
            name='template',
            field=models.CharField(default=b's', max_length=50, choices=[(b'billboard', b'Billboards'), (b'mini_billboard_1', b'Mini Billboards Option 1'), (b'mini_billboard_2', b'Mini Billboards Option 2'), (b'1_col', b'1 Column Free Form'), (b'2_col', b'2 Column Free Form')]),
            preserve_default=True,
        ),
    ]
