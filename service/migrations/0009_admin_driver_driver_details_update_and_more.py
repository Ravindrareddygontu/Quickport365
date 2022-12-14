# Generated by Django 4.1 on 2022-12-12 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_complaint_created_complaint_updated_drivers_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('temp_password', models.CharField(max_length=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Driver_details_update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('temp_password', models.CharField(max_length=12)),
                ('new_password', models.EmailField(max_length=254)),
                ('govt_id', models.CharField(max_length=12)),
                ('id_type', models.CharField(choices=[('Aadhar_no', 'Aadhar no'), ('Driving_license', 'Driving license'), ('Pancard', 'Pancard')], max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='parceldetails',
            name='receiver_phone',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
