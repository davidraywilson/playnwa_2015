# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page_content', '0007_auto_20150414_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='template_choice',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'contact', b'Contact'), (b'events', b'Event Landing Page'), (b'member_login', b'Member Login')]),
            preserve_default=True,
        ),
    ]
