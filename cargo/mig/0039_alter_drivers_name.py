# Generated by Django 4.1 on 2022-12-09 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0038_rename_full_name_drivers_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivers',
            name='name',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]
