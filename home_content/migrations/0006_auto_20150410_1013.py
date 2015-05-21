# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_content', '0005_auto_20150409_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='homesection',
            name='border',
            field=models.CharField(help_text=b'Example: 1px solid #3EBFAC', max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homesection',
            name='template',
            field=models.CharField(default=b's', max_length=50, choices=[(b'billboard', b'Billboards'), (b'mini_billboard_1', b'Mini Billboards Option 1'), (b'mini_billboard_2', b'Mini Billboards Option 2'), (b'1_col', b'1 Column Free Form'), (b'2_col', b'2 Column Free Form'), (b'map', b'Map')]),
            preserve_default=True,
        ),
    ]
