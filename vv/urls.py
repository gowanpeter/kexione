
from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',


    url(r'^piece/(?P<piece_id>\w{0,50})/$', 'vv.views.PieceView', name='piece'),
    url(r'^glaze$', 'vv.views.GlazeView', name='glaze'),
    url(r'^documentation$', 'vv.views.DocumentationView', name='documentation',),
    url(r'^condition$', 'vv.views.ConditionView', name='condition',),
    url(r'^exhibition$', 'vv.views.ExhibitionLookupView', name='exhibition',),
    url(r'^hline$', 'vv.views.HeathLineLookupView', name='hline',),
    url(r'^logo$', 'vv.views.LogoView', name='logo',),
    url(r'^maker$', 'vv.views.MakerLookupView', name='maker',),
    url(r'^material$', 'vv.views.MaterialLookupView', name='material',),
    url(r'^method$', 'vv.views.MethodLookupView', name='method',),
    url(r'^pub$', 'vv.views.PublicationView', name='pub',),
    url(r'^setc$', 'vv.views.SetCollectionView', name='set',),
)




    #src/kk
 #   url(r'^vv/', include('vv.urls', namespace='vv', app_name='kk')),
 #   url(r'^$',vv.views.kk_directory, name='kk')


#if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL,
                          #document_root=settings.STATIC_ROOT)
    #urlpatterns += static(settings.MEDIA_URL,
                          #document_root=settings.MEDIA_ROOT)
