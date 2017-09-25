from django.contrib import admin

from service.models import Service, InvoiceDetail

admin.site.register(Service)
admin.site.register(InvoiceDetail)
