from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    'webapp.views',
    url(r'^$', 'view_home'),
)

urlpatterns += patterns(
    '',
    url(r'^front-edit/', include('front.urls')),
)

urlpatterns += patterns(
    '',
    url(r'^admin/filebrowser/', include('filebrowser.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEVELOPMENT:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

# EDIT FOR DYNAMIC PAGE
urlpatterns += patterns(
    'page_content.views',
    url(r'^edit/(?P<a_slug>.*)$', 'view_web_page'),
)

# NAVIGATION & PAGES
urlpatterns += patterns(
    'navigation.views',
    url(r'^.+/', 'default'),  # '^.+/' PRESERVES DJANGO'S APPEND_SLASH FEATURE
)
