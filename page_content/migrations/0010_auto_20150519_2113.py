# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page_content', '0009_auto_20150512_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='template_choice',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'contact', b'Contact'), (b'events', b'Events Landing Page'), (b'news', b'News Landing Page'), (b'find_space', b'Find Space'), (b'property_owners', b'Property Owners')]),
        ),
    ]
