# Generated by Django 3.0.8 on 2020-12-22 14:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0010_auto_20201219_1036'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Certificate',
        ),
        migrations.AlterField(
            model_name='update',
            name='update_time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 22, 14, 34, 9, 797687, tzinfo=utc)),
        ),
    ]