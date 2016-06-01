from django.db import models
from django.contrib.auth.models import User


class QuotationPart(models.Model):
    created_by = models.ForeignKey(User)
    part_name = models.CharField(blank=True, max_length=50)
    description = models.CharField(blank=True, null=True, max_length=250)
    part_company_name = models.CharField(blank=True, max_length=50)
    price = models.FloatField(default=0)
    part_quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u''.join((self.part_name))


class Performa(models.Model):
    created_by = models.ForeignKey(User, blank=True, null=True)
    purchase_order_number = models.CharField(blank=True, max_length=50)
    parts = models.ManyToManyField(QuotationPart)
    total_cost = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    tax_amount = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)
    estimated_delivery = models.CharField(blank=True, null=True, max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u''.join((self.purchase_order_number))


class Quotation(models.Model):
    created_by = models.ForeignKey(User)
    customer_name = models.CharField(max_length=250)
    company_name = models.CharField(blank=True, max_length=50)
    phone_number = models.CharField(blank=True, null=True, max_length=50)
    total_cost = models.FloatField(blank=True)
    email = models.EmailField(blank=True, null=True)
    parts = models.ManyToManyField(QuotationPart)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    tax_amount = models.FloatField(default=0)
    payment_details = models.CharField(blank=True, null=True, max_length=150)
    address = models.CharField(blank=True, null=True, max_length=250)
    estimated_delivery = models.CharField(blank=True, null=True, max_length=150)
    tax = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)
    performa = models.ForeignKey(Performa, blank=True, null=True)

    def __unicode__(self):
        return u''.join((self.customer_name))
