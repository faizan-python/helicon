from django.db import models
from django.contrib.auth.models import User


class Part(models.Model):
    created_by = models.ForeignKey(User)
    part_name = models.CharField(blank=True, max_length=50)
    part_company_name = models.CharField(blank=True, max_length=50)
    price = models.FloatField(blank=True)
    part_quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u''.join((self.part_name))


class LabourCost(models.Model):
    created_by = models.ForeignKey(User)
    name = models.CharField(blank=True, max_length=50)
    labour_price = models.FloatField(blank=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u''.join((self.name))
