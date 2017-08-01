from enum import Enum

from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

from django_resized import ResizedImageField

from customer.models import Customer


class Mechanic(models.Model):

    """
    Customer model to store all customer related information
    """

    class Gender(Enum):

        """
        This class creates enum for gender field of UserProfile.
        """

        MALE = 'Male'
        FEMALE = 'Female'

        @classmethod
        def as_tuple(cls):
            return ((item.value, item.name.replace('_', ' ')) for item in cls)

    created_by = models.ForeignKey(User)
    first_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    email = models.EmailField()
    about = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(blank=True, max_length=20, null=True)
    phone_number = models.BigIntegerField()
    advance_taken = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    profile_picture = models.ImageField(
        upload_to='profile_picture/',
        blank=True,
        null=True
    )
    profile_picture_icon = ResizedImageField(
        size=[20, 20],
        quality=100,
        crop=['middle', 'center'],
        upload_to='profile_picture/',
        blank=True,
        null=True
    )
    profile_picture_thumbnail = ResizedImageField(
        size=[300, 200],
        quality=100,
        upload_to='profile_picture/',
        blank=True,
        null=True
    )
    profile_picture_macroicon = ResizedImageField(
        size=[50, 50],
        quality=100,
        crop=['middle', 'center'],
        upload_to='profile_picture/',
        blank=True,
        null=True
    )

    def __unicode__(self):
        return u' '.join((self.first_name, self.last_name))
