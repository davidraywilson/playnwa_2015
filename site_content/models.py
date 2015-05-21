from django.contrib.sites.models import Site
from django.db import models
from filebrowser.fields import FileBrowseField


class Logo(models.Model):
    site = models.OneToOneField(Site, default=1, help_text='Choose which site you want this link to appear on')
    image_desktop = FileBrowseField(max_length=400, blank=True, null=True, verbose_name='Desktop image', help_text='Transparent .png')
    image_mobile = FileBrowseField(max_length=400, blank=True, null=True, verbose_name='Mobile image', help_text='Transparent .png')

    def __unicode__(self):
        return 'Logo for %s' % self.site.name

    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logos'


class SiteColor(models.Model):
    site = models.OneToOneField(Site, default=1, help_text='Choose which site you want this link to appear on')
    color = models.CharField(max_length=7, help_text='Hex code starting with #. Ex: #219CDC')

    def __unicode__(self):
        return 'Color for %s' % self.site.name

    class Meta:
        verbose_name = 'Site Color'
        verbose_name_plural = 'Site Colors'


class SocialLink(models.Model):
    site = models.ForeignKey(Site, default=1, help_text='Choose which site you want this link to appear on')
    label = models.CharField(max_length=200)

    image_light = FileBrowseField(max_length=400, verbose_name='Light image')
    image_dark = FileBrowseField(max_length=400, verbose_name='Dark image')
    link = models.URLField()

    order = models.IntegerField(default=1)
    is_published = models.BooleanField(default=True)

    def __unicode__(self):
        return self.label

    class Meta:
        verbose_name = 'Social Link'
        verbose_name_plural = 'Social Links'
        ordering = ('site', 'order', 'label')

    @staticmethod
    def get_published_objects_for_site(current_site):
        return SocialLink.objects.filter(is_published=True, site=current_site)


class Instagram(models.Model):
    site = models.OneToOneField(Site, default=1, help_text='Choose which site you want this link to appear on')
    label = models.CharField(max_length=100, help_text='This is only used in the admin')
    link = models.URLField(help_text='Link to your profile')
    instagram_id = models.CharField(max_length=100, help_text='You can get your ID here ->  http://jelled.com/instagram/lookup-user-id')

    def __unicode__(self):
        return '%s - %s' % (self.label, self.site.name)

    class Meta:
        verbose_name = 'Instagram'
        verbose_name_plural = 'Instagram'
