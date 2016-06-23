from django.conf.urls import patterns, url

from customer.views import *


urlpatterns = patterns(
    '',
    url(r'^add/$', 'customer.views.add_customer',
        name='add_customer'),
    url(r'^create/$', 'customer.views.customer_create',
        name='customer_create'),
    url(r'^view/$', 'customer.views.customer_view',
        name='customer_view'),
    url(r'^edit/(?P<id>[0-9]+)/$', 'customer.views.customer_edit',
        name='customer_edit'),
    url(r'^delete/(?P<id>[0-9]+)/$', 'customer.views.customer_delete',
        name='customer_delete'),
    url(r'^detail/(?P<id>[0-9]+)/$', 'customer.views.customer_detail',
        name='customer_detail'),
)
