# Generated by Django 4.0.3 on 2022-04-24 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_booking_hotel_adults_booking_hotel_dob_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_hotel',
            name='hotel_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.hotel_room'),
        ),
    ]
