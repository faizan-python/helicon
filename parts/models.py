from django.db import models
from django.contrib.auth.models import User


class Part(models.Model):
    created_by = models.ForeignKey(User)
    part_name = models.CharField(blank=True, max_length=500)
    part_company_name = models.CharField(blank=True, max_length=500)
    part_code = models.CharField(blank=True, max_length=500)
    price = models.FloatField(blank=True)
    part_quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    @property
    def total_price(self):
        return self.price * self.part_quantity

    def __unicode__(self):
        return u''.join((self.part_name))


class LabourCost(models.Model):
    created_by = models.ForeignKey(User)
    name = models.CharField(blank=True, max_length=500)
    labour_price = models.FloatField(blank=True)
    labour_quantity = models.IntegerField(blank=True, default=0)
    is_active = models.BooleanField(default=True)

    @property
    def total_price(self):
        return self.labour_price * self.labour_quantity

    def __unicode__(self):
        return u''.join((self.name))
