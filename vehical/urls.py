from django.conf.urls import patterns, url

from vehical.views import *


urlpatterns = patterns(
    '',
    url(r'^user/get/$', 'vehical.views.get_user_vehical',
        name='get_user_vehical'),
)
