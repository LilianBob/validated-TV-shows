# Generated by Django 2.2 on 2021-05-29 09:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('validated_show_app', '0003_auto_20210529_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 29, 9, 0, 14, 741510, tzinfo=utc), null=True),
        ),
    ]
