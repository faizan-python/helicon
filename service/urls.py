from django.conf.urls import patterns, url

from service.views import *


urlpatterns = patterns(
    '',
    url(r'^demo/$', 'service.views.demo',
        name='demo'),


    url(r'^add/$', 'service.views.service_add',
        name='service_add'),
    url(r'^create/$', 'service.views.service_create',
        name='service_create'),
    url(r'^search/$', 'service.views.service_search',
        name='service_search'),
    url(r'^view/(?P<id>[0-9]+)/$', 'service.views.service_view',
        name='service_view'),
    url(r'^pending/$', 'service.views.service_pending',
        name='service_pending'),
    url(r'^edit/(?P<id>[0-9]+)/$', 'service.views.service_edit',
        name='service_edit'),
    url(r'^invoice/create/$', 'service.views.create_invoice',
        name='create_invoice'),
    url(r'^invoice/create/(?P<id>[0-9]+)/$', 'service.views.invoice_get',
        name='invoice_get'),
    url(r'^invoice/$', 'service.views.invoice',
        name='invoice'),    
    url(r'^pending/payment/$', 'service.views.pending_payment',
        name='pending_payment'),
    url(r'^invoice/view/(?P<id>[0-9]+)/$', 'service.views.invoice_view',
        name='invoice_view'),

    url(r'^invoice/tax/view/(?P<id>[0-9]+)/$', 'service.views.invoice_tax_view',
        name='invoice_tax_view'),
    url(r'^invoice/retail/view/(?P<id>[0-9]+)/$', 'service.views.invoice_retail_view',
        name='invoice_retail_view'),

    url(r'^report/$', 'service.views.report',
        name='report'),
    url(r'^customer/report/$', 'service.views.customer_report',
        name='customer_report'),
    url(r'^invoice/list/$', 'service.views.invoice_list',
        name='invoice_list'),
    url(r'^report/generate/$', 'service.views.report_generate',
        name='report_generate'),
    url(r'^customer/report/generate/(?P<id>[0-9]+)/$', 'service.views.customer_report_generate',
        name='customer_report_generate'),
)
