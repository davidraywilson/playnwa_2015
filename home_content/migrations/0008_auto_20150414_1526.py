# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_content', '0007_auto_20150410_1109'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='minibillboard',
            options={'ordering': ('site', 'section', 'order', 'headline'), 'verbose_name': 'Mini Billboard', 'verbose_name_plural': 'Mini Billboards'},
        ),
    ]
