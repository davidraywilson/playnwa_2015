# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site', models.OneToOneField(default=1, to='sites.Site', help_text=b'Choose which site you want this link to appear on')),
            ],
            options={
                'verbose_name': 'Footer',
                'verbose_name_plural': 'Footer',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FooterSocialLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=200)),
                ('image', filebrowser.fields.FileBrowseField(max_length=400)),
                ('link', models.URLField()),
                ('order', models.IntegerField(default=1)),
                ('parent', models.ForeignKey(to='page_content.Footer')),
            ],
            options={
                'ordering': ('order', 'label'),
                'verbose_name': 'Social Link',
                'verbose_name_plural': 'Social Links',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', filebrowser.fields.FileBrowseField(help_text=b'Transparent .png', max_length=400, null=True, blank=True)),
                ('site', models.OneToOneField(default=1, to='sites.Site', help_text=b'Choose which site you want this link to appear on')),
            ],
            options={
                'verbose_name': 'Logo',
                'verbose_name_plural': 'Logo',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=400)),
                ('template', models.CharField(blank=True, max_length=50, null=True, choices=[(b'1_col', b'1 Column'), (b'2_col', b'2 Column'), (b'2_col_left', b'2 Column Wide Left'), (b'2_col_right', b'2 Column Wide Right')])),
                ('image', filebrowser.fields.FileBrowseField(help_text=b'At least 1140px wide', max_length=400, null=True, verbose_name=b'Section image', blank=True)),
                ('display_order', models.IntegerField(default=1)),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('display_order', 'label'),
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WebPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('template_choice', models.CharField(blank=True, max_length=50, null=True, choices=[(b'contact', b'Contact')])),
                ('label', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('meta_title', models.CharField(help_text=b'This shows at the top of the browser, usually in the tab.', max_length=100, null=True, blank=True)),
                ('meta_description', models.CharField(max_length=500, null=True, blank=True)),
                ('meta_tags', models.CharField(max_length=500, null=True, blank=True)),
                ('image_cover', filebrowser.fields.FileBrowseField(help_text=b'Roughly 1400px by 400px', max_length=400, null=True, verbose_name=b'Cover image', blank=True)),
                ('is_published', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('site', models.ForeignKey(default=1, to='sites.Site', help_text=b'Choose which site you want this Page to appear on')),
            ],
            options={
                'ordering': ('label',),
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pagesection',
            name='page',
            field=models.ForeignKey(to='page_content.WebPage'),
            preserve_default=True,
        ),
    ]
