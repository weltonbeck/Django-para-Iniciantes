from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^aula3/$', 'aula3.views.index', name='aula3_index'),
    url(r'^aula3/(?P<id>\d+)/$', 'aula3.views.detail', name='aula3_detail'),
    # url(r'^aula3/(?P<username>[\w-]+)/$', 'aula3.views.detail', name='aula3_detail'),

    url(r'^aula4/$', 'aula4.views.index', name='aula4_index'),
    url(r'^aula5/$', 'aula5.views.index', name='aula5_index'),

    url(r'^aula6/$', 'aula6.views.index', name='aula6_index'),
    url(r'^aula6/(?P<id>\d+)/$', 'aula6.views.detail', name='aula6_detail'),

    url(r'^aula7/$', 'aula7.views.index', name='aula7_index'),
    url(r'^aula7/sair/$', 'aula7.views.sair', name='aula7_sair'),
    url(r'^aula7/view_protegida/$', 'aula7.views.view_protegida', name='aula7_view_protegida'),
    url(r'^aula7/view_protegida2/$', 'aula7.views.view_protegida2', name='aula7_view_protegida2'),

    url(r'^aula9/$', 'aula9.views.index', name='aula9_index'),

    url(r'^aula10/$', 'aula10.views.index', name='aula10_index'),

    url(r'^aula11/$', 'aula11.views.index', name='aula11_index'),

    url(r'^aula12/$', 'aula12.views.index', name='aula12_index'),

    url(r'^aula13/$', 'aula13.views.index', name='aula13_index'),

    # Examples:
    # url(r'^$', 'cursodjango.views.home', name='home'),
    # url(r'^cursodjango/', include('cursodjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

# crio o roteamento dos arquivos estaticos dentro de /media
if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	)

urlpatterns += staticfiles_urlpatterns()