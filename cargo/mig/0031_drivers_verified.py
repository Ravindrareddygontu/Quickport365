# Generated by Django 4.1 on 2022-12-09 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0030_remove_drivers_aadhar_no_drivers_proof_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='drivers',
            name='verified',
            field=models.BooleanField(null=True),
        ),
    ]
