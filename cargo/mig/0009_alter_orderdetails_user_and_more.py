# Generated by Django 4.0.2 on 2022-11-24 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0008_orderdetails_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='parceldetails',
            name='item_weight',
            field=models.CharField(max_length=1),
        ),
    ]
