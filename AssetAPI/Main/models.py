from django.core.exceptions import ValidationError
from django.db import models

from AssetAPI import GLOBALS
from AssetAPI.GLOBALS import BaseModel

import uuid


class Customer(BaseModel):
    company_name = models.CharField(max_length=255, default='', blank=True)

class Human(BaseModel):
    first_name = models.CharField(max_length=255, default='', blank=True)
    middle_name = models.CharField(max_length=255, default='', blank=True)
    last_name = models.CharField(max_length=255, default='', blank=True)
    email = models.EmailField(max_length=255, default='', blank=True)

    class Meta:
        abstract = True

class Qualification(BaseModel):
    name = models.CharField(max_length=255, default='', blank=True)
    level = models.CharField(max_length=255, choices=GLOBALS.QUALIFICATION_LEVEL_CHOICES, default=GLOBALS.UNDEFINED_LEVEL)

class Personnel(Human):
    owner = models.ForeignKey(Customer, on_delete=models.PROTECT)
    identity = models.CharField(max_length=255, default='', blank=True)
    role = models.CharField(max_length=255, choices=GLOBALS.PERSONNEL_ROLE_CHOICES, default=GLOBALS.UNDEFINED_ROLE)
    qualifications = models.ManyToManyField(Qualification)





class Asset(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    uuid = models.CharField(max_length=255, default=uuid.uuid4)

    class Meta:
        abstract = True

class GenericAsset(Asset):
    name = models.CharField(max_length=255, default='', blank=True)

class VehicleAsset(Asset):
    brand = models.CharField(max_length=255, default='', blank=True)
    model = models.CharField(max_length=255, default='', blank=True)
    odometer = models.BigIntegerField(default=0, blank=True)
    color = models.CharField(max_length=12, default='', blank=True)
    registration_number = models.CharField(max_length=35, default='', blank=True)

class AssetFleetRental(BaseModel):
    vehicles = models.ManyToManyField(VehicleAsset)
    assets = models.ManyToManyField(GenericAsset)

    date_of_rental = models.DateField(auto_now_add=True, editable=True)

class AssetCrossAssignment(BaseModel):
    owning_customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="owner_customer")
    assigned_customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="assigned_to_customer")

    fleet_rental_where_crossed = models.ManyToManyField(AssetFleetRental)
    vehicles_crossed = models.ManyToManyField(VehicleAsset)
    assets_crossed = models.ManyToManyField(GenericAsset)



class Trip(BaseModel):

    vehicle = models.ForeignKey(VehicleAsset, on_delete=models.PROTECT)

    fleet = models.ForeignKey(VehicleAsset, on_delete=models.PROTECT)

    origin_lat_long = models.CharField(max_length=255, default='', blank=True)
    origin_address = models.CharField(max_length=255, default='', blank=True)
    origin_odometer = models.BigIntegerField(default=0, blank=True)

    destination_lat_long = models.CharField(max_length=255, default='', blank=True)
    destination_address = models.CharField(max_length=255, default='', blank=True)
    destination_odometer = models.BigIntegerField(default=0, blank=True)

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    operated_by = models.ForeignKey(Personnel, on_delete=models.PROTECT)

    initiated_at_datetime = models.DateTimeField(auto_now_add=True, editable=True)
    concluded_at_datetime = models.DateTimeField(auto_now_add=True, editable=True)

    def save(self, *args, **kwargs):
        # REQUIREMENT: trip must begin and end on the same day
        if self.initiated_at_datetime.date() != self.concluded_at_datetime.date():
            raise ValidationError(f"This trip did not take place over one day."
                                  f"initiated at: {self.initiated_at_datetime}"
                                  f"concluded at: {self.concluded_at_datetime}")
        super(Trip, self).save(*args, **kwargs)

    @property
    def distance(self):
        return self.destination_odometer - self.origin_odometer


