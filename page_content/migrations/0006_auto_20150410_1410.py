# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page_content', '0005_pagesection_border'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagesection',
            name='template',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'1_col', b'1 Column'), (b'1_col_center', b'1 Column Center'), (b'2_col_left', b'2 Column Wide Left'), (b'2_col_right', b'2 Column Wide Right'), (b'3_col', b'3 Column'), (b'break', b'Divider Line')]),
            preserve_default=True,
        ),
    ]
