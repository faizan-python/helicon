from enum import Enum
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

    class PaymentOptions(Enum):
        CASH = 'Cash'
        CHEQUE = 'Cheque'
        OTHERS = 'Others'
        Advance = 'Advance'

        @classmethod
        def as_tuple(cls):
            return ((item.value, item.name.replace('_', ' ')) for item in cls)

    payment_type = models.CharField(blank=True, null=True, max_length=20,
                                    choices=PaymentOptions.as_tuple())
    cheque_number = models.CharField(blank=True, null=True, max_length=70)
    cheque_bank_name = models.CharField(blank=True, null=True, max_length=250)
    cheque_date = models.DateTimeField(blank=True, null=True)
    payment_amount = models.FloatField(default=0)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    recieved_by = models.ForeignKey(User)

    def __unicode__(self):
        return str(self.payment_amount)


class DeliveryDetail(models.Model):
    vehical_number = models.CharField(blank=True, null=True, max_length=70)
    remark = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.vehical_number)


class InvoiceDetail(models.Model):
    latest_retail_invoice = models.CharField(blank=True, null=True, max_length=100)
    latest_tax_invoice    = models.CharField(blank=True, null=True, max_length=100)

    def __unicode__(self):
        return str(self.latest_retail_invoice)


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
    gate_pass_no = models.CharField(blank=True, null=True, max_length=100)
    purchase_order_number = models.CharField(blank=True, null=True, max_length=100)
    purchase_order_date = models.DateTimeField(blank=True, null=True)

    freight_cost = models.FloatField(default=0)
    invoice_date = models.DateTimeField(blank=True, null=True)
    challan_number = models.CharField(blank=True, null=True, max_length=100)
    challan_date = models.DateTimeField(blank=True, null=True)
    delivery_invoice_details = models.ForeignKey(DeliveryDetail, blank=True, null=True)
    retail_invoice_number = models.IntegerField(blank=True, null=True)
    tax_invoice_number = models.IntegerField(blank=True, null=True)
    gst_type = models.CharField(blank=True, null=True, max_length=100)

    def __unicode__(self):
        return str(self.invoice_number)


class TaxCost(models.Model):

    """
    TaxCost model
    """
    igst = models.FloatField(default=0)
    sgst = models.FloatField(default=0)
    cgst = models.FloatField(default=0)

    def __unicode__(self):
        return str(self.igst)
