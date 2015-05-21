# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0008_auto_20150407_1445'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instagram',
            options={'verbose_name': 'Instagram', 'verbose_name_plural': 'Instagram'},
        ),
    ]
