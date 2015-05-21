# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0007_auto_20150407_1439'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instagram',
            options={'verbose_name': 'Instagram', 'verbose_name_plural': 'Instagrams'},
        ),
        migrations.AlterField(
            model_name='instagram',
            name='link',
            field=models.URLField(help_text=b'Link to your profile'),
            preserve_default=True,
        ),
    ]
