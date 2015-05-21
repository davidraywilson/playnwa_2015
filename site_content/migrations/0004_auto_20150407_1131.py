# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0003_auto_20150406_1624'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sociallink',
            options={'ordering': ('site', 'order', 'label'), 'verbose_name': 'Social Link', 'verbose_name_plural': 'Social Links'},
        ),
    ]
