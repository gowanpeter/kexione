from django.conf import settings
from django.conf.urls import include, patterns, url
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(’’,
    url(r’^__debug__/’, include(debug_toolbar.urls)),
    )