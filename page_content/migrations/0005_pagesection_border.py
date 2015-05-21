# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page_content', '0004_auto_20150410_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagesection',
            name='border',
            field=models.CharField(help_text=b'Example: 1px solid #3EBFAC', max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
