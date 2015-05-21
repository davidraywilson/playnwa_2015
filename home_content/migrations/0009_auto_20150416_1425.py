# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_content', '0008_auto_20150414_1526'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='billboard',
            options={'ordering': ('site', 'order', '-publish_date'), 'verbose_name': 'Billboard', 'verbose_name_plural': 'Billboards'},
        ),
        migrations.AlterModelOptions(
            name='homesection',
            options={'ordering': ('site', 'order'), 'verbose_name': 'Section', 'verbose_name_plural': 'Sections'},
        ),
        migrations.AlterModelOptions(
            name='minibillboard',
            options={'ordering': ('section', 'order', 'headline'), 'verbose_name': 'Mini Billboard', 'verbose_name_plural': 'Mini Billboards'},
        ),
        migrations.RemoveField(
            model_name='minibillboard',
            name='site',
        ),
    ]
