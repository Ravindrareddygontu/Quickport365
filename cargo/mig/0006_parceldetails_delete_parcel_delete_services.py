# Generated by Django 4.0.2 on 2022-11-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_alter_drivers_vehicle_name_alter_drivers_vehicle_no_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParcelDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_weight', models.IntegerField()),
                ('item_name', models.CharField(max_length=200)),
                ('pickup_date', models.DateField(null=True)),
                ('delivery_hand', models.CharField(choices=[('self', 'Self'), ('other', 'Other')], max_length=200)),
                ('parcel_image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.DeleteModel(
            name='Parcel',
        ),
        migrations.DeleteModel(
            name='Services',
        ),
    ]