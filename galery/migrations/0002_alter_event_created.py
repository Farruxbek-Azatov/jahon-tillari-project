# Generated by Django 3.2.9 on 2021-12-10 08:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 10, 8, 12, 41, 287936, tzinfo=utc)),
        ),
    ]
