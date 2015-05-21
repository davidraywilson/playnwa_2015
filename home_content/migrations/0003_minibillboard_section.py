# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_content', '0002_auto_20150407_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='minibillboard',
            name='section',
            field=models.ForeignKey(default=1, to='home_content.HomeSection'),
            preserve_default=False,
        ),
    ]
