# Generated by Django 4.0.6 on 2022-12-12 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_alter_orderdetails_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='created',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='drivers',
            name='created',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='drivers',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='drivers_orders',
            name='created',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='drivers_orders',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='created',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='parceldetails',
            name='created',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='parceldetails',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
