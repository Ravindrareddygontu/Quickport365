# Generated by Django 4.0.6 on 2022-12-12 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_orderdetails_driver_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetails',
            name='from_whom',
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='delivery_address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='pickup_address',
            field=models.CharField(max_length=500, null=True),
        ),
    ]