# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_content', '0003_minibillboard_section'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='minibillboard',
            options={'ordering': ('order', 'label'), 'verbose_name': 'Mini Billboard', 'verbose_name_plural': 'Mini Billboards'},
        ),
        migrations.RemoveField(
            model_name='minibillboard',
            name='expire_date',
        ),
        migrations.RemoveField(
            model_name='minibillboard',
            name='publish_date',
        ),
        migrations.RemoveField(
            model_name='minibillboard',
            name='size',
        ),
        migrations.RemoveField(
            model_name='minibillboard',
            name='video',
        ),
        migrations.AddField(
            model_name='minibillboard',
            name='description',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='minibillboard',
            name='headline',
            field=models.CharField(default=' ', max_length=75),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homesection',
            name='template',
            field=models.CharField(default=b's', max_length=50, choices=[(b'billboard', b'Billboards'), (b'mini_billboard 1', b'Mini Billboards Option 1'), (b'mini_billboard 2', b'Mini Billboards Option 2'), (b'1_col', b'1 Column Free Form'), (b'2_col', b'2 Column Free Form'), (b'map', b'Map')]),
            preserve_default=True,
        ),
    ]
