from django.conf.urls.defaults import patterns
import settings

urlpatterns = patterns(settings.SITE_NAME+'.main.views',
    (r'$', 'index')
)