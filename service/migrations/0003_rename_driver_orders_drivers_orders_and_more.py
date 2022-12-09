# Generated by Django 4.1 on 2022-12-09 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0002_drivers_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Driver_orders',
            new_name='Drivers_orders',
        ),
        migrations.AlterField(
            model_name='drivers_orders',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
