# Generated by Django 3.1.5 on 2021-05-18 06:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0007_auto_20210514_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booked_from',
            field=models.DateField(default=datetime.date(2021, 5, 18)),
        ),
    ]
