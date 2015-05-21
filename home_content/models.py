import datetime
from django.db import models
from django.contrib.sites.models import Site
from django.db.models import Q
from filebrowser.fields import FileBrowseField


TEMPLATES = (
    ('billboard', 'Billboards'),
    ('mini_billboard_1', 'Mini Billboards Option 1'),
    ('mini_billboard_2', 'Mini Billboards Option 2'),
    ('1_col', '1 Column Free Form'),
    ('2_col', '2 Column Free Form'),
)


class HomeSection(models.Model):
    site = models.ForeignKey(Site, default=1, help_text='Choose which site you want this Section to appear on')

    label = models.CharField(max_length=200)

    template = models.CharField(max_length=50, choices=TEMPLATES, default='s')

    image_background = FileBrowseField(max_length=200, blank=True, null=True, help_text='Leave blank for white.', verbose_name='Background image')
    border = models.CharField(max_length=30, blank=True, null=True, help_text='Example: 1px solid #3EBFAC')

    is_published = models.BooleanField(default=True)
    order = models.IntegerField(default=1)

    def __unicode__(self):
        return self.label

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'
        ordering = ('site', 'order')

    @staticmethod
    def get_published_objects(current_site):
        sections = HomeSection.objects.filter(site=current_site, is_published=True).order_by('order')
        return sections

    def mini_billboards(self):
        mini_billboards = self.minibillboard_set.filter(is_published=True).order_by('order')
        return mini_billboards


class Billboard(models.Model):
    site = models.ForeignKey(Site, default=1, help_text='Choose which site you want this Billboard to appear on')

    label = models.CharField(max_length=200)

    image = FileBrowseField(max_length=200, help_text='Approximately 1000px wide (Keep subject towards the middle of image for best viewing on mobile.)')
    content = models.TextField(max_length=500)
    link = models.CharField(max_length=200, blank=True, null=True)

    is_published = models.BooleanField(default=True)
    publish_date = models.DateField(db_index=True)
    expire_date = models.DateField(null=True, blank=True)

    order = models.IntegerField(default=1)

    def __unicode__(self):
        return self.label

    class Meta:
        verbose_name = 'Billboard'
        verbose_name_plural = 'Billboards'
        ordering = ('site', 'order', '-publish_date')

    @staticmethod
    def get_published_objects(current_site):
        billboards = Billboard.objects.filter(Q(site=current_site) & Q(publish_date__lte=datetime.datetime.now) & Q(is_published=True) &
                                              (Q(expire_date=None) | Q(expire_date__gte=datetime.datetime.now))).order_by('order', '-publish_date')
        return billboards


class MiniBillboard(models.Model):
    section = models.ForeignKey(HomeSection)

    image = FileBrowseField(max_length=200, blank=True, null=True)
    headline = models.CharField(max_length=75)
    description = models.CharField(max_length=100)
    link = models.CharField(max_length=200, blank=True, null=True)

    is_published = models.BooleanField(default=True)
    order = models.IntegerField(default=1)

    def __unicode__(self):
        return self.headline

    class Meta:
        verbose_name = 'Mini Billboard'
        verbose_name_plural = 'Mini Billboards'
        ordering = ('section', 'order', 'headline')

    @staticmethod
    def get_published_objects():
        mini_billboards = MiniBillboard.objects.filter(is_published=True).order_by('order')
        return mini_billboards
