from django.conf.urls import patterns, include, url
from django.contrib import admin
from vv.views import current_datetime

urlpatterns = patterns('',
    # Examples:
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^time/$', current_datetime),
    url(r'^$', 'vv.views.home_page', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^vv/', include('vv.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
