# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('site_content', '0006_auto_20150407_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instagram',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(help_text=b'This is only used in the admin', max_length=100)),
                ('link', models.CharField(help_text=b'Link to your profile', max_length=400)),
                ('instagram_id', models.CharField(help_text=b'You can get your ID here ->  http://jelled.com/instagram/lookup-user-id', max_length=100)),
                ('site', models.OneToOneField(default=1, to='sites.Site', help_text=b'Choose which site you want this link to appear on')),
            ],
            options={
                'verbose_name': 'Instagram Name',
                'verbose_name_plural': 'Instagram Names',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='instagramname',
            name='site',
        ),
        migrations.DeleteModel(
            name='InstagramName',
        ),
    ]
