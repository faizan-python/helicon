from django.db import models
from django.contrib.auth.models import User

from customer.models import Customer


class Vehical(models.Model):

    """
    Customer model to store all customer related information
    """

    customer = models.ForeignKey(Customer)
    created_by = models.ForeignKey(User)
    vehical_number = models.CharField(unique=True, max_length=50)
    vehical_name = models.CharField(blank=True, max_length=50)
    vehical_colour = models.CharField(blank=True, max_length=50)
    about = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    last_serviced_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return u''.join((self.vehical_number))


class OtherService(models.Model):

    """
    Customer model to store all customer related information
    """

    customer = models.ForeignKey(Customer)
    created_by = models.ForeignKey(User)
    number = models.CharField(unique=True, max_length=50)
    name = models.CharField(blank=True, max_length=50)
    company_name = models.CharField(blank=True, max_length=50)
    about = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return u''.join((self.name))
