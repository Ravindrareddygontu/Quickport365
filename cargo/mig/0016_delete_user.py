# Generated by Django 4.0.2 on 2022-11-27 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0015_rename_user_orderdetails_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
