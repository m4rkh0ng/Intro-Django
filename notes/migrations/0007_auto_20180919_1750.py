# Generated by Django 2.1.1 on 2018-09-19 21:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20180918_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 18, 21, 50, 5, 770150, tzinfo=utc), editable=False),
        ),
    ]
