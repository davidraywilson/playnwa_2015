from django.db import models
from django.utils.text import slugify

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from page_content.models import WebPage


LINK_TYPES = (
    ('page', 'Page'),
    ('custom', 'Link')
)


class PrimaryNavigation(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    title = models.CharField(max_length=100)

    link_type = models.CharField(max_length=50, blank=True, null=True, choices=LINK_TYPES)

    page = models.ForeignKey(WebPage, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)

    is_published = models.BooleanField(default=True)
    order = models.IntegerField(default=1)

    url_search_target = models.CharField(max_length=400, blank=True)

    def url(self):
        if self.link_type == 'custom':
            return "%s" % self.link

        my_url = "/%s" % slugify(self.title)
        if self.parent is None:
            return my_url
        else:
            root_url = self.parent.url()
            return "%s%s" % (root_url, my_url)

    def get_absolute_url(self):
        return self.url()

    def save(self, *args, **kwargs):

        if self.url_search_target != self.url():
            self.url_search_target = self.url()
            update_children_urls = True
        else:
            update_children_urls = False

        super(PrimaryNavigation, self).save(*args, **kwargs)

        if update_children_urls:
            for child in self.children.all():
                child.save()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Primary Navigation'
        verbose_name_plural = 'Primary Navigation'
        ordering = ('order', 'title')

    class MPTTMeta:
        order_insertion_by = ['order', 'title']

    @staticmethod
    def get_published_objects():
        return PrimaryNavigation.objects.filter(is_published=True, parent__isnull=True)

    def links(self):
        return self.children.filter(is_published=True)


class UrlRedirect(models.Model):
    from_url = models.CharField(max_length=200)
    to_url = models.CharField(max_length=200)


    class Meta:
        verbose_name = "Redirect"
        verbose_name_plural = "Redirects"
        ordering = ('from_url',)


    def __unicode__(self):
        return "%s" % (self.from_url)