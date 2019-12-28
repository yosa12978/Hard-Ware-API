# Generated by Django 2.2.6 on 2019-12-28 19:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Processor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Model', models.CharField(max_length=50)),
                ('Series', models.CharField(default=None, max_length=50)),
                ('Company', models.CharField(max_length=50)),
                ('FLOPS', models.IntegerField(default=0)),
                ('Frequency', models.FloatField(default=0)),
                ('Chache_Memory', models.IntegerField(default=0)),
                ('Cores', models.IntegerField(default=0)),
                ('Socket', models.CharField(max_length=50)),
                ('Graphics_Core', models.BooleanField(default=False)),
                ('Add_Date', models.DateTimeField(default=datetime.datetime(2019, 12, 28, 19, 6, 21, 833491, tzinfo=utc))),
            ],
        ),
    ]