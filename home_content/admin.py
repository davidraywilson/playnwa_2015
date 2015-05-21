import logging
from django.contrib.sites.models import Site
from django.contrib import admin
from home_content.models import HomeSection, Billboard, MiniBillboard


class MiniBillboardInline(admin.TabularInline):
    model = MiniBillboard
    sortable_field_name = 'order'
    extra = 1


class SectionAdmin(admin.ModelAdmin):
    model = HomeSection
    list_display = ('label', 'order', 'is_published')
    list_filter = ('is_published',)
    list_editable = ('order', 'is_published')

    fieldsets = (
        (None, {
            'classes': ('full-width',),
            'fields': ('site', 'template', 'label', 'image_background', 'border', 'order', 'is_published')
        }),

    )

    inlines = [
        MiniBillboardInline,
    ]

    class Media:
        js = [
            '/static/admin_js/custom/home_section.js',
        ]

    def queryset(self, request):
        # ONLY SHOW OBJECTS FOR CURRENT SITE
		qs = super(SectionAdmin, self).queryset(request)

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


class BillboardAdmin(admin.ModelAdmin):
    model = Billboard
    list_display = ('label', 'order', 'publish_date', 'is_published')
    list_filter = ('is_published',)
    list_editable = ('order', 'is_published',)

    fieldsets = (

        (None, {
            'classes': ('full-width',),
            'fields': ('site', 'label', 'order', 'image', 'content', 'link', 'publish_date', 'expire_date', 'is_published')
        }),

    )

    class Media:
        js = [
            '/static/admin_js/tinymce/tinymce.min.js',
            '/static/admin_js/tinymce_init.js'
        ]

    def queryset(self, request):
        # ONLY SHOW OBJECTS FOR CURRENT SITE
		qs = super(BillboardAdmin, self).queryset(request)

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


class MiniBillboardAdmin(admin.ModelAdmin):
    model = MiniBillboard
    list_display = ('headline', 'section', 'order', 'is_published')
    list_filter = ('is_published',)
    list_editable = ('order', 'is_published',)

    save_as = True

    fieldsets = (

        (None, {
            'classes': ('full-width',),
            'fields': ('section', 'image', 'headline', 'description', 'link', 'order', 'is_published')
        }),

    )

    def queryset(self, request):
        # ONLY SHOW OBJECTS FOR CURRENT SITE
		qs = super(MiniBillboardAdmin, self).queryset(request)

		try:
		    # GET CURRENT SITE
		    current_site = Site.objects.get_current()

		except Exception, e:
		    logging.error(e)
		    current_site = None

		if current_site:
			return qs.filter(section__site=current_site)

		else:
			return qs


admin.site.register(HomeSection, SectionAdmin)
admin.site.register(Billboard, BillboardAdmin)
admin.site.register(MiniBillboard, MiniBillboardAdmin)
