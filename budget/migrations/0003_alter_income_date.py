# Generated by Django 3.2.6 on 2021-08-25 08:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_auto_20210823_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 25, 8, 40, 23, 656318, tzinfo=utc)),
        ),
    ]