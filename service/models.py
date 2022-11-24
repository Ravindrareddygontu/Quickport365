from django.db import models
from django.contrib.auth.models import User


class Domestic(models.Model):
        origin =models.IntegerField()
        destination = models.IntegerField()


class International(models.Model):
    Destination_country = models.CharField(max_length=100)
    origin = models.IntegerField()
    destination = models.IntegerField()


sh = (("self", 'Self'), ("other", 'Other'))


class ParcelDetails(models.Model):
    item_weight = models.CharField(max_length=1)
    item_name = models.CharField(max_length=200)
    pickup_date = models.DateField(null=True)
    delivery_hand = models.CharField(max_length=200, choices=sh)
    parcel_image = models.ImageField(upload_to='images')


class OrderDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False)
    origin = models.IntegerField()
    destination = models.IntegerField()
    Destination_country = models.CharField(max_length=100)
    item_weight = models.IntegerField()
    item_name = models.CharField(max_length=200)
    services = models.CharField(max_length=200)
    date = models.DateField(null=True)
    from_whom = models.CharField(max_length=200, null=True)
    image = models.ImageField()
    price = models.IntegerField(null=True)


class Drivers(models.Model):
    name = models.CharField(max_length=50)
    vehicle_name = models.CharField(max_length=30)
    vehicle_no = models.CharField(max_length=10)
    area = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=10)
    email = models.EmailField()