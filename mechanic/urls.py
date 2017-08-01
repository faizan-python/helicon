from django.conf.urls import patterns, url

from mechanic.views import *


urlpatterns = patterns(
    '',
    url(r'^add/$', 'mechanic.views.add_mechanic',
        name='add_mechanic'),
    url(r'^update/$', 'mechanic.views.add_mechanic_view',
        name='add_mechanic_view'),
    url(r'^view/$', 'mechanic.views.mechanic_view',
        name='mechanic_view'),
    url(r'^delete/$', 'mechanic.views.mechanic_delete',
        name='mechanic_delete'),
    url(r'^edit/(?P<id>[0-9]+)/$', 'mechanic.views.mechanic_edit',
        name='mechanic_edit'),
)
