# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page_content', '0002_auto_20150406_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagesection',
            name='image',
        ),
    ]
