# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page_content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footer',
            name='site',
        ),
        migrations.RemoveField(
            model_name='footersociallink',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Footer',
        ),
        migrations.DeleteModel(
            name='FooterSocialLink',
        ),
        migrations.RemoveField(
            model_name='logo',
            name='site',
        ),
        migrations.DeleteModel(
            name='Logo',
        ),
    ]
