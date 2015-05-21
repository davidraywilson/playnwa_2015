import logging
from django.contrib.sites.models import Site
from django.contrib import admin
from page_content.models import *


class PageSectionInline(admin.TabularInline):
    model = PageSection
    sortable_field_name = "display_order"
    extra = 1


class WebPageAdmin(admin.ModelAdmin):
    model = WebPage
    list_display = ('label', 'is_published', 'create_date')
    list_filter = ('modified_date', 'is_published')
    list_editable = ('is_published',)

    prepopulated_fields = {'slug': ('label',), }
    search_fields = ('label',)
    save_as = True

    inlines = [
        PageSectionInline,
    ]

    fieldsets = (

        (None, {
            'classes': ('suit-tab suit-tab-general full-width',),
            'fields': ('template_choice', 'label', 'image_cover', 'is_published')
        }),

        (None, {
            'classes': ('suit-tab suit-tab-seo',),
            'fields': ('meta_title', 'meta_description', 'meta_tags', 'slug')
        }),

    )

    suit_form_includes = (
        ('admin/suit_includes/edit_page_content.html', 'bottom', 'general'),
    )

    suit_form_tabs = (('general', 'General'), ('seo', 'SEO'))

    def queryset(self, request):
        # ONLY SHOW OBJECTS FOR CURRENT SITE
		qs = super(WebPageAdmin, self).queryset(request)

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


admin.site.register(WebPage, WebPageAdmin)
