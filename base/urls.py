from django.conf.urls.defaults import *
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login'),
    (r'^admin/', include(admin.site.urls)),
    (r'^frontendadmin/', include('frontendadmin.urls')),
    (r'^', include(settings.SITE_NAME+'.main.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
	    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT})
    ) + urlpatterns
