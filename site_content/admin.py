from django.contrib import admin
from django.contrib.sites.models import Site
from site_content.models import *


class LogoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('full-width',),
            'fields': ('site', 'image_desktop', 'image_mobile')
        }),

    )

    def queryset(self, request):
        # ONLY SHOW OBJECTS FOR CURRENT SITE
		qs = super(LogoAdmin, self).queryset(request)

		try:
		    # GET CURRENT SITE
		    current_site = Site.objects.get_current()

		except Exception, e:
		    logging.error(e)
		    current_site = None

		if current_site:
			return qs.filter(site=current_site)

		else:
			return qs


class ColorAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('full-width',),
            'fields': ('site', 'color')
        }),

    )

    def queryset(self, request):
        # ONLY SHOW OBJECTS FOR CURRENT SITE
		qs = super(ColorAdmin, self).queryset(request)

		try:
		    # GET CURRENT SITE
		    current_site = Site.objects.get_current()

		except Exception, e:
		    logging.error(e)
		    current_site = None

		if current_site:
			return qs.filter(site=current_site)

		else:
			return qs


class SocialAdmin(admin.ModelAdmin):
    list_display = ('label', 'order', 'is_published')
    list_filter = ('is_published',)
    list_editable= ('order', 'is_published')

    fieldsets = (
        (None, {
            'classes': ('full-width',),
            'fields': ('site', 'label', 'image_light', 'image_dark', 'link', 'order', 'is_published')
        }),

    )

    def queryset(self, request):
        # ONLY SHOW OBJECTS FOR CURRENT SITE
		qs = super(SocialAdmin, self).queryset(request)

		try:
		    # GET CURRENT SITE
		    current_site = Site.objects.get_current()

		except Exception, e:
		    logging.error(e)
		    current_site = None

		if current_site:
			return qs.filter(site=current_site)

		else:
			return qs


class InstagramAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('full-width',),
            'fields': ('site', 'label', 'link', 'instagram_id')
        }),

    )

    def queryset(self, request):
        # ONLY SHOW OBJECTS FOR CURRENT SITE
		qs = super(InstagramAdmin, self).queryset(request)

		try:
		    # GET CURRENT SITE
		    current_site = Site.objects.get_current()

		except Exception, e:
		    logging.error(e)
		    current_site = None

		if current_site:
			return qs.filter(site=current_site)

		else:
			return qs


admin.site.register(Logo, LogoAdmin)
admin.site.register(SiteColor, ColorAdmin)
admin.site.register(SocialLink, SocialAdmin)
admin.site.register(Instagram, InstagramAdmin)
