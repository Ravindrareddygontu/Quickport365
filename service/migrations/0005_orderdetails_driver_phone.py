# Generated by Django 4.0.2 on 2022-12-10 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_remove_orderdetails_aadhar_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='driver_phone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
