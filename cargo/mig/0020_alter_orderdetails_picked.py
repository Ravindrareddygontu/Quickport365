# Generated by Django 4.1 on 2022-11-29 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0019_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='picked',
            field=models.CharField(choices=[('picked', 'picked'), ('completed', 'completed')], max_length=20),
        ),
    ]
