from django.conf.urls import patterns, url

from quotation.views import *


urlpatterns = patterns(
    '',
    url(r'^create/$', 'quotation.views.quotation',
        name='quotation'),
    url(r'^generate/$', 'quotation.views.quotation_generate',
        name='quotation_generate'),
    url(r'^list/$', 'quotation.views.quotation_list',
        name='quotation_list'),
    url(r'^view/(?P<id>[0-9]+)/$', 'quotation.views.quotation_pdf',
        name='quotation_pdf'),
    url(r'^delete/(?P<id>[0-9]+)/$', 'quotation.views.quotation_delete',
        name='quotation_delete'),
    url(r'^performa/view/(?P<id>[0-9]+)/$', 'quotation.views.performa_pdf',
        name='performa_pdf'),
    url(r'^performa/(?P<id>[0-9]+)/$', 'quotation.views.performa',
        name='performa'),
    url(r'^performa/generate/$', 'quotation.views.performa_generate',
        name='performa_generate'),
)
