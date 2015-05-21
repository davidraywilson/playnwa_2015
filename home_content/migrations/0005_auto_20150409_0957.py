# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_content', '0004_auto_20150409_0953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='minibillboard',
            options={'ordering': ('order', 'headline'), 'verbose_name': 'Mini Billboard', 'verbose_name_plural': 'Mini Billboards'},
        ),
        migrations.RemoveField(
            model_name='minibillboard',
            name='label',
        ),
    ]
