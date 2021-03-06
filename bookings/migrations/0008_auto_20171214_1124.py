# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-14 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_auto_20171128_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='time',
            name='time_slot',
            field=models.CharField(choices=[('9:00 to 9:30', '9:00 to 9:30'), ('10:00 to 10:30', '10:00 to 10:30'), ('11:00 to 11:30', '11:00 to 11:30')], max_length=32),
        ),
    ]
