from django.contrib import admin

from models import *
from mptt.admin import MPTTModelAdmin


class PrimaryNavigationAdmin(MPTTModelAdmin):
    list_display = ('title', 'is_published', 'order', 'url_search_target')
    list_editable = ('is_published', 'order')

    search_fields = ('title',)
    save_as = True

    fieldsets = (
        (None, {
            'classes': ('full-width',),
            'fields': (
                'parent', 'title', 'link_type', 'page', 'link', 'is_published', 'order'
            )
        }),
    )

    class Media:
        js = [
            '/static/navigation/admin/navigation.js',
        ]


class UrlRedirect_Admin(admin.ModelAdmin):
    model = UrlRedirect
    list_display = ('from_url', 'to_url')


admin.site.register(PrimaryNavigation, PrimaryNavigationAdmin)
admin.site.register(UrlRedirect, UrlRedirect_Admin)
