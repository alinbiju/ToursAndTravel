# Generated by Django 4.0.3 on 2022-04-25 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_booking_hotel_hotel_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_hotel',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
    ]
