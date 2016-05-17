from django.db import models
from django.contrib.auth.models import User

from django_resized import ResizedImageField

from customer.models import Customer
from parts.models import (
    Part,
    LabourCost
)
from mechanic.models import Mechanic
from vehical.models import (
    Vehical,
    OtherService
)


class Payment(models.Model):

    """
    payment model for service
    """
    payment_amount = models.FloatField(default=0)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    recieved_by = models.ForeignKey(User)

    def __unicode__(self):
        return str(self.payment_amount)


class Service(models.Model):

    """
    Service model to store all service related information
    """

    customer = models.ForeignKey(Customer)
    serviced_by = models.ForeignKey(Mechanic, blank=True, null=True)
    created_by = models.ForeignKey(User)
    vehical = models.ForeignKey(Vehical, blank=True, null=True)
    otherservice = models.ForeignKey(OtherService, blank=True, null=True)
    parts = models.ManyToManyField(Part)
    labourcost_detail = models.ManyToManyField(LabourCost)
    payment = models.ManyToManyField(Payment)
    remark = models.TextField(blank=True, null=True)
    service_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    expected_delivery_date = models.DateField(blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True)
    total_paid = models.FloatField(default=0)
    total_pending = models.FloatField(default=0)
    next_service_date = models.DateField(blank=True, null=True)
    invoice_number = models.AutoField(primary_key=True)
    recipient_name = models.CharField(blank=True, max_length=50)
    recipient_nuber = models.CharField(blank=True, max_length=50)
    labour_cost = models.FloatField(default=0)
    part_cost = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    tax_amount = models.FloatField(default=0)
    service_tax = models.FloatField(default=0)
    service_tax_amount = models.FloatField(default=0)
    advance_payment = models.FloatField(default=0)
    total_cost = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)
    is_archive = models.BooleanField(default=False)
    is_serviced = models.BooleanField(default=False)
    complete_payment = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.invoice_number)
