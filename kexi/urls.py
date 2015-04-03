from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kexi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^vv/', include('vv.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
