# Generated by Django 4.1 on 2022-11-30 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0023_orderdetails_driver_alter_complaint_issue_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='picked',
            field=models.BooleanField(null=True),
        ),
    ]
