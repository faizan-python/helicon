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
    url(r'^quotation/view/(?P<id>[0-9]+)/$', 'quotation.views.quotation_pdf',
        name='quotation_pdf'),
)
