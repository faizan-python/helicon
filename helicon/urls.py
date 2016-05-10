"""helicon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^superadmin/', include(admin.site.urls)),
    url(r'^$', 'web.views.home', name='web_home'),
    url(r'^about/', 'web.views.about', name='web_about'),
    url(r'^contact/', 'web.views.contact', name='web_contactus'),
    url(r'^save/contact/', 'web.views.save_contact', name='web_save_contactus'),
    url(r'^product/', 'web.views.product', name='web_product'),

    url(r'^admin/', 'core.views.index', name='core_index'),
    url(r'^verify/', 'core.views.verify', name='core_verify'),
    url(r'^home/', 'core.views.home', name='core_home'),
    url(r'^userprofile/', include('userdetails.urls',
                                  namespace='userprofile')),
    url(r'^customer/', include('customer.urls', namespace='customer')),
    url(r'^part/', include('parts.urls', namespace='part')),
    url(r'^vehical/', include('vehical.urls', namespace='vehical')),
    url(r'^service/', include('service.urls', namespace='service')),
    url(r'^mechanic/', include('mechanic.urls', namespace='mechanic')),
    url(r'^quotation/', include('quotation.urls', namespace='quotation')),
    url(r'^login/$', 'userdetails.views.login',
        name='login'),
    url(r'^logout/$',
        'django.contrib.auth.views.logout', {'next_page': '/admin/'},
        name='logout'),

    # Html URL's
    url(r'^product_warm-shaft/', 'web.views.product_warm_shaft', name='web_product_warm_shaft'),
    url(r'^product_crown-pinion/', 'web.views.product_crown_pinion', name='web_product_crown_pinion'),
    url(r'^product_warm_wheel/', 'web.views.product_warm_wheel', name='web_product_warm_wheel'),
    url(r'^product_pinion_shaft/', 'web.views.product_pinion_shaft', name='web_product_pinion_shaft'),
    url(r'^product_spiral_bevel_gear/', 'web.views.product_spiral_bevel_gear',name='web_product_spiral_bevel_gear'),
    url(r'^product_gear_shafts/', 'web.views.product_gear_shafts',name='web_product_gear_shafts'),
    url(r'^product_worm_wheel_shaft/', 'web.views.product_worm_wheel_shaft',name='web_product_worm_wheel_shaft'),
    url(r'^product_worm_shaft_elevators/', 'web.views.product_worm_shaft_elevators',name='web_product_worm_shaft_elevators'),
    url(r'^product_worm_forging_gear_shaft/', 'web.views.product_forging_gear_shaft',name='web_product_forging_gear_shaft'),
    url(r'^product_worm_crown_pinion_steel/', 'web.views.product_crown_pinion_steel',name='web_product_crown_pinion_steel'),
    url(r'^product_balancing_gear/', 'web.views.product_balancing_gear',name='web_product_balancing_gear'),
    url(r'^product_spur_gear/', 'web.views.product_spur_gear',name='web_product_spur_gear'),
    url(r'^product_loose_gears/', 'web.views.product_loose_gears',name='web_product_loose_gears'),
]
