# Generated by Django 2.2.6 on 2019-12-28 19:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='processor',
            name='Price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='processor',
            name='Add_Date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 28, 19, 18, 24, 573976, tzinfo=utc)),
        ),
    ]
