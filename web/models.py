from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=2000)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u''.join((self.name))


class Product(models.Model):
    name = models.CharField(max_length=2000)
    category = models.ForeignKey(Category)
    description = models.CharField(blank=True, null=True, max_length=2500)
    url = models.URLField(max_length=2000)
    is_active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='products')

    def __unicode__(self):
        return u''.join((self.name))
